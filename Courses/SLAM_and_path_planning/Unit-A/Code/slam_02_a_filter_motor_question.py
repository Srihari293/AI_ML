from math import sin, cos, pi
import matplotlib.pyplot as plt
from lego_robot import LegoLogfile

def filter_step(old_pose, motor_ticks, ticks_to_mm, robot_width):
    """
    Computes the new robot pose based on the old pose, motor ticks, and physical characteristics.

    Args:
        old_pose (tuple): The old pose (x, y, heading) of the robot.
        motor_ticks (tuple): The motor ticks for the left and right wheels.
        ticks_to_mm (float): Conversion factor from ticks to millimeters.
        robot_width (float): Width of the robot (wheel gauge) in millimeters.

    Returns:
        tuple: The new pose (x, y, heading) of the robot.
    """
    # Find out if there is a turn at all.
    if motor_ticks[0] == motor_ticks[1]:
        # Driving straight.
        theta = old_pose[2]
        x = old_pose[0] + motor_ticks[0] * ticks_to_mm * cos(theta)
        y = old_pose[1] + motor_ticks[0] * ticks_to_mm * sin(theta)

        return (x, y, theta)

    else:
        # Turns
        alpha = (motor_ticks[1] - motor_ticks[0]) * ticks_to_mm / robot_width
        R = motor_ticks[0] * ticks_to_mm / alpha

        theta = old_pose[2]
        c_x = old_pose[0] - (R + robot_width / 2) * sin(theta)
        c_y = old_pose[1] + (R + robot_width / 2) * cos(theta)

        theta = (theta + alpha) % (2 * pi)
        x = c_x + (R + robot_width / 2) * sin(theta)
        y = c_y - (R + robot_width / 2) * cos(theta)

        return (x, y, theta)

if __name__ == '__main__':
    # ticks to mm factor.
    ticks_to_mm = 0.349

    # Wheel width/gauge (mm)
    robot_width = 150.0

    # Read data.
    logfile = LegoLogfile()
    logfile.read(r"Data\robot4_motors.txt")

    # Start at origin (0,0), looking along x-axis (alpha = 0).
    pose = (0.0, 0.0, 0.0)

    # Loop over all motor tick records and generate a filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
        filtered.append(pose)

    # Draw the result.
    x_values = [p[0] for p in filtered]
    y_values = [p[1] for p in filtered]

    plt.plot(x_values, y_values, 'bo')
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)')
    plt.title('Filtered Robot Pose')
    plt.grid(True)
    plt.show()