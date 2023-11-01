# Plot the ticks from the left and right motor.
# 01_a_plot_motor_ticks.py
from pylab import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read all ticks of left and right motor.
    # Format:
    # M | timestamp[in ms] | pos-left[in ticks] | * | * | * | pos-right[in ticks] | ...

    with open(r"Data\robot4_motors.txt", "r") as f:
        left_list = []
        right_list = []
        for line in f:
            fields = line.split()
            left_list.append(int(fields[2]))
            right_list.append(int(fields[6]))

    # Create a figure
    plt.figure(figsize=(10, 6))

    # Plot left and right motor ticks
    plt.plot(left_list, label='Left Motor Ticks', linestyle='-', marker='o', markersize=3, color='blue')
    plt.plot(right_list, label='Right Motor Ticks', linestyle='-', marker='o', markersize=3, color='red')

    # Add labels and title
    plt.xlabel('Timestamp (in ms)')
    plt.ylabel('Ticks')
    plt.title('Motor Ticks - Left vs Right')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()