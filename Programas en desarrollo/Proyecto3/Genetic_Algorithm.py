from sys import maxsize

import numpy as np
import matplotlib.pyplot as plt


class GA():
    def __init__(self, pop_size, str_size, lower_bound, upper_bound, n):
        assert str_size % 2 == 0, 'str_size debe ser par'
        assert str_size % n == 0, 'el residuo de dividir str_size entre n debe ser 0'

        # Inicializacion
        self.l_bound = lower_bound
        self.u_bound = upper_bound
        self.n = n # Numero de dimensiones
        self.lx = int(str_size/n) # Tamaño de cada gen
        self.population = np.random.randint(2, size=(pop_size, str_size))
        self.best = maxsize

    def run(self, iter_num=100):
        history = np.empty(shape=iter_num, dtype=np.int16)
        for it in range(iter_num):
            # Selección
            total = 0
            norm_pop = []
            for chromosome in self.population:
                val = self.fitness_func(chromosome)
                total += val
                norm_pop.append(val)

            norm_pop = tuple(val/total for val in norm_pop)

            selection = []
            for _ in range(self.population.shape[0]):
                rand_num = np.random.rand()
                summation = 0
                for i, val in enumerate(norm_pop):
                    if rand_num >= summation and rand_num < summation + val:
                        selection.append(self.population[i])
                        break
                    else:
                        summation += val
            selection = np.array(selection, dtype=np.int16)

            # Cruza
            for i in range(0, selection.shape[0], 2):
                c_point = np.random.randint(1, selection.shape[1])
                temp_arr = selection[i][c_point::].copy()
                selection[i][c_point::] = selection[i+1][c_point::]
                selection[i+1][c_point::] = temp_arr

            # Mutación
            for chromosome in selection:
                idx = np.random.randint(selection.shape[1])
                chromosome[idx] = 0 if chromosome[idx] == 1 else 1

            # Evaluación y remplazo
            for i in range(self.population.shape[0]):
                if self.fitness_func(selection[i]) < self.fitness_func(self.population[i]):
                    self.population[i] = selection[i].copy()

            # Generar historial para ver al mejor
            for i in range(self.population.shape[0]):
                fit_val = self.fitness_func(self.population[i])
                if fit_val < self.best:
                    self.best = fit_val
            history[it] = self.best

        # Historial
        plt.plot(np.arange(1,iter_num+1), history)
        plt.show()

        return history

    def fitness_func(self, chromosome):
        return sum(self.decode(chromosome[i*self.lx:(i*self.lx)+self.lx])**2 for i in range(self.n))

    def decode(self, gene):
        return self.l_bound + ((self.u_bound-self.l_bound)/(2**self.lx-1)
                )*sum(gene[self.lx-1-j]*(2**j) for j in range(self.lx))


if __name__ == '__main__':
    GA(10, 8, -5.21, 5.21, 2).run()
    # print(GA(10, 8, -5.21, 5.21, 2).decode(np.array([0,1,1,1])))
