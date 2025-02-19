"""Main KritaDocument implementation."""
import os
import shutil
from datetime import datetime
from typing import List, Union, Optional, Dict, Any
from zipfile import ZipFile, ZIP_STORED
import xml.etree.ElementTree as ET
from PIL import Image

from .layers.base import BaseLayer
from .layers.text import TextLayer
from .layers.shape import ShapeLayer, Shape, ShapeGroup
from .layers.paint import PaintLayer
from .styles.asl import ASLWriter


class KritaDocument:
    """Main class for creating and manipulating Krita documents.
    
    This class handles the creation and management of Krita documents, including
    layer management, file saving, and resource handling.
    
    Attributes:
        width: Document width in pixels
        height: Document height in pixels
        layers: List of layers in the document
        temp_dir: Directory for temporary files
    """

    def __init__(self, width: int = 1024, height: int = 1024):
        """Initialize a new Krita document.
        
        Args:
            width: Document width in pixels
            height: Document height in pixels
        """
        self.width = width
        self.height = height
        self.layers: List[BaseLayer] = []
        self.temp_dir = "krita_temp"

    def add_layer(self, layer: BaseLayer) -> None:
        """Add a layer to the document.
        
        Args:
            layer: Layer to add (TextLayer, ShapeLayer, or PaintLayer)
        """
        layer.validate()  # Ensure layer is valid
        self.layers.append(layer)

    def save(self, output_path: str) -> None:
        """Save the document as a .kra file.
        
        Args:
            output_path: Path where to save the .kra file
        """
        try:
            # Create temporary directory structure
            for subdir in ['layers', 'annotations', 'animation']:
                os.makedirs(os.path.join(self.temp_dir, subdir), exist_ok=True)

            with ZipFile(output_path, 'w', ZIP_STORED) as zf:
                # Add mimetype (must be first)
                zf.writestr('mimetype', 'application/x-krita')

                # Create and add XML files
                self._add_document_info(zf)
                self._add_main_doc(zf)
                self._add_animation_metadata(zf)
                
                # Process layers
                self._process_layers(zf)

                # Add preview
                self._create_preview(zf)

                # Add layer styles if needed
                if self._has_layer_styles():
                    self._add_layer_styles(zf)

                # Add all files from temp directory to zip
                self._add_temp_files(zf)

        finally:
            # Clean up
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)

    def _create_document_info(self) -> ET.Element:
        """Create the documentinfo.xml structure.
        
        Returns:
            XML Element tree for documentinfo.xml
        """
        doc_info = ET.Element('document-info', {
            'xmlns': 'http://www.calligra.org/DTD/document-info'
        })

        # About section
        about = ET.SubElement(doc_info, 'about')
        for tag in ['title', 'description', 'subject', 'abstract', 'keyword']:
            ET.SubElement(about, tag)
        
        # Creator info
        creator = ET.SubElement(about, 'initial-creator')
        creator.text = 'KritaPy'
        
        # Editing info
        cycles = ET.SubElement(about, 'editing-cycles')
        cycles.text = '1'
        ET.SubElement(about, 'editing-time')
        
        # Dates
        now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        for tag in ['date', 'creation-date']:
            elem = ET.SubElement(about, tag)
            elem.text = now
        
        # Additional metadata
        ET.SubElement(about, 'language')
        ET.SubElement(about, 'license')
        
        # Author section
        author = ET.SubElement(doc_info, 'author')
        for tag in ['full-name', 'creator-first-name', 'creator-last-name',
                   'initial', 'author-title', 'position', 'company']:
            ET.SubElement(author, tag)
        
        return doc_info

    def _create_main_doc(self) -> ET.Element:
        """Create the maindoc.xml structure.
        
        Returns:
            XML Element tree for maindoc.xml
        """
        # Root element
        doc = ET.Element('DOC', {
            'xmlns': 'http://www.calligra.org/DTD/krita',
            'kritaVersion': '5.2.9',
            'syntaxVersion': '2.0',
            'editor': 'Krita'
        })
        
        # Image element
        image = ET.SubElement(doc, 'IMAGE', {
            'width': str(self.width),
            'height': str(self.height),
            'mime': 'application/x-kra',
            'name': 'Unnamed',
            'description': '',
            'y-res': '300',
            'x-res': '300',
            'colorspacename': 'RGBA',
            'profile': 'sRGB-elle-V2-srgbtrc.icc'
        })
        
        # Layers
        layers_elem = ET.SubElement(image, 'layers')
        for layer in self.layers:
            ET.SubElement(layers_elem, 'layer', layer.to_xml())
        
        # Background color
        bg_color = ET.SubElement(image, 'ProjectionBackgroundColor')
        bg_color.set('ColorData', 'AAAAAA==')
        
        # Global color
        global_color = ET.SubElement(image, 'GlobalAssistantsColor')
        global_color.set('SimpleColorData', '176,176,176,255')
        
        # Add mirror axis section
        self._add_mirror_axis(image)
        
        # Additional sections
        ET.SubElement(image, 'Palettes')
        ET.SubElement(image, 'resources')
        
        # Animation
        self._add_animation_section(image)
        
        return doc

    def _add_mirror_axis(self, parent: ET.Element) -> None:
        """Add mirror axis section to the document.
        
        Args:
            parent: Parent XML element
        """
        mirror_axis = ET.SubElement(parent, 'MirrorAxis')
        
        # Add mirror properties
        for prop, value in [
            ('mirrorHorizontal', '0'),
            ('mirrorVertical', '0'),
            ('lockHorizontal', '0'),
            ('lockVertical', '0'),
            ('hideHorizontalDecoration', '0'),
            ('hideVerticalDecoration', '0'),
            ('handleSize', '32')
        ]:
            elem = ET.SubElement(mirror_axis, prop)
            elem.set('value', value)
            elem.set('type', 'value')
        
        # Add axis position
        pos = ET.SubElement(mirror_axis, 'axisPosition')
        pos.set('x', str(self.width // 2))
        pos.set('y', str(self.height // 2))
        pos.set('type', 'pointf')

    def _add_animation_section(self, parent: ET.Element) -> None:
        """Add animation section to the document.
        
        Args:
            parent: Parent XML element
        """
        animation = ET.SubElement(parent, 'animation')
        
        # Framerate
        framerate = ET.SubElement(animation, 'framerate')
        framerate.set('value', '24')
        framerate.set('type', 'value')
        
        # Range
        range_elem = ET.SubElement(animation, 'range')
        range_elem.set('from', '0')
        range_elem.set('to', '100')
        range_elem.set('type', 'timerange')
        
        # Current time
        time_elem = ET.SubElement(animation, 'currentTime')
        time_elem.set('value', '0')
        time_elem.set('type', 'value')

    def _add_document_info(self, zf: ZipFile) -> None:
        """Add documentinfo.xml to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        doc_info = self._create_document_info()
        doc_info_str = ('<?xml version="1.0" encoding="UTF-8"?>\n' + 
                       ET.tostring(doc_info, encoding='unicode'))
        zf.writestr('documentinfo.xml', doc_info_str)

    def _add_main_doc(self, zf: ZipFile) -> None:
        """Add maindoc.xml to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        main_doc = self._create_main_doc()
        main_doc_str = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                       '<!DOCTYPE DOC PUBLIC \'-//KDE//DTD krita 2.0//EN\' '
                       '\'http://www.calligra.org/DTD/krita-2.0.dtd\'>\n' +
                       ET.tostring(main_doc, encoding='unicode'))
        zf.writestr('maindoc.xml', main_doc_str)

    def _process_layers(self, zf: ZipFile) -> None:
        """Process and add all layers to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        for i, layer in enumerate(self.layers, start=1):
            layer_path = os.path.join(self.temp_dir, 'layers', f'layer{i}')
            
            if isinstance(layer, (TextLayer, ShapeLayer)):
                # Create .shapelayer directory
                shape_dir = f"{layer_path}.shapelayer"
                os.makedirs(shape_dir, exist_ok=True)
                
                # Create SVG content
                svg_path = os.path.join(shape_dir, 'content.svg')
                with open(svg_path, 'w', encoding='utf-8') as f:
                    f.write(self._create_svg_wrapper(layer.get_svg_element()))
                    
            elif isinstance(layer, PaintLayer):
                # Save layer data
                layer.save_to_file(layer_path)
                
                # Add default pixel
                with open(f"{layer_path}.defaultpixel", 'wb') as f:
                    f.write(bytes([0, 0, 0, 0]))

    def _create_svg_wrapper(self, content: ET.Element) -> str:
        """Create complete SVG document wrapper.
        
        Args:
            content: SVG content element
        
        Returns:
            Complete SVG document as string
        """
        return f'''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" 
 "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<!-- Created using KritaPy -->
{ET.tostring(content, encoding='unicode')}'''

    def _create_preview(self, zf: ZipFile) -> None:
        """Create and add preview.png to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        if self.layers and isinstance(self.layers[-1], PaintLayer):
            preview = self.layers[-1].image.copy()
        else:
            preview = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        
        preview.thumbnail((256, 256))
        preview_path = os.path.join(self.temp_dir, 'preview.png')
        preview.save(preview_path)
        zf.write(preview_path, 'preview.png')
        os.remove(preview_path)

    def _has_layer_styles(self) -> bool:
        """Check if document has any layer styles.
        
        Returns:
            True if any layer has styles
        """
        return any(isinstance(l, (TextLayer, ShapeLayer)) and l.layer_style 
                  for l in self.layers)

    def _add_layer_styles(self, zf: ZipFile) -> None:
        """Add layer styles to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        writer = ASLWriter()
        styled_layers = [(l, l.layer_style) for l in self.layers 
                        if isinstance(l, (TextLayer, ShapeLayer)) and l.layer_style]
        asl_data = writer.create_asl(styled_layers)
        zf.writestr('annotations/layerstyles.asl', asl_data)

    def _add_temp_files(self, zf: ZipFile) -> None:
        """Add all files from temp directory to zip.
        
        Args:
            zf: ZipFile to add to
        """
        for root, _, files in os.walk(self.temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, self.temp_dir)
                zf.write(file_path, arcname)

    def _add_animation_metadata(self, zf: ZipFile) -> None:
        """Add animation metadata to the zip file.
        
        Args:
            zf: ZipFile to add to
        """
        metadata = '''<?xml version="1.0" encoding="UTF-8"?>
<animation-metadata xmlns="http://www.calligra.org/DTD/krita">
<framerate type="value" value="24"/>
<range from="0" type="timerange" to="100"/>
<currentTime type="value" value="0"/>
<export-settings>
<sequenceFilePath type="value" value=""/>
<sequenceBaseName type="value" value=""/>
<sequenceInitialFrameNumber type="value" value="-1"/>
</export-settings>
</animation-metadata>'''
        zf.writestr('animation/index.xml', metadata)