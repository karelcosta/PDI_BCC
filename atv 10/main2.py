import cv2
import numpy as np

image = cv2.imread('img.jpg')

logo_width, logo_height = 512, 144
image_width, image_height = 424, 312

x1 = 50
y1 = 50
x2 = x1 + logo_width
y2 = y1 + logo_height

mask = np.zeros((image_height, image_width), dtype=np.uint8)
mask[y1:y2, x1:x2] = 255

element_to_remove = cv2.imread('logo.jpg')

element_to_remove = cv2.resize(element_to_remove, (logo_width, logo_height))

inpaint = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA, inpaintMask=element_to_remove)

cv2.imshow('Original', image)
cv2.imshow('Inpainting', inpaint)
cv2.waitKey(0)
cv2.destroyAllWindows()
