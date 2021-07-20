import cv2
import numpy as np
from PIL import Image
import pathlib
maxsize = (500, 600)
for input_img_path in pathlib.Path("input").iterdir():
    output_img_path = str(input_img_path).replace("input", "output")
    with Image.open(input_img_path) as img:
        img = cv2.imread(str(input_img_path))
        img = cv2.resize(img, (500, 600))
        Lmin = np.min(img)  # MINIMUM OF INPUT IMAGE
        Lmax = np.max(img)  # MAXIMUM OF INPUT IMAGE
        Lmean = np.mean(img)  # MEAN OF INPUT IMAGE
        LMssum = np.mean(img * img)  # MEAN SQUARE SUM OF INPUT IMAGE

        Gmin = 0  # MINIMUM OF OUTPUT IMAGE
        Gmax = 255  # MAXIMUM OF OUTPUT IMAGE
        Gmean = 110  # MEAN OF OUTPUT IMAGE

        bnum = Lmax * Lmax * (Gmean-Gmin) - LMssum * \
            (Gmax-Gmin) + Lmin * Lmin * (Gmax-Gmean)
        bden = 2*(Lmax*(Gmean-Gmin)-Lmean*(Gmax-Gmin)+Lmin*(Gmax-Gmean))
        if int(bden) == 0:
            bden = 2
        b = bnum/bden

        a = (Gmax-Gmin)/((Lmax-Lmin)*(Lmax+Lmin-2*b))

        c = Gmin - a*(Lmin-b) * (Lmin-b)

        y = a*(img-b) * (img-b) + c  # PARABOLIC FUNCTION
        y = np.array(y, dtype=np.uint8)
        cv2.imwrite(str(output_img_path), y)
        print(f"processing file {input_img_path} done...")
