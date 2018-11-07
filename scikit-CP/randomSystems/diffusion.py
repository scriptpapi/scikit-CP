#   File: diffusion.py
#   Author: Nawaf Abdullah
#   Creation Date: 5/Nov/2018
#   Description: Modeling of diffusion in 2D and 3D
import numpy as np
from math import floor
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Substance:
    def __init__(self, i_size):
        """
        :param i_size: size of diffusion volume
        """
        self.dim = i_size
        self.D_2d = np.zeros((self.dim, self.dim))
        self.D_3d = np.zeros((self.dim, self.dim, self.dim))
        self.z_switch = False

    def add_mass_2d(self, mass_size):
        """
        Adds mass to be diffused to the 2D grid
        :param mass_size: size of the mass in the grid
        """
        m = int(mass_size/2)
        center = int(self.dim/2)
        self.D_2d[center - m: center + m, center - m: center + m] = 1
        self.z_switch = False

    def add_mass_3d(self, mass_size):
        """
        Adds mass to be diffused to the 3D grid
        :param mass_size: size of the mass in the grid
        """
        m = int(mass_size / 2)
        center = int(self.dim / 2)
        self.D_3d[center - m: center + m, center - m: center + m, center - m: center + m] = 1

    def diffuse_2d(self, num_iter):
        """
        Begin diffusion in 2D
        :param num_iter: number of the time steps
        :return: numpy array of final position of the masses
        """
        D = self.D_2d
        for i in range(len(num_iter)):
            for j in range(len(num_iter)):
                if D[i][j] == 1:
                    D[i][j] = 0
                    r = random.randint(0, 100)
                    # --------------- +x --------------- #
                    if r <= 25:
                        if D[i+1][j] == 1:
                            continue
                        else:
                            D[i+1][j] = 1
                    # --------------- -x --------------- #
                    elif 25 < r <= 50:
                        if D[i-1][j] == 1:
                            continue
                        else:
                            D[i-1][j] = 1
                    # --------------- +y --------------- #
                    elif 50 < r <= 75:
                        if D[i][j+1] == 1:
                            continue
                        else:
                            D[i][j+1] = 1
                    # --------------- -y --------------- #
                    else:
                        if D[i][j-1] == 1:
                            continue
                        else:
                            D[i][j-1] = 1
        self.z_switch = False
        self.D_2d = D
        return self.D_2d

    def diffuse_3d(self, num_iter):
        """
        Begin diffusion in 2D
        :param num_iter: number of the time steps
        :return: numpy array of final position of the masses
        """
        D = self.D_3d
        for i in range(len(num_iter)):
            for j in range(len(num_iter)):
                for k in range(len(num_iter)):
                    if D[i][j][k] == 1:
                        D[i][j][k] = 0
                        r = random.randint(0, 100)
                        if r <= 16.66:
                            if D[i+1][j][k] == 1:
                                continue
                            else:
                                D[i+1][j][k] = 1
                        elif 16.66 < r <= 33.32:
                            if D[i-1][j][k] == 1:
                                continue
                            else:
                                D[i-1][j][k] = 1
                        elif 33.32 < r <= 49.98:
                            if D[i][j+1][k] == 1:
                                continue
                            else:
                                D[i][j+1][k] = 1
                        elif 49.98 < r <= 66.64:
                            if D[i][j-1][k] == 1:
                                continue
                            else:
                                D[i][j-1][k] = 1
                        elif 66.64 < r <= 83.33:
                            if D[i][j][k+1] == 1:
                                continue
                            else:
                                D[i][j][k+1] = 1
                        else:
                            if D[i][j][k-1] == 1:
                                continue
                            else:
                                D[i][j][k-1] = 1
        self.D_3d = D
        self.z_switch = True
        return self.D_3d

    def plot(self):
        if self.z_switch is True:
            ax = plt.axes(projection='3d')
            ax.plot3D(self.D_3d, 'gray')
            plt.show()
        else:
            plt.plot(self.D_2d)
            plt.show()
