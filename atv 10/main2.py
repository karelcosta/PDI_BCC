import cv2
import numpy as np

# Carregando a imagem
image = cv2.imread('img.jpg')

# Definindo a área a ser removida (por exemplo, um retângulo)
# Aqui, estou ajustando o retângulo com base nas dimensões da imagem e da logo
logo_width, logo_height = 512, 144
image_width, image_height = 424, 312

# Calculando as coordenadas do retângulo na imagem
x1 = 50
y1 = 50
x2 = x1 + logo_width
y2 = y1 + logo_height

# Criando a máscara para o retângulo a ser removido
mask = np.zeros((image_height, image_width), dtype=np.uint8)
mask[y1:y2, x1:x2] = 255

# Carregando uma imagem do próprio elemento a ser removido como referência
element_to_remove = cv2.imread('logo.jpg')

# Redimensionando a imagem de referência para as dimensões da imagem
element_to_remove = cv2.resize(element_to_remove, (logo_width, logo_height))

# Aplicando o inpainting com base na imagem de referência
inpaint = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA, inpaintMask=element_to_remove)

# Mostrando a imagem original e a imagem inpainted
cv2.imshow('Original', image)
cv2.imshow('Inpainting', inpaint)
cv2.waitKey(0)
cv2.destroyAllWindows()
