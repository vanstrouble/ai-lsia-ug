import numpy as np


class CGA:
    def __init__(self, chromosome_length, population_size, generations):
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.generations = generations
        self.probability_vector = np.full(self.chromosome_length, 0.5, dtype=np.float)
        self.a = None
        self.a = None

    def compete(self):
        a = np.sum(self.a)
        b = np.sum(self.b)
        
        if a > b:
            return self.a, self.b
        else:
            return self.b, self.a

    def update_vector(self, winner, losser):
        for i in range(self.chromosome_length):
            if winner[i] != losser[i]:
                if winner[i] == 1:
                    self.probability_vector[i] += 1.0 / float(self.population_size)
                else:
                    self.probability_vector[i] -= 1.0 / float(self.population_size)

    def has_converged(self):
        for i in range(len(self.probability_vector)):
            if self.probability_vector[i] > 0.0 and self.probability_vector[i] < 1.0:
                return False
            else:
                return True

    def run(self):
        print(f'\n\tVector de probabilidad: {self.probability_vector}\n')
        g = 0
        
        for i in range(self.generations):
            self.a = np.random.randint(2, size=self.chromosome_length)
            self.b = np.random.randint(2, size=self.chromosome_length)
            
            winner, losser = self.compete()
            
            self.update_vector(winner, losser)
            
            print(f'Generacion: {i + 1}')
            g += 1
            print(f'P: {self.probability_vector}')
            
            if self.has_converged():
                break
            else:
                print('\nNo ha convergido, pero han llegado a la extinción')
        
        print(f'Solución: {self.probability_vector}, Generación: {g}')


if __name__ == '__main__':
    cga = CGA(4, 50, 1000)
    cga.run()
