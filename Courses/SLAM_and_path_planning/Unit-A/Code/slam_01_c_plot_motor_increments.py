# Plot the increments of the left and right motor.
# 01_c_plot_motor_increments.py
from lego_robot import LegoLogfile
from pylab import *
if __name__ == '__main__':

    logfile = LegoLogfile()
    logfile.read(r"Unit-A\Data\robot4_motors.txt")
    plot(logfile.motor_ticks)
    show()