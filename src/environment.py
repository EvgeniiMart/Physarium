import numpy as np
from time import sleep

import matplotlib.pyplot as plt

class Environment:
    def __init__(self, x_len, y_len, evaporation_coeff, agents_list):
        self.matrix = np.zeros((x_len, y_len))
        self.x_len = x_len
        self.y_len = y_len
        self.evaporation_coeff = evaporation_coeff
        self.agents_list = agents_list

        self.work()

    def work(self):
        plt.ion()
        plt.show()

        step = 0
        while True:
            self.agents_update()
            self.draw()
            if step == 0:
                self.evaporate()
            step = (step + 1) % 5

    def agents_update(self):
        for unit in self.agents_list:
            unit.update(self.matrix, self.x_len, self.y_len)

    def draw(self):
        plt.clf()
        plt.imshow(self.matrix, cmap='tab20')
        plt.draw()
        plt.gcf().canvas.flush_events()

    def evaporate(self):
        tmp_func = np.vectorize(lambda x: max(0, x - x * (self.evaporation_coeff / 100)))
        self.matrix = tmp_func(self.matrix)