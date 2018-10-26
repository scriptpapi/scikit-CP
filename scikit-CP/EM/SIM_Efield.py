#   File name: SIM_Efield.py
#   Author: Nawaf Abdullah
#   Creation Date: 25/October/2018
#   Description: Numerical simulation script of electric field and potential
import numpy as np


class EField:
    def __init__(self, i_size):
        """
        :param i_size: size of the grid for field simulation. I.e. the number of available points for writing
        """
        self.dim = i_size
        self.V_2d = np.zeros((self.dim, self.dim))
        self.V_3d = np.zeros((self.dim, self.dim, self.dim))

    def surface_potential(self, num_iter):
        """
        calculates the electric field potential on surface
        :param num_iter: number of iterations of the numerical method calculations
        """
        V = self.V_2d
        for n in range(num_iter):
            for i in range(self.dim):
                for j in range(self.dim):
                    V[i][j] = (V[i+1][j] + V[i-1][j] +
                               V[i][j+1] + V[i][j-1]) * (1/4)
        self.V_2d = V
        return self.V_2d

    def surface_field(self, num_iter):
        """
        calculates the electric field on surface
        :param num_iter: number of iterations of the numerical method calculations
        """


    def space_potential(self, num_iter):
        """
        calculates the electric field potential in space
        :param num_iter: number of iterations of the numerical method calculations
        """
        V = self.V_3d
        for n in range(num_iter):
            for i in range(self.dim):
                for j in range(self.dim):
                    for k in range(self.dim):
                        V[i][j][k] = V[i+1][j][k] + V[i-1][j][k] +\
                                     V[i][j+1][k] + V[i][j-1][k] +\
                                     V[i][j][k+1] + V[i][j][k-1]
        self.V_3d = V
        return self.V_3d

    def space_field(self, num_iter):
        """
        calculates the electric field in space
        :param num_iter: number of iterations of the numerical method calculations
        """

    def set_capacitor_lines(self):
        """
        sets the location and the voltage of the capacitor lines on 2d surface.
        """

    def set_capacitor_plates(self):
        """
        sets the location and the voltage of the capacitor plates in the 3d space.
        """

    def plot_potential(self):
        """
        Plots the potential field.
        """

    def plot_efield(self):
        """
        plots the electric field lines.
        """