import numpy as np
import cv2

from KMeans import KMeans

K = 2
img_path = 'image.jpg'

# Cargar la imagen y copiarla para manipularla
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pixel_values = img.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

kmeans = KMeans(X=pixel_values, num_clusters=K)
means, labels = kmeans.fit()

# Aplicar etiquetas  a los centroides para segmentar
means = np.uint8(means)

segmented_data = means[labels]

# Reestructurar el arreglo
result_image = segmented_data.reshape(img.shape)

result_image = cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('result-img.jpg', result_image)
