from dataclasses import dataclass, field
from typing import List, Optional, Dict, Union
import xml.etree.ElementTree as ET

from .base import BaseLayer
from ..styles.layer import LayerStyle


@dataclass
class TextStyle:
    """Text styling options for Krita text layers.
    
    Attributes:
        font_family: Font family name
        font_size: Font size in points
        fill_color: Text fill color (hex or color name)
        stroke_color: Text outline color
        stroke_width: Outline width in pixels
        stroke_opacity: Outline opacity (0-1)
        letter_spacing: Space between letters in pixels
        word_spacing: Space between words in pixels
        text_align: Text alignment (start, end, center, justify)
        line_height: Line height multiplier
        use_rich_text: Whether to use rich text formatting
        text_rendering: Text rendering quality
        dominant_baseline: Vertical text alignment
        text_anchor: Horizontal text alignment
        paint_order: Order of fill/stroke painting
    """
    font_family: str = "Segoe UI"
    font_size: int = 12
    fill_color: str = "#000000"
    stroke_color: str = "#000000"
    stroke_width: int = 0
    stroke_opacity: float = 0.0
    letter_spacing: int = 0
    word_spacing: int = 0
    text_align: str = "start"  # start, end, center, justify
    text_align_last: str = "auto"
    line_height: float = 1.2
    use_rich_text: bool = False
    text_rendering: str = "auto"  # auto, optimizeSpeed, optimizeLegibility, geometricPrecision
    dominant_baseline: str = "middle"  # auto, middle, central, hanging
    text_anchor: str = "middle"  # start, middle, end
    paint_order: str = "stroke"  # fill, stroke
    stroke_linecap: str = "round"  # butt, round, square
    stroke_linejoin: str = "round"  # miter, round, bevel

    def __post_init__(self) -> None:
        """Validate style attributes."""
        self.validate()

    def validate(self) -> None:
        """Validate text style attributes.
        
        Raises:
            ValueError: If any attributes are invalid
        """
        valid_alignments = {"start", "end", "center", "justify"}
        valid_text_rendering = {"auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"}
        valid_baselines = {"auto", "middle", "central", "hanging"}
        valid_anchors = {"start", "middle", "end"}
        
        if self.text_align not in valid_alignments:
            raise ValueError(f"Invalid text alignment: {self.text_align}")
        if self.text_rendering not in valid_text_rendering:
            raise ValueError(f"Invalid text rendering: {self.text_rendering}")
        if self.dominant_baseline not in valid_baselines:
            raise ValueError(f"Invalid baseline: {self.dominant_baseline}")
        if self.text_anchor not in valid_anchors:
            raise ValueError(f"Invalid text anchor: {self.text_anchor}")

    def to_css(self) -> str:
        """Convert style to CSS string.
        
        Returns:
            CSS style string
        """
        return (
            f"font-family: {self.font_family};"
            f"font-size: {self.font_size}px;"
            f"text-align: {self.text_align};"
            f"text-align-last: {self.text_align_last};"
            f"line-height: {self.line_height};"
            f"dominant-baseline: {self.dominant_baseline};"
            f"text-anchor: {self.text_anchor};"
            f"paint-order: {self.paint_order};"
        )


@dataclass
class TextSpan:
    """Represents a span of text with positioning information.
    
    Attributes:
        text: The text content
        x: Horizontal position
        dy: Vertical offset from previous line
        style: Optional style overrides for this span
    """
    text: str
    x: float = 0
    dy: Optional[float] = None
    style: Optional[Dict[str, str]] = None

    def to_svg_element(self) -> ET.Element:
        """Convert span to SVG tspan element.
        
        Returns:
            ElementTree Element containing tspan data
        """
        attrs = {}
        if self.x is not None:
            attrs['x'] = str(self.x)
        if self.dy is not None:
            attrs['dy'] = str(self.dy)
        if self.style:
            attrs['style'] = ';'.join(f"{k}:{v}" for k, v in self.style.items())
            
        elem = ET.Element('tspan', attrs)
        elem.text = self.text
        return elem


@dataclass
class TextLayer(BaseLayer):
    """A text layer in a Krita document.
    
    Attributes:
        content: List of text spans or raw text
        style: Text styling options
        layer_style: Layer effects (stroke, shadow, etc.)
    """
    content: Union[str, List[TextSpan]] = field(default_factory=list)
    style: TextStyle = field(default_factory=TextStyle)
    layer_style: Optional[LayerStyle] = None
    nodetype: str = "shapelayer"  # Krita stores text in shape layers

    def __post_init__(self) -> None:
        """Initialize text layer content."""
        super().__post_init__()
        
        # Convert string content to TextSpan
        if isinstance(self.content, str):
            self.content = [TextSpan(
                text=line,
                x=0,
                dy=self.style.font_size * self.style.line_height if i > 0 else None
            ) for i, line in enumerate(self.content.split('\n'))]

    def to_xml(self) -> Dict[str, str]:
        """Convert to XML attributes for maindoc.xml."""
        attrs = super().to_xml()
        if self.layer_style:
            attrs['layerstyle'] = "{" + self.layer_style.layer_style_uuid + "}"
        return attrs

    def get_svg_element(self) -> ET.Element:
        """Generate SVG text element.
        
        Returns:
            ElementTree Element containing SVG text
        """
        attrs = {
            'id': 'shape0',
            'krita:useRichText': str(self.style.use_rich_text).lower(),
            'text-rendering': self.style.text_rendering,
            'krita:textVersion': '3',
            'transform': f'translate({self.x}, {self.y})',
            'fill': self.style.fill_color,
            'stroke': self.style.stroke_color,
            'stroke-width': str(self.style.stroke_width),
            'stroke-opacity': str(self.style.stroke_opacity),
            'stroke-linecap': self.style.stroke_linecap,
            'stroke-linejoin': self.style.stroke_linejoin,
            'letter-spacing': str(self.style.letter_spacing),
            'word-spacing': str(self.style.word_spacing),
            'style': self.style.to_css()
        }
        
        text_elem = ET.Element('text', attrs)
        
        # Add spans
        for span in self.content:
            text_elem.append(span.to_svg_element())
            
        return text_elem

    @classmethod
    def from_text(cls, text: str, **kwargs) -> 'TextLayer':
        """Create a TextLayer from plain text.
        
        Args:
            text: Text content
            **kwargs: Additional layer attributes
            
        Returns:
            New TextLayer instance
        """
        style = kwargs.pop('style', TextStyle())
        return cls(content=text, style=style, **kwargs)