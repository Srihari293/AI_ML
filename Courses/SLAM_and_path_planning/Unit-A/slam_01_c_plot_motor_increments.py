# Plot the increments of the left and right motor.
# 01_c_plot_motor_increments.py
from pylab import *
from lego_robot import LegoLogfile

if __name__ == '__main__':

    logfile = LegoLogfile()
    logfile.read(r"C:\Users\sriha\OneDrive\Documents\Code\AI_ML\Courses\SLAM_and_path_planning\Unit-A\robot4_motors.txt")
    plot(logfile.motor_ticks)
    show()

# We can see that the left motor bemcomes slower and right motor becomes faster