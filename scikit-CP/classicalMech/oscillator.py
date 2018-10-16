#   File name: oscillator.py
#   Author: Nawaf Abdullah
#   Creation Date: 8/June/2018
#   Description: numerical modeling of oscillatory motion

from math import sin
import matplotlib.pyplot as plt
from datetime import datetime


#   Global Variables:
#   Gravitational Acceleration (m*s^-2)
g = 9.80665
#   Pi
PI = 3.14159265359


class Oscillator:
    def __init__(self, i_length, i_ang=0, i_o=0, i_E=0, i_time=0, i_damp=0, f_d=0, ohm_d=0):
        """

        :param i_ang: Initial position (radians)
        :param i_o: Initial velocity (radians/s)
        :param i_E: Initial energy (Joules)
        :param i_length: Length of the oscillator (meters)
        :param i_time: Initial time point
        :param i_damp: Initial dampening parameter
        :param f_d: Driving force (newtons)
        :param ohm_d: Externally imposed frequency
        """

        self.length = i_length
        self.Si = i_ang
        self.S = [i_ang]

        self.Oi = i_o
        self.O = [i_o]

        self.Ei = i_E
        self.E = [i_E]

        self.ti = i_time
        self.t = [self.ti]

        self.q = i_damp
        self.Fd = f_d
        self.Od = ohm_d

    def init_param(self, l, i_ang, i_o, i_E):
        """
        Reset oscillator basic parameters
        :return: None
        """
        self.length = l
        self.Si = i_ang
        self.Oi = i_o
        self.Ei = i_E

    def set_dampening(self, q):
        """
        Sets dampening
        :param q: dampening factor
        """
        self.q = q

    def set_driving_force(self, f_d):
        """
        Sets driving Force
        :param f_d: driving force
        """
        self.Fd = f_d

    def set_external_freq(self, ohm_d):
        """
        Sets externally imposed frequency
        :param ohm_d: External frequency
        """
        self.Od = ohm_d

    def oscillate(self, num_steps, dt):
        """
        Calculates the position and the velocity of the oscillator
        :param num_steps: number of time steps
        :param dt: size of each time step
        :return: position (self.S) velocity (self.O)
        """
        for i in range(num_steps):
            o_f = self.O[i]-dt*((g/self.length)*sin(self.S[i]+self.q*self.O[i]+self.Fd*sin(self.Od*self.t[i])))
            self.O.append(o_f)
            self.S.append(self.S[i]+self.O[i+1]*dt)
            self.E.append(self.E[i]+0.5*(self.O[i+1]**2+self.S[i+1]**2))
            self.t.append(self.t[i]+dt)
            if self.S[i+1] > PI:
                self.S[i+1] = self.S[i+1] - PI
            elif self.S[i+1] < -PI:
                self.S[i+1] = self.S[i+1] + PI
        return self.O, self.S

    def get_position(self):
        """
        :return: position trajectory list
        """
        return self.O

    def get_velocity(self):
        """
        :return: velocity as a function of time in a list
        """
        return self.S

    def get_energy(self):
        """
        :return: Energy as a function of time in a list
        """
        return self.E

    def reset(self, i_length, i_ang, i_o, i_time):
        """
        Re-assign the oscillator's values and empty the lists storing position, speed, and time data
        :return:
        """
        del self.S
        del self.O
        del self.t
        self.length = i_length
        self.Si = i_ang
        self.Oi = i_o
        self.ti = i_time
        self.S = [self.Si]
        self.O = [self.Oi]
        self.t = [self.ti]

    def output_txt(self):
        """
        outputs data to a text file
        :return: None
        """
        data = open("oscillator.txt", "a")
        data_init = "[" + str(datetime.now()) + "] oscillator data:"
        data.write(data_init)
        data_init = "Length = " + str(self.length)
        data.write(data_init)
        for i in range(len(self.S)):
            data_str = "Position (rad): " + str(self.S[i]) + " Velocity (rad/s): " + str(self.O[i]) + " Energy (J): " \
                       + str(self.E[i])
            data.write(data_str)

    def plot(self):
        """
        Plots position and velocity against time
        :return: None
        """
        plt.xlabel("Time (s)")
        plt.plot(self.t, self.S, label='Position (radians)')
        plt.plot(self.t, self.O, label='Velocity (radians/s)')
        plt.legend(loc='best')
        plt.show()

    def poincare_plot(self):
        """
        Plots velocity vs position
        :return: None
        """
        plt.ylabel("Velocity (radians/s)")
        plt.xlabel("Position (radians)")
        plt.plot(self.S, self.O)
        plt.show()


