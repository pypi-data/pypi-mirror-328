import colorsys
import random
import re

from pydreamplet.utils import constrain, math_round


def hexStr(n):
    """
    Converts an integer (0-255) to a two-digit hexadecimal string.
    """
    return format(n, "02x")


def random_int(min_val, max_val):
    """Returns a random integer N such that min_val <= N <= max_val."""
    return random.randint(min_val, max_val)


def str2rgb(col):
    """
    Converts a hex color string to an RGB dictionary.
    Accepts strings in the format "#RRGGBB" or "#RGB".
    If the input doesn't match, returns {'r': 0, 'g': 0, 'b': 0}.
    """
    rgb = {"r": 0, "g": 0, "b": 0}
    # Regex matches a string starting with one or more '#' and then either 6 or 3 hex digits.
    rgx = re.compile(r"^#+([a-fA-F\d]{6}|[a-fA-F\d]{3})$")
    if rgx.match(col):
        # Expand shorthand (e.g. "#abc" -> "#aabbcc")
        if len(col) == 4:
            col = "#" + col[1] * 2 + col[2] * 2 + col[3] * 2
        try:
            rgb["r"] = int(col[1:3], 16)
            rgb["g"] = int(col[3:5], 16)
            rgb["b"] = int(col[5:7], 16)
        except ValueError:
            # In case of conversion error, keep default (0,0,0)
            pass
    return rgb


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """
    Convert a hex color string (e.g., "#ff0000") to an (R, G, B) tuple.
    """
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError("Hex color must be in the format RRGGBB")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """
    Convert an (R, G, B) tuple to a hex color string.
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def color2rgba(c, alpha=1):
    """
    Converts an input color (which can be a list/tuple of three numbers,
    an integer, or a hex string) and an alpha value to an "rgba(r, g, b, a)" string.
    """
    r = g = b = 0
    a = 1
    if isinstance(c, (list, tuple)):
        if len(c) == 3:
            r = constrain(c[0], 0, 255)
            g = constrain(c[1], 0, 255)
            b = constrain(c[2], 0, 255)
            a = constrain(alpha, 0, 1)
        else:
            r = g = b = 0
            a = 1
    elif isinstance(c, int):
        r = g = b = constrain(c, 0, 255)
        a = constrain(alpha, 0, 1)
    elif isinstance(c, str):
        rgb = str2rgb(c)
        r = rgb.get("r", 0)
        g = rgb.get("g", 0)
        b = rgb.get("b", 0)
        a = constrain(alpha, 0, 1)
    return f"rgba({r}, {g}, {b}, {a})"


def blend(color1, color2, proportion):
    """
    Blends two hex color strings by the given proportion.
    proportion: 0 returns color1, 1 returns color2.
    Returns the blended color as a hex string.
    """
    proportion = constrain(proportion, 0, 1)
    # Ensure the colors start with '#'
    c1 = color1 if color1.startswith("#") else "#" + color1
    c2 = color2 if color2.startswith("#") else "#" + color2

    # Regex to test for valid hex color (3 or 6 hex digits)
    rgx = re.compile(r"^#+([a-fA-F\d]{6}|[a-fA-F\d]{3})$")
    if rgx.match(c1) and rgx.match(c2):
        # Remove leading '#' and expand shorthand if necessary.
        col1 = c1[1:]
        col2 = c2[1:]
        if len(col1) == 3:
            col1 = "".join([ch * 2 for ch in col1])
        if len(col2) == 3:
            col2 = "".join([ch * 2 for ch in col2])
        try:
            r1 = int(col1[0:2], 16)
            r2 = int(col2[0:2], 16)
            r = math_round((1 - proportion) * r1 + proportion * r2)
            g1 = int(col1[2:4], 16)
            g2 = int(col2[2:4], 16)
            g = math_round((1 - proportion) * g1 + proportion * g2)
            b1 = int(col1[4:6], 16)
            b2 = int(col2[4:6], 16)
            b = math_round((1 - proportion) * b1 + proportion * b2)
            return "#" + hexStr(r) + hexStr(g) + hexStr(b)
        except Exception:
            return "#000000"
    else:
        return "#000000"


def random_color():
    """
    Generates a random hex color string.
    """
    r = hexStr(random_int(0, 255))
    g = hexStr(random_int(0, 255))
    b = hexStr(random_int(0, 255))
    return "#" + r + g + b


def generate_colors(base_color: str, n=4, harmony="complementary"):
    """
    Generate a list of colors based on a selected color harmony.

    Parameters:
        base_color (str): The starting color in hex format (e.g., "#db45f9").
        n (int): Number of colors to generate.
        harmony (str): The type of harmony to use. Supported options:
            - "complementary": Base color and its opposite on the color wheel.
            - "compound": Base color with a split complement (two hues adjacent to the complement).
            - "square": Four colors evenly spaced around the color wheel.

    Returns:
        list[str]: A list of hex color strings.
    """

    def generate_variations(light, count, delta=0.2):
        """
        Generate a list of `count` lightness values centered around the original lightness `light`,
        spread by ±delta (clamped between 0 and 1).
        """
        l_min = max(0, light - delta)
        l_max = min(1, light + delta)
        if count == 1:
            return [light]
        step = (l_max - l_min) / (count - 1)
        return [l_min + i * step for i in range(count)]

    def distribute_counts(total, groups):
        """
        Evenly distribute `total` items into `groups` buckets.
        Returns a list of counts for each group.
        """
        base = total // groups
        remainder = total % groups
        return [base + 1 if i < remainder else base for i in range(groups)]

    # Convert the base color to an RGB tuple (0-255)
    r, g, b = hex_to_rgb(base_color)
    # Normalize RGB to 0-1 for colorsys
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
    # Convert RGB to HLS (Hue, Lightness, Saturation)
    h, l, s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)

    harmony = harmony.lower()
    if harmony == "complementary":
        hues = [h, (h + 0.5) % 1]
    elif harmony == "compound":
        # Compound (split-complementary) uses the base hue and two hues adjacent to its complement.
        offset = 0.08  # This offset can be adjusted for taste.
        hues = [h, (h + 0.5 - offset) % 1, (h + 0.5 + offset) % 1]
    elif harmony == "square":
        # Square harmony: Four colors evenly spaced around the color wheel.
        hues = [h, (h + 0.25) % 1, (h + 0.5) % 1, (h + 0.75) % 1]
    else:
        raise ValueError(f"Unsupported harmony type: {harmony}")

    num_groups = len(hues)
    counts = distribute_counts(n, num_groups)

    group_colors = []
    for idx, hue in enumerate(hues):
        count = counts[idx]
        l_values = generate_variations(l, count)
        group = []
        for lv in l_values:
            # Convert from HLS back to RGB (normalized to 0-1)
            r_new, g_new, b_new = colorsys.hls_to_rgb(hue, lv, s)
            # Scale to 0-255 and round using math_round
            rgb_int = (
                math_round(r_new * 255),
                math_round(g_new * 255),
                math_round(b_new * 255),
            )
            group.append(rgb_to_hex(rgb_int))
        group_colors.append(group)

    # Interleave colors from each group to form a balanced palette.
    palette = []
    max_len = max(len(group) for group in group_colors)
    for i in range(max_len):
        for group in group_colors:
            if i < len(group):
                palette.append(group[i])

    return palette[:n]
