#   File name: SIM_Nbody.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/October/2018
#   Description: numerical simulation of the n-body problem for multiple n-bodies.


class System:
    def __init__(self, i_ms, i_body_list=None):
        """
        :param i_body_list: list containing the n-body objects in the system.
        :param i_ms: mass of the system's star
        """
        if i_body_list is not None:
            if i_body_list is list:
                self.n_bodies = i_body_list
            else:
                raise ValueError("Value passed is not a list of Projectile types")
        self.ms = i_ms

    def add_body(self, i_body):
        """
        Adds an n-body object to the system's list.
            - User must create the object first then add it using this method
        :param i_body: object to be added to the system
        """
        self.n_bodies.append(i_body)

    def del_projectile(self, i_key):
        """
        Deletes an n-body object from the system
        :param i_key: the key that specifies the object to be deleted
        """
        for i in range(len(self.n_bodies)):
            if self.n_bodies[i].getKey() == i_key:
                del self.n_bodies[i]
            elif self.n_bodies[i].getKey() != i_key and i <= len(self.n_bodies):
                raise ValueError("Key not found")
            else:
                continue

    def calc_system(self):
        """
        Calculate the trajectory of n-bodies in the system.
        """