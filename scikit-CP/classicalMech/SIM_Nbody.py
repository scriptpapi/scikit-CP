#   File name: SIM_Nbody.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/October/2018
#   Description: numerical simulation of the n-body problem.

from classicalMech import planet
import matplotlib.pyplot as plt


PI = 3.14159


class System:
    def __init__(self, i_ms, i_planet=None):
        """
        initialize system with a start and a planet
        :param i_planet: planet object
        :param i_ms: mass of the system's star
        """
        self.ms = i_ms
        self.planets = i_planet

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
        for i in range(len(self.planets)):
            for j in range(n):
                t_vx = self.planets[i].vx[j] - ((4*PI*PI*self.planets[i].dx[j]*dt)/(self.planets[i].R_i(j)**3))
                t_vy = self.planets[i].vy[j] - ((4*PI*PI*self.planets[i].dy[j]*dt)/(self.planets[i].R_i(j)**3))
                for k in range(len(self.planets)):
                    if k == i:
                        continue
                    else:
                        m = (self.planets[k].m/self.ms)
                        dx = (self.planets[i].dx[j] - self.planets[k].dx[j])
                        dy = (self.planets[i].dy[j] - self.planets[k].dy[j])
                        t_vx -= (4*PI*PI*m*dx*dt) / self.planets[i].R_ab_i(self.planets[j])**3
                        t_vy -= (4*PI*PI*m*dy*dt) / self.planets[i].R_ab_i(self.planets[j])**3
                self.planets[i].vx.append(t_vx)
                self.planets[i].vy.append(t_vy)
                self.planets[i].dx.append(self.planets[i].dx[j] + self.planets[i].vx[j+1]*dt)
                self.planets[i].dy.append(self.planets[i].dy[j] + self.planets[i].vy[j+1]*dt)

    def plot(self):
        """
        Plot the trajectories of the planets in the solar system
        """
        for i in range(self.planets):
            plt.plot(self.planets[i].dx, self.planets[i].dy)

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
