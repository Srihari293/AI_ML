# Print the increments of the left and right motor.
# Now using the LegoLogfile class.
# 01_b_print_motor_increments.py
from lego_robot import LegoLogfile  
if __name__ == '__main__':
    logfile = LegoLogfile()
    logfile.read(r"C:\Users\sriha\OneDrive\Documents\Code\AI_ML\Courses\SLAM_and_path_planning\Unit-A\robot4_motors.txt")
    for i in range(20):
        print(logfile.motor_ticks[i])