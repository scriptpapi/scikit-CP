#   File name: SIM_Collisions.py
#   Author: Nawaf Abdullah
#   Creation Date: 31/May/2018
#   Description: Detects collision trajectories in a population of 'Projectile' objects

from classicalMech.projectile import Projectile2D, Projectile3D
from datetime import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Detector:
    def __init__(self, i_projectile_list=None):
        """
        :param i_projectile_list: List of Projectile objects passed to the collision detector
        """
        if i_projectile_list is not None:
            if i_projectile_list is list:
                self.projectiles = i_projectile_list
            else:
                raise ValueError("Value passed is not a list of Projectile types")
        """
        :param num_collisions: number of collisions detected
        collisions_coords: list of coordinates of each collision detected
        """
        self.num_collisions = 0
        self.collisions_coords = list()

    def add_projectile(self, i_projectile):
        """
        Adds a Projectile object to the detector's list.
            - User must create the object first then add it using this method
        :param i_projectile: object to be added to the detector
        """
        self.projectiles.append(i_projectile)

    def del_projectile(self, i_key):
        """
        Deletes a Projectile object from the detector
        :param i_key: the key that specifies the object to be deleted
        """
        for i in range(len(self.projectiles)):
            if self.projectiles[i].getKey() == i_key:
                del self.projectiles[i]
            elif self.projectiles[i].getKey() != i_key and i <= len(self.projectiles):
                raise ValueError("Key not found")
            else:
                continue

    def detect_points(self):
        """
        Detect collisions as points without accounting for objects volume
        :return: number of collisions, and their coordinates. False if none occur.
        """
        for i in range(len(self.projectiles)):
            for j in range(len(self.projectiles)):
                if self.projectiles[i] is self.projectiles[j]:
                    continue
                for k in range(len(self.projectiles[i].dx)):
                    if self.projectiles[i].dx[k] == self.projectiles[j].dx[k] and \
                       self.projectiles[i].dy[k] == self.projectiles[j].dy[k] and \
                       self.projectiles[i].dz[k] == self.projectiles[j].dz[k]:
                        self.num_collisions += 1
                        temp_point = [self.projectiles[i].dx[k], self.projectiles[i].dy[k], self.projectiles[i].dz[k]]
                        self.collisions_coords.append(temp_point)
        if self.num_collisions == 0 and len(self.collisions_coords) == 0:
            return False
        else:
            return self.num_collisions, self.collisions_coords

    def detect_volume(self):
        """
        Detect collisions as points with accounting for object volume
        :return: number of collisions, and their coordinates. False if none occur.
        """
        for i in range(len(self.projectiles)):
            for j in range(len(self.projectiles)):
                if self.projectiles[i] is self.projectiles[j]:
                    continue
                for k in range(len(self.projectiles[i].dx)):
                    """
                    proj: stands for Projectile object
                    i: for the first object
                    j: for the second object
                    r: stands for "Rear", i.e. the point minus the dimension/2 
                    f: stands for "Front", i.e. the point plus the dimension/2 
                    x, y, z: cartesian coordinates
                    """
                    # projectile i volume boundaries
                    proj_i_r_x = self.projectiles[i].dx[k] - 0.5 * self.projectiles[i].length
                    proj_i_f_x = self.projectiles[i].dx[k] + 0.5 * self.projectiles[i].length
                    proj_i_r_y = self.projectiles[i].dy[k] - 0.5 * self.projectiles[i].width
                    proj_i_f_y = self.projectiles[i].dy[k] + 0.5 * self.projectiles[i].width
                    proj_i_r_z = self.projectiles[i].dz[k] - 0.5 * self.projectiles[i].height
                    proj_i_f_z = self.projectiles[i].dz[k] + 0.5 * self.projectiles[i].height
                    # projectile j volume boundaries
                    proj_j_r_x = self.projectiles[j].dx[k] - 0.5 * self.projectiles[j].length
                    proj_j_f_x = self.projectiles[j].dx[k] + 0.5 * self.projectiles[j].length
                    proj_j_r_y = self.projectiles[j].dy[k] - 0.5 * self.projectiles[j].width
                    proj_j_f_y = self.projectiles[j].dy[k] + 0.5 * self.projectiles[j].width
                    proj_j_r_z = self.projectiles[j].dz[k] - 0.5 * self.projectiles[j].height
                    proj_j_f_z = self.projectiles[j].dz[k] + 0.5 * self.projectiles[j].height

                    if proj_j_r_x <= proj_i_f_x <= proj_j_f_x and \
                       proj_j_r_y <= proj_i_f_y <= proj_j_f_y and \
                       proj_j_r_z <= proj_i_f_z <= proj_j_f_z:
                        self.num_collisions += 1
                        temp_point = [self.projectiles[i].dx[k], self.projectiles[i].dy[k], self.projectiles[i].dz[k]]
                        self.collisions_coords.append(temp_point)
                    elif proj_j_r_x <= proj_i_r_x <= proj_j_f_x and \
                            proj_j_r_y <= proj_i_r_y <= proj_j_f_y and \
                            proj_j_r_z <= proj_i_r_z <= proj_j_f_z:
                        self.num_collisions += 1
                        temp_point = [self.projectiles[i].dx[k], self.projectiles[i].dy[k], self.projectiles[i].dz[k]]
                        self.collisions_coords.append(temp_point)

        if self.num_collisions == 0 and len(self.collisions_coords) == 0:
            return False
        else:
            return self.num_collisions, self.collisions_coords

    def get_num_collisions(self):
        """
        Outputs the number of collisions by detect.
        :return: number of collisions as an integer
        """
        return self.num_collisions

    def get_collisions_coordinates(self):
        """
        Outputs the location of each collision on the XYZ coordinates
        :return: a list with coordinates of each collision detected
        """
        return self.collisions_coords

    def scatter_2d(self):
        """
        Plots the location of each collisions in 2D
        """
        plt.scatter(self.collisions_coords[:][0], self.collisions_coords[:][1])
        plt.show()

    def scatter_3d(self):
        """
        Plots the location of each collisions in 3D
        """
        ax = plt.axes(projection='3d')
        ax.scatter(self.collisions_coords[:][0], self.collisions_coords[:][1], self.collisions_coords[:][2], 'gray')

    def plot_collision_course(self):
        """
        Plots all the trajectories in the simulation in 3D and highlights collision coordinates
        """
        ax = plt.axes(projection='3d')
        for i in range(len(self.projectiles)):
            ax.plot3D(self.projectiles[i].dx, self.projectiles[i].dy, self.projectiles[i].dz, 'gray')
        ax.legend()
        plt.show()

    def output_txt(self):
        """
        Outputs trajectory data to a txt file
        """
        data = open("collisions.txt", "a")
        data_init = "[" + str(datetime.now()) + "] Collisions detected [" + str(self.num_collisions) + "] :"
        data.write(data_init)
        for i in range(self.num_collisions):
            data_str = "Collision at " + str(self.collisions_coords[i])
            data.write(data_str)
