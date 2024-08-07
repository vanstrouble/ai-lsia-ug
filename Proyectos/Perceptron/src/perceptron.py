import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1) -> None:
        '''
        Instanciar un nuevo Perceptron
        :parametro learning_rate: coeficiente para ajustar la respuesta del modelo
        a los datos de entrenamiento.
        '''
        self.learning_rate = learning_rate
        # self.n_iter = None
        self._b = 0.0 # Intersección con el eje y
        self._w = None # Pesos asignados a las caracteristicas de entrada
        # Recuento de errores durante cada iteración
        self.misclassified_samples = []

    def f(self, x: np.array) -> float:
        '''
        Calcular la salidad de la neurona
        :parametro x: caracteristicas de entrada
        :retorna: la salida de la neurona
        '''
        return np.dot(x, self._w) + self._b

    def predict(self, x: np.array):
        '''
        Convertir la salida de la neurona en salidad binaria
        :parametro x: caracteristicas de entrada
        :retorna: 1 si la salida de la muestra es positiva (o cero), -1 en caso contrario
        '''
        return np.where(self.f(x) >= 0.0, 1, 0)

    def fit(self, x: np.array, y: np.array, n_iter=100):
        '''
        Método fit - Ajustar el modelo de Perceptron en los datos de entrenamiento

        :parametro x: muestras para ajustar el modelo
        :parametro y: etiquetas de las muestras de entrenamiento
        :parametro n_iter: número de iteraciones de entrenamiento
        '''
        self._b = 0.0
        self._w = np.zeros(x.shape[1])
        self.misclassified_samples = []

        for _ in range(n_iter):
            errors = 0 # Errores durante la iteración
            for xi, yi in zip(x, y):
                # Para cada muestra calcular el valor de actualización
                update = self.learning_rate * (yi - self.predict(xi))
                # Aplicarlo a la interseccion con y y al arreglo de pesos
                self._b += update
                self._w += update * xi
                errors += int(update != 0.0)
            self.misclassified_samples.append(errors)
