from dataclasses import dataclass, field
from typing import Optional, Tuple
import uuid


@dataclass
class LayerStyle:
    """Represents a Krita layer style.
    
    Attributes:
        enabled: Whether the style is enabled
        scale: Scale of the style effects (percentage)
        stroke_enabled: Whether stroke effect is enabled
        stroke_style: Type of stroke ("OutF" for outside frame)
        stroke_blend_mode: Blend mode for stroke ("Nrml" for normal)
        stroke_opacity: Opacity of stroke (percentage)
        stroke_size: Size of stroke in pixels
        stroke_color: RGB color tuple for stroke
        layer_style_uuid: Unique identifier for the style
    """
    enabled: bool = True
    scale: float = 100.0
    layer_style_uuid: Optional[str] = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    # Stroke Effect
    stroke_enabled: bool = False
    stroke_style: str = "OutF"  # OutF for outside frame
    stroke_blend_mode: str = "Nrml"  # Nrml for normal blend mode
    stroke_opacity: float = 100.0
    stroke_size: float = 3.0
    stroke_color: Tuple[float, float, float] = (255, 255, 255)

    def __post_init__(self):
        if not self.layer_style_uuid:
            self.layer_style_uuid = str(uuid.uuid4())
        
        # Remove hyphens from UUID if present
        self.layer_style_uuid = self.layer_style_uuid.replace("-", "")

    @property
    def has_effects(self) -> bool:
        """Check if the style has any effects enabled."""
        return self.stroke_enabled  # Add more effects here as they're implemented (ToDo)