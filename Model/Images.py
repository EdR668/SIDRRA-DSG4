import cv2
import numpy as np

def save_image(image):
    image = image.replace("/", "\\\\")
    img_array = np.fromfile(image, np.uint8)
    name_image = str(image).split("\\")[-1]
    image = cv2.imdecode(img_array,cv2.IMREAD_UNCHANGED)
    try:
        new_image = cv2.resize(image,(90,90), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("Images\\Image_alimentos"+"\\"+name_image, new_image)
    except cv2.error:
        print("ERORR!!!.")

    return name_image