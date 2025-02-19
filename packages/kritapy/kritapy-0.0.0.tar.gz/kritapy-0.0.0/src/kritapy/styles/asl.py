"""Adobe Style Library (ASL) format handling for KritaPy."""
import struct
from typing import List, Tuple, Any
from ..layers.base import BaseLayer


class ASLWriter:
    """Handles writing of ASL format files."""
    
    def __init__(self):
        self.buffer = bytearray()

    def write_string(self, s: str, string_type: str = "normal") -> None:
        """Write string in ASL format with proper encoding and padding.
        
        Args:
            s: String to write
            string_type: Type of string ("normal", "key", or "embedded")
        """
        if string_type == "key" and len(s) == 4:
            self.buffer.extend(s.encode('ascii'))
            return
            
        if string_type == "embedded":
            # Add null bytes between each character
            encoded = b''
            for c in s.encode('ascii'):
                encoded += bytes([c, 0])
            # Add final null terminator
            encoded += b'\x00\x00'
        else:
            encoded = s.encode('ascii')
            
        # Write length for variable-length strings
        if string_type != "key":
            self.buffer.extend(struct.pack('>I', len(encoded)))
        self.buffer.extend(encoded)
        
        # Add padding to align to 4 bytes
        padding = (4 - (len(encoded) % 4)) % 4
        if padding:
            self.buffer.extend(b'\x00' * padding)

    def write_header(self) -> None:
        """Write ASL file header."""
        self.buffer.extend(struct.pack('>H', 2))  # Version 2
        self.buffer.extend(b'8BSL')               # Signature
        self.buffer.extend(struct.pack('>H', 3))  # Patterns version
        self.buffer.extend(struct.pack('>I', 0))  # Patterns section size

    def write_style_block(self, layer: BaseLayer, style: Any) -> None:
        """Write a single style block.
        
        Args:
            layer: Layer the style belongs to
            style: Layer style configuration
        """
        # Record start position for size calculation
        start_pos = len(self.buffer)
        self.buffer.extend(b'\x00\x00\x00\x00')  # Size placeholder
        
        # Write null marker
        self.buffer.extend(b'null')
        
        # Write layer name
        self.buffer.extend(b'Nm  ')
        self.buffer.extend(b'TEXT')
        self.write_string(f"<{layer.name}> (embedded)", "embedded")
        
        # Write style UUID
        self.buffer.extend(b'Idnt')
        self.buffer.extend(b'TEXT')
        uuid_str = f"%{style.layer_style_uuid}"
        self.write_string(uuid_str, "embedded")
        
        # Write style descriptor
        self._write_style_descriptor(style)
        
        # Update block size
        size = len(self.buffer) - start_pos - 4
        struct.pack_into('>I', self.buffer, start_pos, size)

    def _write_style_descriptor(self, style: Any) -> None:
        """Write style descriptor data."""
        self.buffer.extend(b'Styl')
        self.buffer.extend(b'documentMode')
        self.buffer.extend(b'Objc')
        self.buffer.extend(b'documentMode')
        
        # Write effects block
        self.buffer.extend(b'Lefx')
        self.buffer.extend(b'Objc')
        self.buffer.extend(b'Lefx')
        
        # Write scale
        self.buffer.extend(b'Scl ')
        self.buffer.extend(b'UntF#Prc')
        self.buffer.extend(struct.pack('>d', style.scale))
        
        # Write master switch
        self.buffer.extend(b'masterFXSwitch')
        self.buffer.extend(b'bool')
        self.buffer.extend(struct.pack('>B', style.enabled))
        
        if style.stroke_enabled:
            self._write_stroke_effect(style)

    def _write_stroke_effect(self, style: Any) -> None:
        """Write stroke effect data."""
        self.buffer.extend(b'FrFX')
        self.buffer.extend(b'Objc')
        self.buffer.extend(b'FrFX')
        
        # Enabled flag
        self.buffer.extend(b'enab')
        self.buffer.extend(b'bool')
        self.buffer.extend(struct.pack('>B', 1))
        
        # Style type
        self.buffer.extend(b'Style')
        self.buffer.extend(b'enum')
        self.buffer.extend(b'FStl')
        self.buffer.extend(b'OutF')
        self.buffer.extend(b'PntT')
        
        # Fill style
        self.buffer.extend(b'enum')
        self.buffer.extend(b'FrFl')
        self.buffer.extend(b'SClr')
        
        # Blend mode
        self.buffer.extend(b'Md  ')
        self.buffer.extend(b'enum')
        self.buffer.extend(b'BlnM')
        self.buffer.extend(b'Nrml')
        
        # Opacity
        self.buffer.extend(b'Opct')
        self.buffer.extend(b'UntF#Prc')
        self.buffer.extend(struct.pack('>d', style.stroke_opacity))
        
        # Size
        self.buffer.extend(b'Sz  ')
        self.buffer.extend(b'UntF#Pxl')
        self.buffer.extend(struct.pack('>d', style.stroke_size))
        
        # Color
        self.buffer.extend(b'Clr ')
        self.buffer.extend(b'Objc')
        self.buffer.extend(b'RGBC')
        for channel, value in zip((b'Rd  ', b'Grn ', b'Bl  '), style.stroke_color):
            self.buffer.extend(channel)
            self.buffer.extend(b'doub')
            self.buffer.extend(struct.pack('>d', value))

    def create_asl(self, layers: List[Tuple[BaseLayer, Any]]) -> bytes:
        """Create complete ASL file from layers.
        
        Args:
            layers: List of (layer, style) tuples
        
        Returns:
            Complete ASL file as bytes
        """
        self.write_header()
        
        # Write number of styles
        num_styles = len([l for l, s in layers if s and s.has_effects])
        self.buffer.extend(struct.pack('>I', num_styles))
        
        # Write each style block
        for layer, style in layers:
            if style and style.has_effects:
                self.write_style_block(layer, style)
        
        return bytes(self.buffer)