import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from perceptron import Perceptron


def main():
    options = '1. IrisPlant | 2. Wine | 3. Balance - Scale'
    print('\tPERCEPTRON CLASSIFIER')
    print('\n' + options + '\n' + '-' * len(options) + '\n')
    try:
        option = int(input('Elige el dataset: '))

        if option == 1:
            path = 'datasets/iris.data'
            df = pd.read_csv(path, header=None)
            col_label = 4
            ch_columns = [0, 1, 2, 3]
            # cl_range = int(input("Introduce el rango: "))
            cl_range = 100
        elif option == 2:
            path = 'datasets/wine.data'
            df = pd.read_csv(path, header=None)
            col_label = 0
            ch_columns = [1, 2, 3, 4, 5, 6, 7] # Podemos configurarlo para tomar más caracteristicas
            # cl_range = int(input("Introduce el rango: "))
            cl_range = 130
        elif option == 3:
            path = 'datasets/balance-scale.data'
            df = pd.read_csv(path, header=None)
            col_label = 0
            ch_columns = [1, 2, 3, 4]
            # cl_range = int(input("Introduce el rango: "))
            cl_range = 625
    except Exception as e:
        print(f'Ocurrió un error {e}, {type(e)}')

    y = df.iloc[:, col_label].values # Extraer la etiqueta de la columna
    x = df.iloc[:, ch_columns[0]:ch_columns[-1]].values # Extraer caracteristicas

    # Filtramos las categorias y caractetisticas
    x = x[0:cl_range, ch_columns[0]:ch_columns[-1]] # Dimensionalidad de los datos
    y = y[0:cl_range]

    # Mapear las etiquetas de un valor entero binario
    y = np.where(y == y[0], 1, 0)

    # Dividir la información
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state=0)

    # Elegir el tamaño de muestra
    try: 
        sample_size = int(input('Digite tamaño de muestra: '))
    except Exception as e:
        print(f'Ocurió un error {e}, {type(e)}')

    # sample_size = 3

    results_train = []
    results_test = []
    for _ in range(sample_size):
        indexes = [np.random.randint(0, len(x_train)) for _ in range(len(x_train))] 
        charac = x_train.take(indexes, axis=0) # Tomamos los valores
        label = y_train.take(indexes, axis=0) 

        # Entrenamos el modelo
        classifier = Perceptron()
        classifier.fit(charac, label)

        # Agregamos el modelo generado a una lista
        results_train.append(classifier.predict(x_train))
        results_test.append(classifier.predict(x_test))

    # Conteo de votos de entrenamiento
    final_results = []
    for i in range(len(y_train)):
        votes = {1:0, 0:0} # Diccionario de comparación
        for r in results_train:
            votes[r[i]] += 1
        final_results.append(max(zip(votes.values(), votes.keys()))[1])
    final_results = np.array(final_results)

    # print(final_results, y_train) # Comparación de los arreglos
    print(f"Presición de entrenamiento: {accuracy_score(final_results, y_train)*100:.0f}%")

    # Conteo de votos de prueba
    final_results = []
    for i in range(len(y_test)):
        votes = {1:0, 0:0}
        for r in results_test:
            votes[r[i]] += 1
        final_results.append(max(zip(votes.values(), votes.keys()))[1])
    final_results = np.array(final_results)

    # print(final_results, y_test) # Comparación de los arreglos
    print(f"Precisión de prueba: {accuracy_score(final_results, y_test)*100:.0f}%")


if __name__ == "__main__":
    main()
