import cv2

from hierarchical_clustering import algorithm, get_distances_matrix, get_n_clusters


def main():
    img = cv2.imread('beach2.jpg')

    data = img.reshape((-1,3))
    clusters = [e for e in data]

    dendogram = algorithm(get_distances_matrix(data), clusters)
    k_clusters = get_n_clusters(dendogram, 4)

    # Convierte todos los pixeles de cada cluster en el mismo color
    i = 0
    colors = [(0, 0, 255),(0,255,0),(255,0,0)]
    values = []
    def edit_values(node):
        if type(node).__name__ != 'list':
            color = colors[i%len(colors)]
            for c_index, c in enumerate(color):
                node[c_index] = c
        else:
            edit_values(node[0])
            edit_values(node[1])

    for i, cluster in enumerate(k_clusters):
        values = []
        edit_values(cluster)

    # Reajusta la forma del arreglo a una matriz de mxn y guarda dicha matriz como imagen
    result_image = data.reshape((img.shape))
    cv2.imwrite('beach2.jpg', result_image)


if __name__ == '__main__':
    main()
