"""Paint layer implementation for KritaPy."""
import math
import numpy as np
from dataclasses import dataclass, field
from typing import Union
from PIL import Image
import lzf

from .base import BaseLayer


@dataclass
class PaintLayer(BaseLayer):
    """A raster paint layer in a Krita document."""
    image: Union[str, Image.Image]  # Path or PIL Image
    colorspace: str = "RGBA"

    def __post_init__(self):
        super().__post_init__()
        # Convert string path to PIL Image
        if isinstance(self.image, str):
            self.image = Image.open(self.image)
        
        # Convert to RGBA if needed
        if self.image.mode != "RGBA":
            self.image = self.image.convert("RGBA")

    def to_xml(self) -> dict:
        """Convert to XML attributes for maindoc.xml."""
        attrs = super().to_xml()
        attrs.update({
            'nodetype': 'paintlayer',
            'compositeop': 'normal',
            'colorspacename': self.colorspace,
            'channelflags': '',
            'channellockflags': '',
            'onionskin': '0'
        })
        return attrs

    def save_to_file(self, path: str) -> None:
        """Save layer data in Krita's format.
        
        Args:
            path: Output path for the layer data
        """
        w, h = self.image.size
        
        # Calculate tiles
        tile_size = 64
        nx = math.ceil(w / tile_size)
        ny = math.ceil(h / tile_size)
        
        # Prepare tile entries
        tile_entries = []
        
        for ty in range(ny):
            for tx in range(nx):
                left = tx * tile_size
                top = ty * tile_size
                
                # Create and initialize tile
                tile = Image.new("RGBA", (tile_size, tile_size), (0, 0, 0, 0))
                crop = self.image.crop((left, top, 
                                      min(left + tile_size, w), 
                                      min(top + tile_size, h)))
                tile.paste(crop, (0, 0))
                
                # Convert to numpy array
                data = np.array(tile, dtype=np.uint8)
                
                # Create planar data (BGRA order)
                planes = [
                    data[:, :, 2].flatten(),  # Blue
                    data[:, :, 1].flatten(),  # Green
                    data[:, :, 0].flatten(),  # Red
                    data[:, :, 3].flatten(),  # Alpha
                ]
                plane_data = np.concatenate(planes).tobytes()
                
                # Compress tile
                compressed = lzf.compress(plane_data)
                if not compressed:
                    compressed = b""
                
                # Create tile header and data
                tile_data = b"\x01" + compressed
                tile_header = f"{left},{top},LZF,{len(tile_data)}\n".encode("utf-8")
                tile_entries.append((tile_header, tile_data))
        
        # Write file
        header = [
            b"VERSION 2\n",
            f"TILEWIDTH {tile_size}\n".encode("utf-8"),
            f"TILEHEIGHT {tile_size}\n".encode("utf-8"),
            b"PIXELSIZE 4\n",
            f"DATA {len(tile_entries)}\n".encode("utf-8"),
        ]
        
        with open(path, "wb") as f:
            # Write header
            f.write(b"".join(header))
            
            # Write tiles
            for header, data in tile_entries:
                f.write(header)
                f.write(data)