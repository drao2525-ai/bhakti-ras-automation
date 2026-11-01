from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import math

# Output folder
OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)

WIDTH = 1280
HEIGHT = 720

# Create devotional background
img = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# Purple-blue gradient background
for y in range(HEIGHT):
    for x in range(WIDTH):
        glow = max(0, 1 - math.sqrt(
            ((x - 640) / 900) ** 2 +
            ((y - 330) / 600) ** 2
        ))
        r = int(12 + glow * 55)
        g = int(8 + glow * 15)
        b = int(35 + glow * 100)
        draw.point((x, y), fill=(r, g, b))

# Decorative circles
for radius in range(100, 350, 40):
    draw.ellipse(
        (640-radius, 340-radius, 640+radius, 340+radius),
        outline=(100, 75, 160),
        width=2
    )

# Load fonts
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
title_font = ImageFont.truetype(font_path, 76)
small_font = ImageFont.truetype(font_path, 38)

# Add text
title = "JAI SHREE KRISHNA"
subtitle = "BHAKTI RAS"

bbox = draw.textbbox((0, 0), title, font=title_font)
draw.text(
    ((WIDTH - (bbox[2] - bbox[0])) / 2, 285),
    title,
    font=title_font,
    fill=(255, 225, 160)
)

bbox = draw.textbbox((0, 0), subtitle, font=small_font)
draw.text(
    ((WIDTH - (bbox[2] - bbox[0])) / 2, 400),
    subtitle,
    font=small_font,
    fill=(255, 255, 255)
)

# Save background image
image_path = OUTPUT / "background.png"
img.save(image_path)

# Create 15-second MP4 video
video_path = OUTPUT / "bhakti_ras_video.mp4"

subprocess.run([
    "ffmpeg", "-y",
    "-loop", "1",
    "-i", str(image_path),
    "-t", "15",
    "-r", "25",
    "-vf", "scale=1280:720,format=yuv420p",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    str(video_path)
], check=True)

print("Bhakti Ras video created successfully!")
