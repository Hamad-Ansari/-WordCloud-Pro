"""
Core word cloud generation engine using the wordcloud library.
Supports custom palettes, backgrounds, shapes, and masks.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from wordcloud import WordCloud, STOPWORDS
from typing import List, Tuple, Optional


def generate_wordcloud_image(
    text: str,
    palette: List[str],
    bg_color: str,
    shape: str = "circle",
    max_words: int = 100,
    min_font: int = 14,
    max_font: int = 80,
    width: int = 1200,
    height: int = 600,
) -> Image.Image:
    """
    Generate a word cloud image with custom styling.

    Args:
        text: Input text for word cloud
        palette: List of hex color strings
        bg_color: Background color (hex string)
        shape: Shape of the word cloud mask
        max_words: Maximum number of words
        min_font: Minimum font size
        max_font: Maximum font size
        width: Output image width
        height: Output image height

    Returns:
        PIL Image object of the generated word cloud
    """
    # Create mask based on shape
    mask = _create_mask(shape, width, height)

    # Build color function from palette
    def random_color_func(
        word=None, font_size=None, position=None, orientation=None, **kwargs
    ):
        import random
        return random.choice(palette)

    # Create word cloud
    wc = WordCloud(
        width=width,
        height=height,
        background_color=bg_color,
        max_words=max_words,
        mask=mask,
        stopwords=STOPWORDS,
        contour_width=2,
        contour_color=palette[0],
        color_func=random_color_func,
        min_font_size=min_font,
        max_font_size=max_font,
        prefer_horizontal=0.7,
        relative_scaling=0.5,
        colormap=None,  # Using custom color_func instead
    )

    wc.generate(text)
    return wc.to_image()


def _create_mask(shape: str, width: int, height: int) -> Optional[np.ndarray]:
    """
    Create a numpy mask array for the given shape.

    Args:
        shape: Shape name ('circle', 'square', 'rounded_square', 'diamond')
        width: Mask width
        height: Mask height

    Returns:
        Numpy array mask (255 = visible, 0 = hidden) or None
    """
    if shape == "circle":
        return _circle_mask(width, height)
    elif shape == "square":
        return _square_mask(width, height)
    elif shape == "rounded_square":
        return _rounded_square_mask(width, height)
    elif shape == "diamond":
        return _diamond_mask(width, height)
    elif shape == "custom":
        return _star_mask(width, height)
    return None


def _circle_mask(width: int, height: int) -> np.ndarray:
    """Create a circular mask."""
    x = np.arange(width)
    y = np.arange(height)
    xx, yy = np.meshgrid(x - width / 2, y - height / 2)
    mask = (xx**2 + yy**2) <= (min(width, height) / 2 - 10) ** 2
    return mask.astype(np.uint8) * 255


def _square_mask(width: int, height: int) -> np.ndarray:
    """Create a square mask."""
    margin = 10
    mask = np.zeros((height, width), dtype=np.uint8)
    mask[margin:-margin, margin:-margin] = 255
    return mask


def _rounded_square_mask(width: int, height: int, radius: int = 40) -> np.ndarray:
    """Create a rounded square mask."""
    mask = np.zeros((height, width), dtype=np.uint8)
    img = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(5, 5), (width - 5, height - 5)], radius=radius, fill=255)
    return np.array(img)


def _diamond_mask(width: int, height: int) -> np.ndarray:
    """Create a diamond-shaped mask."""
    x = np.arange(width)
    y = np.arange(height)
    xx, yy = np.meshgrid(x - width / 2, y - height / 2)
    mask = (np.abs(xx) / (width / 2) + np.abs(yy) / (height / 2)) <= 0.85
    return mask.astype(np.uint8) * 255


def _star_mask(width: int, height: int) -> np.ndarray:
    """Create a star-shaped mask."""
    img = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(img)

    cx, cy = width / 2, height / 2
    outer_r = min(width, height) / 2 - 10
    inner_r = outer_r * 0.4
    points = []
    for i in range(10):
        angle = (i * 36 - 90) * np.pi / 180
        r = outer_r if i % 2 == 0 else inner_r
        points.append((cx + r * np.cos(angle), cy + r * np.sin(angle)))

    draw.polygon(points, fill=255)
    return np.array(img)


def add_glow_effect(image: Image.Image, intensity: int = 20) -> Image.Image:
    """
    Add a subtle glow effect to the word cloud image.

    Args:
        image: PIL Image to add glow to
        intensity: Glow intensity (0-50)

    Returns:
        PIL Image with glow effect
    """
    # Convert to RGBA if needed
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Create a blurred copy for glow
    blurred = image.filter(ImageFilter.GaussianBlur(radius=intensity // 5))

    # Composite
    result = Image.alpha_composite(image, blurred)
    return result.convert("RGB")