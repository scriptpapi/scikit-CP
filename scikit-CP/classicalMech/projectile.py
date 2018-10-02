#   File name: projectile.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/Feb/2018
#   Description: calculation and plotting of projectile motion with or without drag.

from math import cos, sin, radians, sqrt
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#   Global Variables:
#   Gravitational Acceleration (m*s^-2)
g = 9.80665
#   Sea-Level pressure (Pa)
P_o = 101.325e3
#   Sea-Level Temperature (standard day)
T_o = 288.15


class Projectile2D:
    def __init__(self, vo, ang, dt, i_num_steps, i_length=None, i_width=None, i_key=None):
        """
        :param vo: initial velocity
        :param ang: launch angle between  x and y axis
        :param dt: time step size
        :param i_num_steps: number of time steps
        :param i_length: length of the object
        :param i_width: width of the object
        :param i_key: object's key
        """
        self.vo = vo
        self.ang = ang
        self.vx = [vo*cos(radians(ang))]
        self.vy = [vo*sin(radians(ang))]
        self.dx = [0]
        self.dy = [0]
        self.dz = [0]
        self.t = [0]
        self.dt = dt
        self.num_steps = i_num_steps
        self.length = i_length
        self.width = i_width
        self.height = 0
        self.key = i_key
        self.a_g = g

    def trajectory_vacuum(self):
        """
        Calculates the trajectory of the projectile in 2D with no drag.
            - Stops calculation when object hits the ground (dy < 0).
        :return: returns x and y trajectory.
        """
        for i in range(self.num_steps):
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i]-self.a_g*self.dt)
            self.dx.append(self.dx[i] + self.vx[i]*self.dt)
            self.dy.append(self.dy[i] + self.vy[i]*self.dt)
            self.dz.append(0)
            self.t.append(self.t[i] + self.dt)
            if self.dy[i] < 0:
                break
        return self.dx, self.dy

    def trajectory_drag(self, rho, A, C, m, altitude=False):
        """
        Calculates the trajectory of the projectile in 2D with drag.
            - Stops calculation when object hits the ground (dy < 0).
        :param rho: air density
        :param A: frontal surface area
        :param C: Drag coefficient
        :param m: mass of object
        :param altitude: enables the effect of altitude by passing "alt"
        :return: returns x and y trajectory.
        """

        for i in range(self.num_steps):
            if altitude is True:
                P = P_o*(1-(6.5e-3*self.dy[i]/T_o))**2.5
                alt_coefficient = P/P_o
            else:
                alt_coefficient = 1
            v = sqrt(self.vx[i]**2 + self.vy[i]**2)
            a_dx = alt_coefficient*((C*rho*A*v*self.vx[i])/(2*m))
            a_dy = alt_coefficient*((C*rho*A*v*self.vy[i])/(2*m))
            self.vx.append(self.vx[i] - a_dx*self.dt)
            self.vy.append(self.vy[i] - a_dy*self.dt - self.a_g * self.dt)
            self.dx.append(self.dx[i] + self.vx[i]*self.dt)
            self.dy.append(self.dy[i] + self.vy[i]*self.dt)
            self.dz.append(0)
            self.t.append(self.t[i] + self.dt)
            if self.dy[i] < 0:
                break
        return self.dx, self.dy

    def init_params(self, vo, ang, dt, i_num_steps):
        """
        Reset the initial parameters for the projectile
        :param vo: initial velocity
        :param ang: launch angle between  x and y axis
        :param dt: time step size
        :param i_num_steps: number of iterations
        """
        self.vo = vo
        self.ang = ang
        self.dt = dt
        self.num_steps = i_num_steps

    def reset(self):
        """
        Resets the trajectory lists for the projectile.
        """
        del self.vx, self.vy, self.dx, self.dy, self.t
        self.vx = [self.vo*cos(radians(self.ang))]
        self.vy = [self.vo*sin(radians(self.ang))]
        self.dx = [0]
        self.dy = [0]
        self.t = [0]

    def output_txt(self):
        """
        Outputs trajectory data to a txt file
        """
        data = open("trajectory.txt", "a")
        data_init = "[" + str(datetime.now()) + "] Projectile Trajectory:"
        data.write(data_init)
        for i in range(self.num_steps):
            data_str = "dx: " + str(self.dx[i]) + " dy: " + str(self.dy[i])+" vx: " + str(self.vx[i])+" vy: " + \
                       str(self.vy[i]) + " t: " + str(self.t[i])
            data.write(data_str)

    def set_dimensions(self, i_length, i_width):
        """
        Sets the dimensions of the object
        :param i_length: length of the object
        :param i_width: width of the object
        """
        self.length = i_length
        self.width = i_width

    def set_init_coordinates(self, xi, yi):
        """
        Set projectiles initial coordinates.
        :param xi: initial x coordinates
        :param yi: initial y coordinates
        """
        self.dx = [xi]
        self.dy = [yi]

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

    def set_gravity(self, new_gravity):
        """
        changes the gravity acceleration value of the simulation
        :param new_gravity: new gravity acceleration value
        """
        self.a_g = new_gravity

    def plot(self):
        """
        Plots the trajectory of the projectile
        """
        plt.xlabel("x-trajectory")
        plt.ylabel("y-trajectory")
        plt.plot(self.dx, self.dy)
        plt.show()


