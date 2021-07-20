import cv2
import numpy as np
from PIL import Image
import pathlib
maxsize = (500, 600)
for input_img_path in pathlib.Path("input").iterdir():
    output_img_path = str(input_img_path).replace("input", "output")
    with Image.open(input_img_path) as im:
        im = cv2.imread(str(input_img_path))
        im = cv2.resize(im, (500, 600))
        image_bw = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=5)
        im = clahe.apply(image_bw) + 0
        cv2.imwrite(str(output_img_path), im)
        print(f"processing file {input_img_path} done...")
