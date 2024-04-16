import cv2
import numpy as np

image = cv2.imread('img.png')

height, width, channels = image.shape
print("Resolução da imagem: {} x {}".format(width, height))

mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[100:300, 100:400] = 255

element_to_remove = cv2.imread('logo.png') 
height2, width2, channels2 = element_to_remove.shape
print("Resolução da imagem: {} x {}".format(width2, height2))

inpaint = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

cv2.imshow('Original', image)
cv2.imshow('Inpainting', inpaint)
cv2.waitKey(0)
cv2.destroyAllWindows()
