#   File name: projectile.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/Feb/2018
#   Description: calculation and plotting of projectile motion with or without drag.

from math import cos, sin, radians, sqrt
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import count

#   Global Variables:
#   Gravitational Acceleration (m*s^-2)
g = 9.80665
#   Sea-Level pressure (Pa)
P_o = 101.325e3
#   Sea-Level Temperature (standard day)
T_o = 288.15


class Projectile2D:
    _ids = count(0)

    def __init__(self, vo, ang, i_length=None, i_width=None, i_key=None):
        """
        :param vo: initial velocity
        :param ang: launch angle between  x and y axis
        :param i_length: length of the object
        :param i_width: width of the object
        :param i_key: object's key
        """
        self.id = next(self._ids)
        self.vo = vo
        self.ang = ang
        self.vx = [vo*cos(radians(ang))]
        self.vy = [vo*sin(radians(ang))]
        self.dx = [0]
        self.dy = [0]
        self.dz = [0]
        self.t = [0]
        self.length = i_length
        self.width = i_width
        self.height = 0
        if i_key is None:
            self.key = "projectile " + str(self.id)
        else:
            self.key = i_key
        self.a_g = g

    def trajectory_vacuum(self, num_steps, dt):
        """
        Calculates the trajectory of the projectile in 2D with no drag.
            - Stops calculation when object hits the ground (dy < 0).
        :param num_steps: number of time steps.
        :param dt: time step size
        :return: returns x and y trajectory.
        """
        for i in range(num_steps):
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i] - self.a_g*dt)
            self.dx.append(self.dx[i] + self.vx[i]*dt)
            self.dy.append(self.dy[i] + self.vy[i]*dt)
            self.dz.append(0)
            self.t.append(self.t[i] + dt)
            if self.dy[i] < 0:
                break
        return self.dx, self.dy

    def trajectory_drag(self, num_steps, dt, rho, A, C, m, altitude=False):
        """
        Calculates the trajectory of the projectile in 2D with drag.
            - Stops calculation when object hits the ground (dy < 0).
        :param num_steps: number of time steps.
        :param dt: time step size
        :param rho: air density
        :param A: frontal surface area
        :param C: Drag coefficient
        :param m: mass of object
        :param altitude: enables the effect of altitude by passing "alt"
        :return: returns x and y trajectory.
        """

        for i in range(num_steps):
            if altitude is True:
                P = P_o*(1-(6.5e-3*self.dy[i]/T_o))**2.5
                alt_coefficient = P/P_o
            else:
                alt_coefficient = 1
            v = sqrt(self.vx[i]**2 + self.vy[i]**2)
            a_dx = alt_coefficient*((C*rho*A*v*self.vx[i])/(2*m))
            a_dy = alt_coefficient*((C*rho*A*v*self.vy[i])/(2*m))
            self.vx.append(self.vx[i] - a_dx*dt)
            self.vy.append(self.vy[i] - a_dy*dt - self.a_g*dt)
            self.dx.append(self.dx[i] + self.vx[i]*dt)
            self.dy.append(self.dy[i] + self.vy[i]*dt)
            self.dz.append(0)
            self.t.append(self.t[i] + dt)
            if self.dy[i] < 0:
                break
        return self.dx, self.dy

    def init_params(self, vo=None, ang=None, i_length=None, i_width=None):
        """
        Resets any of the parameters for the projectile object
        """
        if vo is not None:
            self.vo = vo
        if ang is not None:
            self.ang = ang
        if i_length is not None:
            self.length = i_length
        if i_width is not None:
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
        for i in range(len(self.dx)):
            data_str = "dx: " + str(self.dx[i]) + " dy: " + str(self.dy[i])+" vx: " + str(self.vx[i])+" vy: " + \
                       str(self.vy[i]) + " t: " + str(self.t[i])
            data.write(data_str)

    def plot(self):
        """
        Plots the trajectory of the projectile
        """
        plt.xlabel("x-trajectory")
        plt.ylabel("y-trajectory")
        plt.plot(self.dx, self.dy)
        plt.show()


