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

def re_size(image, name_image):
    image  = cv2.imread(image, cv2.IMREAD_UNCHANGED)

    height = int(image.shape[1]*75/100) 
    width = int(image.shape[0]*75/100)
    dsize = (height,width)
    new_image = cv2.resize(image, dsize)
    print(new_image.shape[0], new_image.shape[1])
    cv2.imwrite("Images\\Fondos"+"\\"+name_image, new_image)