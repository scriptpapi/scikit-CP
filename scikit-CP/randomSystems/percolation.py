#   File: percolation.py
#   Author: Nawaf Abdullah
#   Creation Date: 16/Nov/2018
#   Description: Modeling of basic percolation
import numpy as np
from random import randint
import matplotlib.pyplot as plt


class Fluid:
    def __init__(self, i_size, i_p):
        """
        :param i_size: size of the lattice
        :param i_p: percolation probability. Must be < 1
        """
        self.size = i_size
        self.percolation = np.zeros((self.size, self.size))
        if i_p > 1:
            raise ValueError("Probability cannot be larger than 1.")
        else:
            self.p = i_p

    def percolate(self):
        """
        percolate the lattice
        :return: the 2D percolation numpy array
        """
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                r = randint(0, 100)
                if r <= self.p*100:
                    self.percolation[i][j] = 1
        return self.percolation

    def recursive_cluster_detector(self, x, y):
        """
        :param x: i position in the loop
        :param y: j position in the loop
        :return: N/A
        """
        try:
            if self.percolation[x + 1][y] == 1:
                self.percolation[x][y] = 5
                self.percolation[x+1][y] = 5
                self.recursive_cluster_detector(x + 1, y)
        except IndexError:
            pass
        try:
            if self.percolation[x - 1][y] == 1:
                self.percolation[x][y] = 5
                self.percolation[x - 1][y] = 5
                self.recursive_cluster_detector(x - 1, y)
        except IndexError:
            pass
        try:
            if self.percolation[x][y + 1] == 1:
                self.percolation[x][y] = 5
                self.percolation[x][y + 1] = 5
                self.recursive_cluster_detector(x, y + 1)
        except IndexError:
            pass
        try:
            if self.percolation[x][y - 1] == 1:
                self.percolation[x][y] = 5
                self.percolation[x][y - 1] = 5
                self.recursive_cluster_detector(x, y - 1)
        except IndexError:
            pass

    def detect_clusters(self):
        """
        detects clusters that resulting from percolation
        :return: the 2D percolation numpy array with the clusters highlighted having a value of 5
        """
        # Detect clusters loop
        for i in range(self.size):
            for j in range(self.size):
                if self.percolation[i][j] == 1:
                    self.recursive_cluster_detector(i, j)
                else:
                    continue

    def plot(self):
        plt.pcolormesh(self.percolation)
        plt.grid(True)
        plt.colorbar()
        plt.show()


"""
# Example use case
example = Fluid(50, 0.6)
example.percolate()
example.detect_clusters()
example.plot()
"""