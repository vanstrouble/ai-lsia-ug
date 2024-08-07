import numpy as np
import cv2

from Genetic_Algorithm import GA

img = cv2.imread('circles.png')
img_orig = img.copy()
# Convertir imagen a escala de grises
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Suavizar la imagen
img = cv2.medianBlur(img, 3)

# Detectamos los bordes
edge = cv2.Canny(img, 50, 50)

# Encontramos los contornos
contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
pixels = np.concatenate(contours)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Configuramos los parametros para el GA
# GA = GA(pixels.shape[0], , 0, pixels.shape[0]-1, 3)
# 2**n >= pixels.shape[0]-1