class Projectile3D:
    def __init__(self, vo, elev, bear, dt, i_num_steps, i_length=None, i_width=None, i_height=None, key=None):
        """
        :param vo: initial velocity
        :param elev: elevation angle
        :param bear: bearing angle
        :param dt: time step size
        :param i_num_steps: number of time steps
        :param i_length: length of the object
        :param i_width: width of the object
        :param i_height: height of the object
        :param key: object's key
        """
        self.vo = vo
        self.elev = elev
        self.bear = bear
        self.vx = [vo*cos(radians(bear)*cos(radians(elev)))]
        self.vy = [vo*sin(radians(bear)*cos(radians(elev)))]
        self.vz = [vo*sin(radians(elev))]
        self.dx = [0]
        self.dy = [0]
        self.dz = [0]
        self.t = [0]
        self.dt = dt
        self.num_steps = i_num_steps
        self.length = i_length
        self.width = i_width
        self.height = i_height
        self.key = key
        self.a_g = g

    def trajectory_vacuum(self):
        """
        Calculates the trajectory of the projectile in 3D with no drag.
            - Stops calculation when object hits the ground (dz < 0).
        :return: returns x, y, and z trajectory.
        """
        for i in range(self.num_steps):
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            self.vz.append(self.vz[i]-self.a_g*self.dt)
            self.dx.append(self.dx[i] + self.vx[i]*self.dt)
            self.dy.append(self.dy[i] + self.vy[i]*self.dt)
            self.dz.append(self.dz[i] + self.vz[i]*self.dt)
            self.t.append(self.t[i] + self.dt)
            if self.dz[i] < 0:
                break
        return self.dx, self.dy, self.dz

    def trajectory_drag(self, rho, A, C, m, altitude=True):
        """
        Calculates the trajectory of the projectile in 3D with drag.
            - Stops calculation when object hits the ground (dz < 0).
        :param rho: air density
        :param A: frontal surface area
        :param C: Drag coefficient
        :param m: mass of object
        :param altitude: enables the effect of altitude by passing "alt"
        :return: returns x, y, and z trajectory.
        """
        for i in range(self.num_steps):
            if altitude is True:
                P = P_o*(1-(6.5e-3*self.dy[i]/T_o))**2.5
                alt_coefficient = P/P_o
            else:
                alt_coefficient = 1
            v = sqrt(self.vx[i]**2 + self.vy[i]**2 + self.vz[i]**2)
            a_dx = alt_coefficient*((C*rho*A*v*self.vx[i])/(2*m))
            a_dy = alt_coefficient*((C*rho*A*v*self.vy[i])/(2*m))
            a_dz = alt_coefficient*((C*rho*A*v*self.vz[i])/(2*m))
            self.vx.append(self.vx[i] - a_dx*self.dt)
            self.vy.append(self.vy[i] - a_dy*self.dt)
            self.vz.append(self.vz[i] - a_dz*self.dt - self.a_g * self.dt)
            self.dx.append(self.dx[i] + self.vx[i]*self.dt)
            self.dy.append(self.dy[i] + self.vy[i]*self.dt)
            self.dz.append(self.dz[i] + self.vz[i]*self.dt)
            self.t.append(self.t[i] + self.dt)
            if self.dz[i] < 0:
                break
        return self.dx, self.dy, self.dz

    def init_params(self, vo, elev, bear, dt, i_num_steps):
        """
        Reset the initial parameters for the projectile
        :param vo: initial velocity
        :param elev: elevation angle
        :param bear: bearing angle
        :param dt: time step size
        :param i_num_steps: number of iterations
        """
        self.vo = vo
        self.elev = elev
        self.bear = bear
        self.dt = dt
        self.num_steps = i_num_steps

    def reset(self):
        """
        Resets the lists containing trajectory for the projectile.
        """
        del self.vx, self.vy, self.vz, self.dx, self.dy, self.dz, self.t
        self.vx = [self.vo*cos(radians(self.bear)*cos(radians(self.elev)))]
        self.vy = [self.vo*sin(radians(self.bear)*cos(radians(self.elev)))]
        self.vz = [self.vo*sin(radians(self.elev))]
        self.dx = [0]
        self.dy = [0]
        self.dz = [0]

    def output_txt(self):
        """
        Outputs trajectory data to a txt file.
        """
        data = open("trajectory.txt", "a")
        data_init = "[" + str(datetime.now()) + "] Projectile Trajectory:"
        data.write(data_init)
        for i in range(self.num_steps):
            data_str = "dx: " + str(self.dx[i]) + " dy: " + str(self.dy[i]) + " dz: " + str(self.dz[i]) + \
                       " vx: " + str(self.vx[i]) + " vy: " + str(self.vx[i]) + " vz: " + str(self.vx[i]) + \
                       " t: " + str(self.t[i])
            data.write(data_str)

    def set_dimensions(self, i_length, i_width, i_height):
        """
        Set the dimensions of the projectile object.
        Sets the dimensions of the object
        :param i_length: length of the object
        :param i_width: width of the object
        :param i_height: height of the object
        """
        self.length = i_length
        self.width = i_width
        self.height = i_height

    def set_init_coordinates(self, xi, yi, zi):
        """
        Set projectiles initial coordinates.
        :param xi: initial x coordinates
        :param yi: initial y coordinates
        :param zi: initial z coordinates
        """
        self.dx = [xi]
        self.dy = [yi]
        self.dz = [zi]

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

    def set_gravity(self, new_gravity):
        """
        changes the gravity acceleration value of the simulation
        :param new_gravity: new gravity acceleration value
        """
        self.a_g = new_gravity

    def plot(self):
        """

        Plots the trajectory of the projectile in 3D
        """
        ax = plt.axes(projection='3d')
        ax.plot3D(self.dx, self.dy, self.dz, 'gray')
        plt.show()
