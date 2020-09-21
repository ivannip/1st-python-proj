import sys
import os
from PIL import Image

try:
    source_dir = sys.argv[1]
    dist_dir = sys.argv[2]
except IndexError:
    print("Not enough argument, use default")
    source_dir = "images"
    dist_dir = "images"

files = os.listdir(f"./{source_dir}")
for filename in files:
    li = str.split(filename, ".")
    if li[1] == "jpg":
        img = Image.open(f"./{source_dir}/{filename}")
        img.save(f"./{dist_dir}/{li[0]}.png", "PNG")
