#   File name: SIM_RandomWalkers.py
#   Author: Nawaf Abdullah
#   Creation Date: 5/Nov/2018
#   Description: Simulates a population of random walkers

from randomSystems.walker import Walker
import matplotlib.pyplot as plt


class RWPopulation:
    def __init__(self, i_walkers_list=None):
        """
        :param i_walkers_list: Initial list of random walkers
        """
        if i_walkers_list is not None:
            if isinstance(i_walkers_list, list):
                self.walkers = i_walkers_list
            else:
                raise ValueError("Value passed is not a list of Walker types")

    def add_walker(self, i_walker):
        """
        Adds a walker to the list of walker population
        :param i_walker: walker instance
        """
        if isinstance(i_walker, Walker):
            self.walkers.append(i_walker)
        else:
            raise TypeError("Value passed is not a Walker type")

    def del_walker(self, key):
        """
        Deletes a walker instance which is identified within the list using a key
        :param key: key used to identify walker instance to be deleted
        """
        for i in range(len(self.walkers)):
            if self.walkers[i].key == key:
                del self.walkers[i]
            elif self.walkers[i].key != key and i <= len(self.walkers):
                raise ValueError("Key not found")
            else:
                continue

    def detect_intersection_2d(self):
        """
        detects when two walkers cross paths in 2d
        :return: points of crossing in a list Format: (x, y, step number). False if no intersections occur.
        """
        intersect = []
        for W_A in self.walkers:
            for W_B in self.walkers:
                if W_A is W_B:
                    continue
                for i in range(1, len(W_A.x)):
                    if W_A.x[i] == W_B.x[i] and \
                       W_A.y[i] == W_B.y[i]:
                        intersect.append((W_A.x[i], W_A.y[i], i))
        if intersect == []:
            return False
        else:
            return intersect

    def detect_intersection_3d(self):
        """
        detects when two walkers cross paths in 3d
        :return: points of crossing in a list Format: (x, y, z, step number). False if no intersections occur.
        """
        intersect = []
        for W_A in self.walkers:
            for W_B in self.walkers:
                if W_A is W_B:
                    continue
                for i in range(len(W_A.x)):
                    if W_A.x[i] == W_B.x[i] and \
                       W_A.y[i] == W_B.y[i] and \
                       W_A.z[i] == W_B.z[i]:
                        intersect.append((W_A.x[i], W_A.y[i], W_A.z[i], i))
        if intersect == []:
            return False
        else:
            return intersect

    def plot_2d(self):
        """
        Plot the paths of walkers in 2d
        """
        for i in range(len(self.walkers)):
            i_key = self.walkers[i].key
            plt.plot(self.walkers[i].x, self.walkers[i].y, label=str(i_key))
        plt.legend()
        plt.show()

    def plot_3d(self):
        """
        Plot the paths of walkers in 3d
        """
        ax = plt.axes(projection='3d')
        for i in range(len(self.walkers)):
            i_key = self.walkers[i].key
            ax.plot3D(self.walkers[i].x, self.walkers[i].y, self.walkers[i].z, label=str(i_key))
        ax.legend()
        plt.show()


"""
# use case example
bob = Walker(5, 3, 2)
bob.saw_3d(1000, True)
jon = Walker()
jon.saw_3d(1000, True)
walkers_gang = [bob, jon]
sys = RWPopulation(walkers_gang)
print(sys.detect_intersection_3d())
sys.plot_3d()
"""