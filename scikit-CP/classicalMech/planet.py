#   File name: planet.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/October/2018
#   Description: 2D numerical modeling of a planet as an N-body
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


#   constants
PI = 3.14159265359


class Planet:
    def __init__(self, i_m, x_i, y_i, vx_i=0, vy_i=0, i_key=None):
        """
        :param i_m: mass
        :param x_i: initial x position
        :param y_i:  initial y position
        :param vx_i: initial x velocity
        :param vy_i: initial y velocity
        :param i_key: key string that can be used identify the object in a list or a tree
        """
        self.m = i_m
        self.dx = [x_i]
        self.dy = [y_i]
        self.vx = [vx_i]
        self.vy = [vy_i]
        self.key = i_key

    def orbit(self, n, dt):
        """
        Calculates planet's orbit around a star without the influence of other planets
        :param n: number of time steps
        :param dt: time step size
        :return: x and y trajectory lists
        """
        for i in range(n):
            ri = self.R_i(i)
            self.vx.append(self.vx[i] - (4 * PI * PI * self.dx[i] * dt / ri ** 3))
            self.vy.append(self.vy[i] - (4 * PI * PI * self.dy[i] * dt / ri ** 3))
            self.dx.append(self.dx[i] + self.vx[i + 1] * dt)
            self.dy.append(self.dy[i] + self.vy[i + 1] * dt)
        return self.dx, self.dy

    def r_i(self, i):
        """
        :param i: time step point
        :return: position vector
        """
        return np.array([self.dx[i], self.dy[i]])

    def R_i(self, i):
        """
        :param i: time step point
        :return: magnitude of position vector at i
        """
        r_i = sqrt((self.dx[i] ** 2) + (self.dy[i] ** 2))
        return r_i

    def r_ab_i(self, i, planet_b):
        """
        :param i: time step point
        :param planet_b: The other planet which the distance is being calculated from
        :return: The position vector from planet a to planet b
        """
        a = np.array([self.dx[i], self.dy[i]])
        b = np.array([planet_b.dx[i], planet_b.dy[i]])
        ab = a - b
        return ab

    def R_ab_i(self, i, planet_b):
        """
        :param i: the number of the current time step point
        :param planet_b: The other planet which the distance is being calculated from
        :return: distance of both objects from the center of the system.
        """
        x_temp = (self.dx[i] - planet_b.dx[i]) ** 2
        y_temp = (self.dy[i] - planet_b.dy[i]) ** 2
        r_ab_i = sqrt(x_temp + y_temp)
        return r_ab_i

    def set_params(self, i_m=None, x_i=None, y_i=None, vx_i=None, vy_i=None):
        """
        Set all physical parameters of the planet object
        """
        if i_m is not None:
            self.m = i_m
        if x_i is not None:
            self.dx = [x_i]
        if y_i is not None:
            self.dy = [y_i]
        if vx_i is not None:
            self.vx = [vx_i]
        if vy_i is not None:
            self.vy = [vy_i]

    def set_key(self, i_key):
        """
        :param i_key: set key identifying object. must be a string.
        """
        if i_key is isinstance(i_key, str):
            self.key = i_key
        else:
            raise ValueError("Key value must be a string.")

    def get_key(self):
        """
        :return: returns planets key
        """
        return self.key

    def reset(self):
        """
        Resets the trajectory lists for Planet object
        """
        del self.dx, self.dy, self.vx, self.vy
        self.dx = [0]
        self.dy = [0]
        self.vx = [0]
        self.vy = [0]

    def output_txt(self):
        """
        Outputs trajectory data to a txt file
        """
        data = open("trajectory.txt", "a")
        data_init = "[" + str(datetime.now()) + "] Projectile Trajectory:"
        data.write(data_init)
        for i in range(len(self.dx)):
            data_str = "dx: " + str(self.dx[i]) + " dy: " + str(self.dy[i]) + \
                       " vx: " + str(self.vx[i]) + " vy: " + str(self.vy[i])
            data.write(data_str)

    def plot(self):
        """
        plots the trajectory of the planet
        """
        plt.xlabel("x-Position")
        plt.xlabel("y-Position")
        plt.plot(self.dx, self.dy)
        plt.show()
