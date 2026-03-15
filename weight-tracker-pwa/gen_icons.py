from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), '#1a1a1a')
    draw = ImageDraw.Draw(img)
    # Draw a simple "W" scale icon
    margin = size * 0.15
    cx = size / 2
    cy = size / 2
    r = size * 0.35
    # Circle for scale
    draw.ellipse([cx-r, cy-r*0.6, cx+r, cy+r*0.8], outline='white', width=max(2, size//48))
    # Needle
    import math
    angle = -0.4
    nx = cx + r * 0.55 * math.cos(math.pi + angle)
    ny = cy - r * 0.55 * math.sin(angle) * 0.6
    draw.line([cx, cy, nx, ny], fill='white', width=max(2, size//48))
    # Center dot
    dot = size * 0.04
    draw.ellipse([cx-dot, cy-dot, cx+dot, cy+dot], fill='white')
    # Tick marks
    for i in range(5):
        a = math.pi * (0.85 + i * 0.075)
        x1 = cx + r * 0.82 * math.cos(a)
        y1 = cy - r * 0.5 * math.sin(a) + r * 0.1
        x2 = cx + r * 0.95 * math.cos(a)
        y2 = cy - r * 0.5 * math.sin(a) * (0.95/0.82) + r * 0.1
        draw.line([x1,y1,x2,y2], fill='white', width=max(1, size//96))
    img.save(path)

make_icon(192, '/home/claude/weightpwa/icon-192.png')
make_icon(512, '/home/claude/weightpwa/icon-512.png')
print("Icons generated")
