import cv2
import numpy as np

# Carregando a imagem
image = cv2.imread('img.png')

height, width, channels = image.shape
print("Resolução da imagem: {} x {}".format(width, height))

# Definindo a área a ser removida (por exemplo, um retângulo)
# Você pode definir essa área interativamente ou manualmente
# Aqui, estou definindo um retângulo na parte superior esquerda da imagem
mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[100:300, 100:400] = 255

# Carregando uma imagem do próprio elemento a ser removido como referência
element_to_remove = cv2.imread('logo.png') 
height2, width2, channels2 = element_to_remove.shape
print("Resolução da imagem: {} x {}".format(width2, height2))

# Aplicando o inpainting com base na imagem de referência
inpaint = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
# inpaint = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA, inpaintMask=element_to_remove)

# Mostrando a imagem original e a imagem inpainted
cv2.imshow('Original', image)
cv2.imshow('Inpainting', inpaint)
cv2.waitKey(0)
cv2.destroyAllWindows()
