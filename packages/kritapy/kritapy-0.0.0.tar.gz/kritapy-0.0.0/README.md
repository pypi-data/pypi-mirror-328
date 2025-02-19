# Krita Python Library Documentation

## Overview
The Krita Python Library provides a simple and intuitive way to programmatically create and manipulate Krita (.kra) files. It supports creating documents with multiple layers, including text, shapes, and images.

## Installation

```bash
pip install kritapy
```

## Basic Usage

```python
from kritapy import KritaDocument, TextStyle, ShapeStyle, ShapeLayer

# Create a new document
doc = KritaDocument(width=1280, height=1024)

# Add some content
doc.add_text_layer("Hello Krita!")
doc.add_image_layer("background.jpg")

# Save the document
doc.save("output.kra")
```

## Core Components

### KritaDocument
The main class for creating and managing Krita documents.

```python
doc = KritaDocument(width=1280, height=1024)
```

Parameters:
- `width` (int): Document width in pixels (default: 1024)
- `height` (int): Document height in pixels (default: 1024)

### Layer Types

#### Text Layers
Text layers can be created in two ways:

1. Simple method:
```python
doc.add_text_layer(
    text="Hello Krita!",
    name="My Text",
    x=100,
    y=100
)
```

2. Advanced method with styling:
```python
text_style = TextStyle(
    font_family="Arial",
    font_size=24,
    fill_color="#000000",
    stroke_color="#FFFFFF",
    stroke_width=1,
    stroke_opacity=1.0,
    letter_spacing=0,
    text_align="start"
)

text_layer = ShapeLayer.from_text(
    text="Hello\nMultiline Text",
    name="Styled Text",
    x=100,
    y=100,
    style=text_style
)

doc.add_text_layer(text_layer)
```

#### Image Layers
Add raster images to your document:

```python
doc.add_image_layer(
    image="path/to/image.jpg",  # Can be path or PIL Image
    name="Background",
    opacity=255,
    x=0,
    y=0
)
```

#### Shape Layers
Create vector shapes using various primitives:

```python
from krita_lib import Rectangle, Circle, Ellipse, Line, Path, ShapeGroup

# Create shape style
shape_style = ShapeStyle(
    fill="#FF0000",
    stroke="#000000",
    stroke_width=2.0,
    stroke_opacity=1.0,
    fill_opacity=0.5
)

# Create shapes
rect = Rectangle(
    x=100,
    y=100,
    width=200,
    height=150,
    rx=10,  # rounded corners
    style=shape_style
)

circle = Circle(
    cx=300,
    cy=300,
    r=50,
    style=shape_style
)

# Add shapes to document
doc.add_shape_layer(
    ShapeGroup([rect, circle]),
    name="My Shapes"
)
```

### Working with Paths
Create complex vector paths using SVG path commands:

```python
path = Path(
    d="M 100 100 L 200 100 L 150 50 Z",  # Triangle
    style=ShapeStyle(
        fill="#00FF00",
        stroke="#000000",
        stroke_width=2
    )
)

doc.add_shape_layer(path, name="Path Layer")
```

Common SVG Path Commands:
- `M x y` - Move to
- `L x y` - Line to
- `H x` - Horizontal line
- `V y` - Vertical line
- `Q x1 y1 x y` - Quadratic curve
- `C x1 y1 x2 y2 x y` - Cubic curve
- `Z` - Close path

## Styling Options

### TextStyle Properties
- `font_family`: Font name (e.g., "Arial")
- `font_size`: Font size in points
- `fill_color`: Text color in hex format
- `stroke_color`: Outline color
- `stroke_width`: Outline width
- `stroke_opacity`: Outline opacity (0-1)
- `letter_spacing`: Space between letters
- `word_spacing`: Space between words
- `text_align`: Text alignment ("start", "end", "center", "justify")
- `line_height`: Line spacing multiplier
- `use_rich_text`: Enable rich text formatting
- `text_rendering`: Text rendering mode

### ShapeStyle Properties
- `fill`: Fill color or "none"
- `stroke`: Stroke color
- `stroke_width`: Stroke width
- `stroke_opacity`: Stroke opacity (0-1)
- `fill_opacity`: Fill opacity (0-1)
- `stroke_linecap`: Line endings ("butt", "round", "square")
- `stroke_linejoin`: Line joins ("miter", "round", "bevel")
- `stroke_dasharray`: Dash pattern (e.g., "5,5")

## Complete Example

```python
from krita_lib import (
    KritaDocument, TextStyle, ShapeStyle,
    ShapeLayer, Rectangle, Circle, Path, ShapeGroup
)

# Create document
doc = KritaDocument(width=1280, height=1024)

# Add styled text
text_style = TextStyle(
    font_family="Arial",
    font_size=24,
    fill_color="#000000",
    stroke_color="#FFFFFF",
    stroke_width=1
)

text_layer = ShapeLayer.from_text(
    text="Hello Krita!\nMultiline Text",
    name="Title",
    x=100,
    y=100,
    style=text_style
)

doc.add_text_layer(text_layer)

# Add shapes
shape_style = ShapeStyle(
    fill="#FF0000",
    stroke="#000000",
    stroke_width=2
)

shapes = [
    Rectangle(x=80, y=80, width=300, height=150, rx=10, style=shape_style),
    Circle(cx=230, cy=155, r=100, style=shape_style),
    Path(
        d="M 100 150 Q 130 140, 160 150 Q 190 160, 220 150",
        style=ShapeStyle(fill="none", stroke="#0000FF", stroke_width=2)
    )
]

doc.add_shape_layer(ShapeGroup(shapes), name="Decorative Shapes")

# Add background image
doc.add_image_layer("background.jpg", name="Background")

# Save the document
doc.save("output.kra")
```

## Best Practices
1. Create styles separately from layers for better code organization
2. Group related shapes using ShapeGroup
3. Consider layer order - earlier layers appear behind later ones
4. Use meaningful layer names
5. Clean up resources by closing the document after saving

## Error Handling
The library throws standard Python exceptions:
- `TypeError`: Invalid parameter types
- `ValueError`: Invalid parameter values
- `FileNotFoundError`: Missing image files
- `OSError`: File system related errors

## Limitations
- Text formatting is limited to single style per layer
- Some advanced Krita features not supported (filters, masks, etc.)
- Limited animation support

## Contributing
Contributions are welcome! Please check our GitHub repository for guidelines.