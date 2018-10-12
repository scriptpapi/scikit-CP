#   File name: planet.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/October/2018
#   Description: 2D numerical modeling of a planet as an N-body
from math import sqrt
import matplotlib.pyplot as plt
from datetime import datetime


#   constants
PI = 3.14159265359


class Planet:
    def __init__(self, i_x, i_y, i_m, i_dt, i_vx=0, i_vy=0, i_key=None):
        """
        :param i_x: initial x location
        :param i_y: initial y location
        :param i_m: mass of the planet
        :param i_dt: calculation time step size
        :param i_vx: initial velocity in the x-direction
        :param i_vy: initial velocity in the y=direction
        :param i_key: a key to be assigned to the object to make identifying it
        """
        self.dx = [i_x]
        self.dy = [i_y]
        self.m = i_m
        self.vx = [i_vx]
        self.vy = [i_vy]
        self.dt = i_dt
        self.key = i_key

    def single_orbit(self, num_steps):
        """
        Calculates the trajectory of the planet without the effect of any other celestial object.
        :param num_steps: Number of time steps
        :return: x and y trajectory lists
        """
        for i in range(num_steps):
            ri = sqrt(self.dx[i] ** 2 + self.dy[i] ** 2)
            self.vx.append(self.vx[i] - (4 * PI * PI * self.dx[i] * self.dt / ri ** 3))
            self.vy.append(self.vy[i] - (4 * PI * PI * self.dy[i] * self.dt / ri ** 3))
            self.dx.append(self.dx[i] + self.vx[i + 1] * self.dt)
            self.dy.append(self.dy[i] + self.vy[i + 1] * self.dt)
        return self.dx, self.dy

    def r_i(self, i):
        """
        :param: the number of the current time step point
        :return: distance from the center of the system
        """
        r_i = sqrt((self.dx[i]**2) + (self.dy[i]**2))
        return r_i

    def r_ab_i(self, i, planet_b):
        """
        :param i: the number of the current time step point
        :param planet_b: The other planet which the distance is being calculated from
        :return: distance of both objects from the center of the system.
        """
        x_temp = (self.dx[i] - planet_b.dx[i])**2
        y_temp = (self.dy[i] - planet_b.dy[i])**2
        r_ab_i = sqrt(x_temp + y_temp)
        return r_ab_i

    def init_params(self, i_x, i_y, i_m, i_dt, i_vx=0, i_vy=0):
        """
        Changes the parameters for the planet object
        """
        self.dx = [i_x]
        self.dy = [i_y]
        self.m = i_m
        self.vx = [i_vx]
        self.vy = [i_vy]
        self.dt = i_dt

    def set_mass(self, i_m):
        """
        :param i_m: new mass of Planet object
        """
        self.m = i_m

    def set_init_coordinates(self, x_i, y_i):
        """
        Set projectiles initial coordinates.
        :param x_i: initial x coordinates
        :param y_i: initial y coordinates
        """
        self.dx = [x_i]
        self.dy = [y_i]

    def set_key(self, i_key):
        """
        :param i_key: set a key for the projectile object to be found later.
        """
        self.key = i_key

    def get_key(self):
        """
        :return: object's key
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
