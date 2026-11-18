#!/usr/bin/env python3
"""Generate the BTE book cover PNG. Requires Pillow and macOS Songti/PingFang fonts."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2400
PAPER = (246, 241, 231)
INK = (31, 31, 31)
MUTED = (122, 111, 96)
ACCENT = (181, 55, 42)

SONGTI = "/System/Library/Fonts/Supplemental/Songti.ttc"
PINGFANG = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"


def font(path, size, index):
    return ImageFont.truetype(path, size, index=index)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Rules
    d.rectangle([0, 0, W, 18], fill=ACCENT)
    d.rectangle([0, H - 18, W, H], fill=ACCENT)

    # English kicker
    kicker = font(PINGFANG, 40, 3)
    d.text((140, 220), "THE BTE BOOK", font=kicker, fill=MUTED)
    d.text((140, 300), "OF AI ERA", font=kicker, fill=MUTED)

    # Title
    title = font(SONGTI, 150, 6)
    d.text((140, 520), "AI 时代的", font=title, fill=INK)
    d.text((140, 710), "技术销售", font=title, fill=INK)
    d.text((140, 900), "白皮书", font=title, fill=ACCENT)

    # Rule
    d.rectangle([140, 1120, 1460, 1128], fill=ACCENT)

    # Subtitle
    sub = font(PINGFANG, 52, 3)
    d.text((140, 1200), "把技术变成生意，把承诺变成可交付的合同。", font=sub, fill=INK)

    # Tagline
    tag = font(PINGFANG, 42, 3)
    d.text((140, 1420), "BTE 设计承诺 · SA 证明承诺 · TAM 兑现承诺", font=tag, fill=MUTED)

    # Author and version
    author = font(PINGFANG, 48, 3)
    d.text((140, 2160), "Allen Galler", font=author, fill=INK)
    ver = font(PINGFANG, 34, 3)
    d.text((140, 2240), "v1.0 初稿 · 2026-11-03 · CC BY-NC-SA 4.0", font=ver, fill=MUTED)

    # Seal
    d.rectangle([1380, 300, 1500, 420], fill=ACCENT)
    seal = font(SONGTI, 64, 6)
    bbox = d.textbbox((0, 0), "承", font=seal)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((1380 + (120 - tw) / 2, 300 + (120 - th) / 2 - 8), "承", font=seal, fill=PAPER)

    img.save("cover.png", "PNG")
    print("wrote cover.png")


if __name__ == "__main__":
    main()