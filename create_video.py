from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("output", exist_ok=True)

W, H = 1280, 720
image = Image.new("RGB", (W, H), (25, 20, 65))
draw = ImageDraw.Draw(image)

# Simple devotional background
for y in range(H):
    shade = int(25 + 35 * y / H)
    draw.line((0, y, W, y), fill=(shade, 20, 85))

title = "जय श्री कृष्ण"
subtitle = "राधे राधे 🙏"
footer = "Bhakti Ras"

try:
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    title_font = ImageFont.truetype(font_path, 76)
    sub_font = ImageFont.truetype(font_path, 42)
    small_font = ImageFont.truetype(font_path, 28)
except OSError:
    title_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

def centered_text(text, y, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    x = (W - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)

centered_text(title, 230, title_font, "white")
centered_text(subtitle, 340, sub_font, "#FFD700")
centered_text(footer, 620, small_font, "white")

image.save("output/bhakti_ras_test.png")
print("Bhakti Ras test image created successfully!")
