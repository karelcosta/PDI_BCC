import cv2
import numpy as np
from matplotlib import pyplot as plt

def filter_noise(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    r = 50  
    mask[crow-r:crow+r, ccol-r:ccol+r] = 1

    fshift_filtered = fshift * mask

    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back

img = cv2.imread('img.png', 0) 

filtered_img = filter_noise(img)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Imagem Original')
plt.subplot(122), plt.imshow(filtered_img, cmap='gray'), plt.title('Imagem Filtrada')
plt.show()
