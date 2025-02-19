"""Base layer class definitions for KritaPy."""
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
import uuid
import xml.etree.ElementTree as ET


@dataclass
class BaseLayer:
    """Base class for all Krita layers.
    
    This class provides the core functionality and attributes that all Krita
    layer types (text, shape, paint) must implement.
    
    Attributes:
        name: Layer name as shown in Krita
        visible: Whether layer is visible
        opacity: Layer opacity (0-255)
        x: Horizontal position
        y: Vertical position
        uuid: Unique identifier for the layer
    """
    name: str
    visible: bool = True
    opacity: int = 255
    x: float = 0
    y: float = 0
    uuid: str = field(default_factory=lambda: "{" + str(uuid.uuid4()) + "}")
    nodetype: str = "base"  # Override in subclasses

    def __post_init__(self) -> None:
        """Validate and format layer attributes after initialization."""
        # Ensure opacity is in valid range
        self.opacity = max(0, min(255, self.opacity))
        
        # Ensure UUID has proper format
        if not self.uuid.startswith("{"):
            self.uuid = "{" + self.uuid
        if not self.uuid.endswith("}"):
            self.uuid = self.uuid + "}"

    def to_xml(self) -> Dict[str, str]:
        """Convert layer attributes to XML format for maindoc.xml.
        
        Returns:
            Dictionary of XML attributes
        """
        return {
            'visible': '1' if self.visible else '0',
            'name': self.name,
            'uuid': self.uuid,
            'x': str(self.x),
            'y': str(self.y),
            'opacity': str(self.opacity),
            'nodetype': self.nodetype,
            'intimeline': '0',
            'collapsed': '0',
            'colorlabel': '0',
            'locked': '0',
            'channelflags': '',
            'compositeop': 'normal'
        }

    def get_svg_element(self) -> ET.Element:
        """Generate SVG element for the layer.
        
        Returns:
            ElementTree Element containing SVG data
        
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement get_svg_element()")

    def generate_uuid(self) -> None:
        """Generate a new UUID for the layer."""
        self.uuid = "{" + str(uuid.uuid4()) + "}"
        
    def validate(self) -> None:
        """Validate layer attributes.
        
        Raises:
            ValueError: If any attributes are invalid
        """
        if not self.name:
            raise ValueError("Layer name cannot be empty")
        if not 0 <= self.opacity <= 255:
            raise ValueError("Opacity must be between 0 and 255")