# Plot a scan of the robot using matplotlib.
# 03_a_plot_scan
from pylab import *
from lego_robot import *

# Read the logfile which contains all scans.
logfile = LegoLogfile()
logfile.read(r"C:\Users\sriha\OneDrive\Documents\Code\AI_ML\Courses\SLAM_and_path_planning\Unit-A\robot4_scan.txt")

# Plot one scan.
plot(logfile.scan_data[10])
show()
