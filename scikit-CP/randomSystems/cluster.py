#   File: cluster.py
#   Author: Nawaf Abdullah
#   Creation Date: 13/Nov/2018
#   Description: Modeling of cluster growth
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import time


class Cluster:
    def __init__(self, i_size):
        """
        :param i_size: size of the space the cluster is allowed to grow within
        """
        self.size = i_size
        self.growth = None
        self.z_swtich = False
        self.particles_2d = list()
        self.particles_3d = list()

    def add_seed_particle(self, x, y, z=None):
        """
        Adds a seed particle on a user specified point in 2D or 3D
        :param x: x-location
        :param y: y-location
        :param z: z-location
        """
        if z is None:
            self.growth = np.zeros((self.size, self.size))
            self.particles_2d.append((x, y))
            self.growth[x][y] = 1
        else:
            self.growth = np.zeros((self.size, self.size, self.size))
            self.particles_3d.append((x, y, z))
            self.growth[x][y][z] = 1

    def Eden_growth(self, num_iter):
        """
        Grow the cluster using Eden cluster growth model.
        :param num_iter: number of iterations
        :return: growth numpy array
        """
        if self.growth.shape == (self.size, self.size, self.size):
            self.z_swtich = True
            self.__Eden_growth_3d(num_iter)
        elif self.growth.shape == (self.size, self.size):
            self.z_swtich = False
            self.__Eden_growth_2d(num_iter)
        return self.growth

    def __Eden_growth_2d(self, N):
        """
        Grow the cluster using Eden cluster growth model in 2D
        :param N: number of iterations
        """
        grounded = list()
        for n in range(N):
            for coord in self.particles_2d:
                if coord in grounded:
                    continue
                x = coord[0]
                y = coord[1]
                try:
                    # Make sure index stays within range
                    index_check_right = self.growth[x + 1][y]
                    index_check_left  = self.growth[x - 1][y]
                    index_check_up    = self.growth[x][y + 1]
                    index_check_down  = self.growth[x][y - 1]
                except IndexError:
                    continue
                r = randint(0, 100)
                if r <= 25:
                    if self.growth[x+1][y] != 1:
                        self.growth[x+1][y] = 1
                        self.particles_2d.append((x+1, y))
                    else:
                        if self.growth[x-1][y] != 1:
                            self.growth[x-1][y] = 1
                            self.particles_2d.append((x-1, y))
                        elif self.growth[x][y+1] != 1:
                            self.growth[x][y+1] = 1
                            self.particles_2d.append((x, y+1))
                        elif self.growth[x][y-1] != 1:
                            self.growth[x][y-1] = 1
                            self.particles_2d.append((x, y-1))
                        else:
                            grounded.append((x, y))
                # --------------- -x --------------- #
                elif 25 < r <= 50:
                    if self.growth[x-1][y] != 1:
                        self.growth[x-1][y] = 1
                        self.particles_2d.append((x - 1, y))
                    else:
                        if self.growth[x+1][y] != 1:
                            self.growth[x+1][y] = 1
                            self.particles_2d.append((x + 1, y))
                        elif self.growth[x][y+1] != 1:
                            self.growth[x][y+1] = 1
                            self.particles_2d.append((x, y + 1))
                        elif self.growth[x][y-1] != 1:
                            self.growth[x][y-1] = 1
                            self.particles_2d.append((x, y - 1))
                        else:
                            grounded.append((x, y))
                # --------------- +y --------------- #
                elif 50 < r <= 75:
                    if self.growth[x][y+1] != 1:
                        self.growth[x][y+1] = 1
                        self.particles_2d.append((x, y + 1))
                    else:
                        if self.growth[x-1][y] != 1:
                            self.growth[x-1][y] = 1
                            self.particles_2d.append((x - 1, y))
                        elif self.growth[x+1][y] != 1:
                            self.growth[x+1][y] = 1
                            self.particles_2d.append((x + 1, y))
                        elif self.growth[x][y-1] != 1:
                            self.growth[x][y-1] = 1
                            self.particles_2d.append((x, y - 1))
                        else:
                            grounded.append((x, y))
                # --------------- -y --------------- #
                else:
                    if self.growth[x][y-1] != 1:
                        self.growth[x][y-1] = 1
                        self.particles_2d.append((x, y - 1))
                    else:
                        if self.growth[x-1][y] != 1:
                            self.growth[x-1][y] = 1
                            self.particles_2d.append((x - 1, y))
                        elif self.growth[x+1][y] != 1:
                            self.growth[x+1][y] = 1
                            self.particles_2d.append((x + 1, y))
                        elif self.growth[x][y+1] != 1:
                            self.growth[x][y+1] = 1
                            self.particles_2d.append((x, y + 1))
                        else:
                            grounded.append((x, y))

    def __Eden_growth_3d(self, N):
        """
        Grow the cluster using Eden cluster growth model in 3D
        :param N:number of iterations
        :return:
        """
        time.sleep(5)

    def DLA_growth(self, num_iter, num_steps):
        """
        Grows the cluster using diffusion limited aggregation
        :param num_iter: number of iterations
        :param num_steps: number of steps for the randomly moving particle
        :return: growth numpy array
        """
        if self.growth.shape == (self.size, self.size, self.size):
            self.z_swtich = True
            self.__DLA_growth_3d(num_iter, num_steps)
        elif self.growth.shape == (self.size, self.size):
            self.z_swtich = False
            self.__DLA_growth_2d(num_iter, num_steps)
        return self.growth

    def __DLA_growth_2d(self, N, N_steps):
        """
        Grows the cluster using diffusion limited aggregation in 2D
        :param N: number of iterations.
        :param N_steps: the number of steps of the random moving particle
        """
        for n in range(N):
            # Select random coordinates for the randomly moving particle
            x = randint(0, self.size)
            y = randint(0, self.size)

            # Make sure the location is still within bounds
            try:
                index_check = self.growth[x+1][y] + self.growth[x-1][y] + self.growth[x][y+1] + self.growth[x][y-1]
            except IndexError:
                continue

            # Check if there isn't a particle already assigned to the randomly chosen location
            if self.growth[x][y] == 1:
                continue
            else:
                self.growth[x][y] = 1

            # start random walk for the particle
            for i in range(N_steps):

                # Make sure the location is still within bounds
                try:
                    index_check = self.growth[x + 1][y] + self.growth[x - 1][y] + self.growth[x][y + 1] + \
                                  self.growth[x][y - 1]
                except IndexError:
                    continue

                r = randint(0, 100)
                if r <= 25:
                    # Move to the right
                    if self.growth[x+1][y] != 1:
                        self.growth[x+1][y] = self.growth[x][y]
                        self.growth[x][y] = 0
                        x = x + 1
                        y = y
                    else:
                        self.particles_2d.append((x, y))
                        break
                elif 25 < r <= 50:
                    # Move to the left
                    if self.growth[x-1][y] != 1:
                        self.growth[x-1][y] = self.growth[x][y]
                        self.growth[x][y] = 0
                        x = x - 1
                        y = y
                    else:
                        self.particles_2d.append((x, y))
                        break
                elif 50 < r <= 75:
                    # Move up
                    if self.growth[x][y+1] != 1:
                        self.growth[x][y+1] = self.growth[x][y]
                        self.growth[x][y] = 0
                        x = x
                        y = y + 1
                    else:
                        self.particles_2d.append((x, y))
                        break
                else:
                    # Move down
                    if self.growth[x][y-1] != 1:
                        self.growth[x][y-1] = self.growth[x][y]
                        self.growth[x][y] = 0
                        x = x
                        y = y - 1
                    else:
                        self.particles_2d.append((x, y))
                        break

    def __DLA_growth_3d(self, N, N_steps):
        """
        Grows the cluster using diffusion limited aggregation in 2D
        :param N: number of iterations.
        :param N_steps: the number of steps of the random moving particle
        """
        time.sleep(5)
        pass

    def plot(self):
        plt.pcolormesh(self.growth)
        plt.grid(True)
        plt.show()


"""
# Example use case
bob = Cluster(100)
bob.add_seed_particle(50, 50)
bob.DLA_growth(1000, 10000)
bob.plot()
"""