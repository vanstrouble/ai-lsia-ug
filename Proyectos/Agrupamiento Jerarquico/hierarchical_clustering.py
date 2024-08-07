from sys import maxsize

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_distances_matrix(data):
    assert type(data).__name__ == 'ndarray', 'La matriz introducida debe ser un arreglo de numpy'
    assert len(data.shape) == 2, f'La matriz debe ser de 2 dimensiones, no {data.shape[0]}'

    dist = lambda p1, p2: np.sqrt(((p1 - p2)**2).sum())
    distance_matrix = []

    for i in range(data.shape[0]): # TODO: Mejorar estructura porque va muy lento
        print(i) # Verificar las iteraciones para medir el tiempo
        temp_list = []
        for j in range(data.shape[0]):
            temp_list.append(dist(data[i], data[j]))
        distance_matrix.append(temp_list)
    
    return distance_matrix


def get_n_clusters(dendogram, clusters_num):
    assert type(dendogram).__name__ == 'list', 'El dendograma tiene que ser una lista de listas'
    assert clusters_num > 1, 'La cantidad de clusters tiene que ser igual o mayor que 2'

    clusters_list = [dendogram[0], dendogram[1]]

    i = 0
    while len(clusters_list) < clusters_num:
        skip = False
        step = 0

        if i == len(clusters_list) - 1:
            if type(clusters_list[i]).__name__ != 'list':
                skip = True
        else:
            if type(clusters_list[i]).__name__ != 'list':
                step += 1
                skip = True
            else:
                step += 2

        if not skip:
            temp_cluster = clusters_list[i]
            del clusters_list[i]
            clusters_list.insert(i, temp_cluster[1])
            clusters_list.insert(i, temp_cluster[0])

        i += step

    return clusters_list


def graph(clusters_list):
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'gray']
    values = []

    def get_values(node):
        if type(node).__name__ != 'list':
            values.append(node)
        else:
            get_values(node[0])
            get_values(node[1])

    for i, cluster in enumerate(clusters_list):
        values = []

        get_values(cluster)

        x, y = [], []
        for v in values:
            x.append(v[0])
            y.append(v[1])

        plt.scatter(x, y, c=colors[i%len(colors)])
    
    plt.show()
    return


def algorithm(dm, clusters):
    it = 1 # Contador de iteraciones

    while len(dm) > 1:
        print(it)
        # Ciclo que recorre todas las filas y columnas
        min_val = maxsize
        for i, row in enumerate(dm):
            for j, val in enumerate(row):
                if i != j: # Evita que se guarden las distancias 0.0
                    if val < min_val:
                        min_val = val
                        row_idx, col_idx = i, j

        # Generar nuevo cluster
        # * Matriz de distancias
        new_distances = [min(a, b) for a, b in zip(dm[row_idx], dm[col_idx])]
        dm.append(new_distances.copy())
        new_distances.append(0)
        for row, dis in zip(dm, new_distances):
            row.append(dis)
        
        # * Lista de clusters
        clusters.append([clusters[row_idx], clusters[col_idx]])

        # Eliminamos los clusters que se juntaron
        # * Matriz de distancias
        del dm[col_idx], dm[row_idx]
        for row in dm:
            del row[col_idx], row[row_idx]

        # * Lista de clusters
        del clusters[col_idx], clusters[row_idx]
        
        it += 1
    
    return clusters[0]


def main():
    data = pd.read_csv('test.data', sep=',', header=None).values

    # data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None).values[:, 0:2]

    clusters = [e for e in data]

    dendogram = algorithm(get_distances_matrix(data), clusters)
    k_clusters = get_n_clusters(dendogram, 3)
    graph(k_clusters)

    i = 0
    # colors = [(0, 0, 255),(0,255,0),(255,0,0)]
    colors = [(0, 255), (255,0), (255,255)]

    values = []
    def get_values(node):
        if type(node).__name__ != 'list':
            color = colors[i%len(colors)]
            for c_index, c in enumerate(color):
                node[c_index] = c
        else:
            get_values(node[0])
            get_values(node[1])

    for i, cluster in enumerate(k_clusters):
        values = []

        get_values(cluster)
        
    print()


if __name__ == '__main__':
    main()
