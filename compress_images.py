from pathlib import Path
from PIL import Image

SRC = Path("raw_images")      
DST = Path("web/assets")
DST.mkdir(parents=True, exist_ok=True)

MAX_SIDE = 640     
QUALITY = 85       
CLASSES = ["plastik", "kagit", "cam", "metal"]
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}

for c in CLASSES:
    (DST/c).mkdir(parents=True, exist_ok=True)
    for p in (SRC/c).rglob("*"):
        if p.suffix.lower() in EXTS:
            im = Image.open(p)
            if im.mode != "RGB":
                im = im.convert("RGB")

            w, h = im.size
            scale = min(MAX_SIDE / max(w, h), 1.0)
            if scale < 1.0:
                im = im.resize((int(w*scale), int(h*scale)), Image.LANCZOS)

            out = (DST/c/f"{p.stem}.jpg")
            im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            print("✅ saved", out)
