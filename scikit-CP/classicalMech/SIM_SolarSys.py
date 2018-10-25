#   File name: SIM_SolarSys.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/October/2018
#   Description: numerical simulation of the n-body problem of a solar system

from classicalMech.planet import Planet
import matplotlib.pyplot as plt


# Constants
PI = 3.14159


class System:
    def __init__(self, i_ms, i_planet=None):
        """
        initialize system with a start and a planet
        :param i_planet: planet object
        :param i_ms: mass of the system's star
        """
        self.ms = i_ms
        if i_planet is not None:
            self.planets = i_planet
        else:
            self.planets = list()

    def add_planet(self, i_planet):
        """
        adds a planet to the system
        :param i_planet: planet object
        """
        self.planets.append(i_planet)

    def del_planet(self, key):
        """
        deletes a planet from the system
        :param key: used to specify the planet object to be deleted
        """
        for i in range(len(self.planets)):
            if self.planets[i].get_key() == key:
                del self.planets[i]
            elif self.planets[i].get_key() != key and i <= len(self.planets):
                raise ValueError("Object not found, key may be incorrect")
            else:
                continue

    def calc_system(self, n, dt):
        """
        Calculates system orbits
        :param n: number of time steps
        :param dt: time step size
        """

        for j in range(n):
            for A in self.planets:
                i = len(A.vx) - 1
                sys_vx = A.vx[i] - (4 * PI * PI * A.dx[i] * dt) / (A.R_i(i) ** 3)
                sys_vy = A.vy[i] - (4 * PI * PI * A.dy[i] * dt) / (A.R_i(i) ** 3)
                for B in self.planets:
                    if A is B:
                        continue
                    else:
                        M = B.m / self.ms
                        dx = A.dx[i] - B.dx[i]
                        dy = A.dy[i] - B.dy[i]
                        sys_vx -= (4 * PI * PI * M * dx * dt) / (A.R_ab_i(i, B))
                        sys_vy -= (4 * PI * PI * M * dy * dt) / (A.R_ab_i(i, B))
                A.vx.append(sys_vx)
                A.vy.append(sys_vy)
                A.dx.append(A.dx[i] + A.vx[i + 1] * dt)
                A.dy.append(A.dy[i] + A.vy[i + 1] * dt)

    def plot(self):
        """
        Plot the trajectories of the planets in the solar system
        """
        for i in range(len(self.planets)):
            i_key = self.planets[i].get_key()
            plt.plot(self.planets[i].dx, self.planets[i].dy, label=str(i_key))
        plt.legend()
        plt.show()

    def output_txt(self):
        """
        outputs data to a text file
        :return: None
        """
        data = open("solar_system.txt", "a")
        for i in range(len(self.planets)):
            i_data = "Planet [" + str(i) + "]"
            for j in range(len(self.planets[i].dx)):
                i_data = "[i=" + str(j)+"]"+"[x]: " + str(self.planets[i].dx[j]) + "[y]: " + str(self.planets[i].dy[j])
            data.write(i_data)


"""
#   test case
sys = System(500000)
pl1 = Planet(4, 1, -1, 0, 2)
sys.add_planet(pl1)
pl2 = Planet(2, -2, -2, -0.8, 0.2)
sys.add_planet(pl2)
pl3 = Planet(3, -1, -1, 2, 0)
sys.add_planet(pl3)
pl4 = Planet(10, 1.5, 1.5, 1.5, -0.5)
sys.add_planet(pl4)
sys.calc_system(10000, 0.001)
sys.plot()
"""