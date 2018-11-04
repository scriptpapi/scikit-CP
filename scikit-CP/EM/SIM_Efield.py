#   File name: SIM_Efield.py
#   Author: Nawaf Abdullah
#   Creation Date: 25/October/2018
#   Description: Numerical simulation script of electric field and potential
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class EField:
    def __init__(self, i_size):
        """
        :param i_size: size of the grid for field simulation. I.e. the number of available points for writing
        """
        self.dim = i_size
        self.V_2d = np.zeros((self.dim, self.dim))
        self.V_3d = np.zeros((self.dim, self.dim, self.dim))
        self.V1 = 1
        self.V2 = -1
        self.z_switch = False
        self.E_x = []
        self.E_y = []
        self.E_z = []

    def set_capacitor_lines(self, L1, L2, V1, V2, D, W1=1, W2=1):
        """
        Set the properties of the capacitor lines
        :param L1: Width of capacitor 1
        :param L2: Width of capacitor 2
        :param V1: Voltage of capacitor 1
        :param V2: Voltage of capacitor 2
        :param D: Distance between the two capacitors
        """
        self.V1 = V1
        self.V2 = V2
        center = int((self.dim/2))
        if L1 > self.dim:
            raise ValueError("Width of the capacitor cannot be larger than the grid size")
        elif L2 > self.dim:
            raise ValueError("Width of the capacitor cannot be larger than the grid size")
        else:
            L1 = int(L1 / 2)
            L2 = int(L2 / 2)
        pos1 = int((self.dim / 2) + (D / 2))
        pos2 = int((self.dim / 2) - (D / 2))
        # print(pos1, ":", pos1 + W1)
        # print(pos2, ":", pos2 + W2)
        # print(center-L1, ":", center+L1)
        # print(center-L2, ":", center+L2)
        self.V_2d[pos1:pos1 + W1, center - L1:center + L1] = self.V1
        self.V_2d[pos2:pos2 + W2, center - L2:center + L2] = self.V2

    def set_capacitor_plates(self, L1, L2, V1, V2, D, W1=1, W2=1):
        """
        sets the location and the voltage of the capacitor plates in the 3d space.
        :param L1: Side length of capacitor plate 1
        :param L2: Side length of capacitor plate 2
        :param V1: Voltage of capacitor 1
        :param V2: Voltage of capacitor 2
        :param D: Distance between the two capacitors
        """
        self.z_switch = True
        self.V1 = V1
        self.V2 = V2
        center = int((self.dim / 2))
        if L1 > self.dim:
            raise ValueError("Width of the capacitor cannot be larger than the grid size")
        elif L2 > self.dim:
            raise ValueError("Width of the capacitor cannot be larger than the grid size")
        else:
            L1 = int(L1 / 2)
            L2 = int(L2 / 2)
        pos1 = int((self.dim / 2) + (D / 2))
        pos2 = int((self.dim / 2) - (D / 2))
        self.V_3d[pos1:pos1 + W1, center - L1:center + L1, center - L1:center+L1] = self.V1
        self.V_3d[pos2:pos2 + W2, center - L2:center + L2, center - L2:center+L2] = self.V2

    def surface_potential(self, num_iter):
        """
        calculates the electric field potential on surface
        :param num_iter: number of iterations of the numerical method calculations
        """
        V = self.V_2d
        for n in range(num_iter):
            for i in range(1, self.dim-1):
                for j in range(1, self.dim-1):
                    if V[i][j] == self.V1 or V[i][j] == self.V2:
                        continue
                    else:
                        V[i][j] = (V[i + 1][j] + V[i - 1][j] +
                                   V[i][j + 1] + V[i][j - 1]) * (1 / 4)
        self.V_2d = V
        return self.V_2d

    def space_potential(self, num_iter):
        """
        calculates the electric field potential in space
        :param num_iter: number of iterations of the numerical method calculations
        """
        V = self.V_3d
        for n in range(num_iter):
            for i in range(1, self.dim-1):
                for j in range(1, self.dim-1):
                    for k in range(1, self.dim-1):
                        if V[i][j][k] == self.V1 or V[i][j][k] == self.V2:
                            continue
                        else:
                            V[i][j][k] = (V[i + 1][j][k] + V[i - 1][j][k] +
                                          V[i][j + 1][k] + V[i][j - 1][k] +
                                          V[i][j][k + 1] + V[i][j][k - 1]) * (1/6)
        self.V_3d = V
        return self.V_3d

    def surface_field(self, ds):
        """
        calculates the electric field on surface
        :param ds: step size for Electric field calculation
        """
        V = self.V_2d
        for i in range(1, self.dim-1):
            for j in range(1, self.dim-1):
                if V[i][j] == self.V1 or V[i][j] == self.V2:
                    continue
                else:
                    self.E_x.append(-1 * ((V[i - 1][j] - V[i + 1][j]) * (1 / (2 * ds))))
                    self.E_y.append(-1 * ((V[i][j - 1] - V[i][j + 1]) * (1 / (2 * ds))))
        return [self.E_x, self.E_y]

    def space_field(self, ds):
        """
        calculates the electric field in space
        :param ds: step size for Electric field calculation
        """
        V = self.V_3d
        for i in range(1, self.dim-1):
            for j in range(1, self.dim-1):
                for k in range(1, self.dim-1):
                    if V[i][j][k] == self.V1 or V[i][j][k] == self.V2:
                        continue
                    else:
                        self.E_x.append(-1 * ((V[i - 1][j][k] - V[i + 1][j][k]) * (1 / (2 * ds))))
                        self.E_y.append(-1 * ((V[i][j - 1][k] - V[i][j + 1][k]) * (1 / (2 * ds))))
                        self.E_z.append(-1 * ((V[i][j][k - 1] - V[i][j][k + 1]) * (1 / (2 * ds))))
        return [self.E_x, self.E_y, self.E_z]

    def plot_potential_surface(self):
        """
        Plots the potential field.
        """
        fig, ax0 = plt.subplots(nrows=1)
        im = ax0.pcolormesh(self.V_2d)
        fig.colorbar(im, ax=ax0)
        plt.show()

    def plot_potential_3d_slice(self, slice_pos):
        """
        Plots a slice of the 3d potential matrix
        :param slice_pos: slice position between two plates
        """
        fig, ax0 = plt.subplots(nrows=1)
        im = ax0.pcolormesh(self.V_3d[slice_pos, :, :])
        fig.colorbar(im, ax=ax0)
        plt.show()

    def plot_field(self):
        """
        plots the electric field lines.
        """
        if self.z_switch is True:
            ax = plt.axes(projection='3d')
            ax.plot3D(self.E_x, self.E_y, self.E_z, 'gray')
            plt.show()
        else:
            plt.plot(self.E_x, self.E_y)
            plt.show()