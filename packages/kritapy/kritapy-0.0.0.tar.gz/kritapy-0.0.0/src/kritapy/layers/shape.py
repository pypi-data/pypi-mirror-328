from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
import xml.etree.ElementTree as ET

from .base import BaseLayer
from ..styles.layer import LayerStyle


@dataclass
class ShapeStyle:
    """Styling options for shapes."""
    fill: str = "none"  # Color or "none"
    stroke: str = "#000000"
    stroke_width: float = 1.0
    stroke_opacity: float = 1.0
    fill_opacity: float = 1.0
    stroke_linecap: str = "round"  # butt, round, square
    stroke_linejoin: str = "round"  # miter, round, bevel
    stroke_dasharray: Optional[str] = None


@dataclass
class Shape:
    """Base class for all vector shapes."""
    style: ShapeStyle = field(default_factory=ShapeStyle)
    transform: str = ""

    def get_svg_attributes(self) -> Dict[str, str]:
        """Get common SVG attributes for the shape."""
        attrs = {
            'fill': self.style.fill,
            'stroke': self.style.stroke,
            'stroke-width': str(self.style.stroke_width),
            'stroke-opacity': str(self.style.stroke_opacity),
            'fill-opacity': str(self.style.fill_opacity),
            'stroke-linecap': self.style.stroke_linecap,
            'stroke-linejoin': self.style.stroke_linejoin
        }
        if self.style.stroke_dasharray:
            attrs['stroke-dasharray'] = self.style.stroke_dasharray
        if self.transform:
            attrs['transform'] = self.transform
        return attrs

    def to_svg_element(self) -> ET.Element:
        """Convert shape to SVG element."""
        raise NotImplementedError


@dataclass
class Rectangle(Shape):
    """Rectangle shape."""
    x: float = 0
    y: float = 0
    width: float = 100
    height: float = 100
    rx: Optional[float] = None
    ry: Optional[float] = None

    def to_svg_element(self) -> ET.Element:
        attrs = self.get_svg_attributes()
        attrs.update({
            'x': str(self.x),
            'y': str(self.y),
            'width': str(self.width),
            'height': str(self.height)
        })
        if self.rx is not None:
            attrs['rx'] = str(self.rx)
        if self.ry is not None:
            attrs['ry'] = str(self.ry)
        return ET.Element('rect', attrs)


@dataclass
class Circle(Shape):
    """Circle shape."""
    cx: float = 0
    cy: float = 0
    r: float = 50

    def to_svg_element(self) -> ET.Element:
        attrs = self.get_svg_attributes()
        attrs.update({
            'cx': str(self.cx),
            'cy': str(self.cy),
            'r': str(self.r)
        })
        return ET.Element('circle', attrs)


@dataclass
class Ellipse(Shape):
    """Ellipse shape."""
    cx: float = 0
    cy: float = 0
    rx: float = 50
    ry: float = 30

    def to_svg_element(self) -> ET.Element:
        attrs = self.get_svg_attributes()
        attrs.update({
            'cx': str(self.cx),
            'cy': str(self.cy),
            'rx': str(self.rx),
            'ry': str(self.ry)
        })
        return ET.Element('ellipse', attrs)


@dataclass
class Path(Shape):
    """Path shape."""
    d: str = ""  # SVG path data

    def to_svg_element(self) -> ET.Element:
        attrs = self.get_svg_attributes()
        attrs['d'] = self.d
        return ET.Element('path', attrs)


@dataclass
class Line(Shape):
    """Line shape."""
    x1: float = 0
    y1: float = 0
    x2: float = 100
    y2: float = 100

    def to_svg_element(self) -> ET.Element:
        attrs = self.get_svg_attributes()
        attrs.update({
            'x1': str(self.x1),
            'y1': str(self.y1),
            'x2': str(self.x2),
            'y2': str(self.y2)
        })
        return ET.Element('line', attrs)


@dataclass
class ShapeGroup:
    """Group of shapes."""
    shapes: List[Shape]
    transform: str = ""

    def to_svg_element(self) -> ET.Element:
        group = ET.Element('g')
        if self.transform:
            group.set('transform', self.transform)
        for shape in self.shapes:
            group.append(shape.to_svg_element())
        return group


@dataclass
class ShapeLayer(BaseLayer):
    """A vector shape layer in a Krita document."""
    content: Union[List[Shape], List[ShapeGroup]] = field(default_factory=list)
    style: ShapeStyle = field(default_factory=ShapeStyle)
    layer_style: Optional[LayerStyle] = None

    def to_xml(self) -> dict:
        """Convert to XML attributes for maindoc.xml."""
        attrs = super().to_xml()
        attrs.update({
            'nodetype': 'shapelayer',
            'compositeop': 'normal',
        })
        if self.layer_style:
            attrs['layerstyle'] = "{" + self.layer_style.layer_style_uuid + "}"
        return attrs

    def get_svg_content(self) -> str:
        """Generate SVG content for the layer."""
        # Create root SVG element
        svg = ET.Element('svg', {
            'xmlns': 'http://www.w3.org/2000/svg',
            'xmlns:xlink': 'http://www.w3.org/1999/xlink',
            'xmlns:krita': 'http://krita.org/namespaces/svg/krita',
            'width': '100%',
            'height': '100%'
        })

        # Create group for the layer
        group = ET.SubElement(svg, 'g', {
            'id': 'shape0',
            'transform': f'translate({self.x}, {self.y})'
        })

        # Add shapes
        for item in self.content:
            group.append(item.to_svg_element())

        # Convert to string
        return ET.tostring(svg, encoding='unicode')