class Projectile3D:
    _ids = count(0)

    def __init__(self, vo, elev, bear, i_length=None, i_width=None, i_height=None, i_key=None):
        """
        :param vo: initial velocity
        :param elev: elevation angle
        :param bear: bearing angle
        :param i_length: length of the object
        :param i_width: width of the object
        :param i_height: height of the object
        :param key: object's key
        """
        self.id = next(self._ids)
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
        self.length = i_length
        self.width = i_width
        self.height = i_height
        if i_key is None:
            self.key = "projectile " + str(self.id)
        else:
            self.key = i_key
        self.a_g = g

    def trajectory_vacuum(self, num_steps, dt):
        """
        :param num_steps: number of time steps
        :param dt: time step size
        Calculates the trajectory of the projectile in 3D with no drag.
            - Stops calculation when object hits the ground (dz < 0).
        :return: returns x, y, and z trajectory.
        """
        for i in range(num_steps):
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            self.vz.append(self.vz[i]-self.a_g*dt)
            self.dx.append(self.dx[i] + self.vx[i]*dt)
            self.dy.append(self.dy[i] + self.vy[i]*dt)
            self.dz.append(self.dz[i] + self.vz[i]*dt)
            self.t.append(self.t[i] + dt)
            if self.dz[i] < 0:
                break
        return self.dx, self.dy, self.dz

    def trajectory_drag(self, num_steps, dt, rho, A, C, m, altitude=True):
        """
        Calculates the trajectory of the projectile in 3D with drag.
            - Stops calculation when object hits the ground (dz < 0).
        :param num_steps: number of time steps
        :param dt: time step size
        :param rho: air density
        :param A: frontal surface area
        :param C: Drag coefficient
        :param m: mass of object
        :param altitude: enables the effect of altitude by passing "alt"
        :return: returns x, y, and z trajectory.
        """
        for i in range(num_steps):
            if altitude is True:
                P = P_o*(1-(6.5e-3*self.dy[i]/T_o))**2.5
                alt_coefficient = P/P_o
            else:
                alt_coefficient = 1
            v = sqrt(self.vx[i]**2 + self.vy[i]**2 + self.vz[i]**2)
            a_dx = alt_coefficient*((C*rho*A*v*self.vx[i])/(2*m))
            a_dy = alt_coefficient*((C*rho*A*v*self.vy[i])/(2*m))
            a_dz = alt_coefficient*((C*rho*A*v*self.vz[i])/(2*m))
            self.vx.append(self.vx[i] - a_dx*dt)
            self.vy.append(self.vy[i] - a_dy*dt)
            self.vz.append(self.vz[i] - a_dz*dt - self.a_g*dt)
            self.dx.append(self.dx[i] + self.vx[i]*dt)
            self.dy.append(self.dy[i] + self.vy[i]*dt)
            self.dz.append(self.dz[i] + self.vz[i]*dt)
            self.t.append(self.t[i] + dt)
            if self.dz[i] < 0:
                break
        return self.dx, self.dy, self.dz

    def init_params(self, vo=None, elev=None, bear=None, i_length=None, i_width=None, i_height=None):
        """
        Reset any of the parameters for the projectile
        """
        if vo is not None:
            self.vo = vo
        if elev is not None:
            self.elev = elev
        if bear is not None:
            self.bear = bear
        if i_length is not None:
            self.length = i_length
        if i_width is not None:
            self.width = i_width
        if i_height is not None:
            self.height = i_height

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
        data = open("trajectory_3d.txt", "a")
        data_init = "[" + str(datetime.now()) + "] Projectile Trajectory:"
        data.write(data_init)
        for i in range(len(self.dx)):
            data_str = "dx: " + str(self.dx[i]) + " dy: " + str(self.dy[i]) + " dz: " + str(self.dz[i]) + \
                       " vx: " + str(self.vx[i]) + " vy: " + str(self.vx[i]) + " vz: " + str(self.vx[i]) + \
                       " t: " + str(self.t[i])
            data.write(data_str)

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