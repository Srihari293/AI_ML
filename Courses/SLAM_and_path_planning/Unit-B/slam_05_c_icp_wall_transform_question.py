# Subsample the scan. For each point, find a closest point on the
# wall of the arena.
# From those point pairs, estimate a transform and apply this to the pose.
# Repeat the closest point - estimate transform loop.
# This is an ICP algorithm.
# 05_c_icp_wall_transform
from lego_robot import *
from slam_b_library import filter_step, concatenate_transform
from slam_04_a_project_landmarks import write_cylinders
from slam_04_d_apply_transform_question import estimate_transform, apply_transform, correct_pose
from slam_05_a_find_wall_pairs_question import get_subsampled_points, get_corresponding_points_on_wall

# ICP: Iterate the steps of transforming the points, selecting point pairs, and
# estimating the transform. Returns the final transformation.
def get_icp_transform(world_points, iterations):

    # Iterate assignment and estimation of trafo a few times.
    # --->>> Implement your code here.
    # You may use the following strategy:
    # Start with the identity transform:
    #   overall_trafo = (1.0, 1.0, 0.0, 0.0, 0.0)
    trafo = (1.0, 1.0, 0.0, 0.0, 0.0)
    # Then loop for i in xrange(iterations):
    for i in range(iterations):
     #   Transform the world_points using the curent overall_trafo (see 05_b on how to do this). Call get_correspoinding_points_on_wall(...)
     left, right = get_corresponding_points_on_wall(world_points)
     
     #   Determine transformation which is needed "on top of" the current overall_trafo: trafo = estimate_transform(...)
     new_trafo = estimate_transform(left, right)

    #   Concatenate the found transformation with the current overall_trafo
    #     to obtain a new, 'combined' transformation. You may use the function
    #     overall_trafo = concatenate_transform(trafo, overall_trafo)
    #     to concatenate two similarities.
    #   Note also that estimate_transform may return None.
     if new_trafo:
          trafo = concatenate_transform(new_trafo, trafo)
          world_points = [apply_transform(new_trafo, point) for point in world_points]

    # Return the final transformation.
    return trafo


if __name__ == '__main__':
    # The constants we used for the filter_step.
    scanner_displacement = 30.0
    ticks_to_mm = 0.349
    robot_width = 150.0

    # The start pose we obtained miraculously.
    pose = (1850.0, 1897.0, 3.717551306747922)

    # Read the logfile which contains all scans.
    logfile = LegoLogfile()
    logfile.read(r"D:\Study\Code\Github\AI_ML\Courses\SLAM_and_path_planning\Unit-B\robot4_motors.txt")
    logfile.read(r"D:\Study\Code\Github\AI_ML\Courses\SLAM_and_path_planning\Unit-B\robot4_scan.txt")

    # Iterate over all positions.
    out_file = open("icp_wall_transform.txt", "w")
    for i in range(len(logfile.scan_data)):
        # Compute the new pose.
        pose = filter_step(pose, logfile.motor_ticks[i], ticks_to_mm, robot_width, scanner_displacement)

        # Subsample points.
        subsampled_points = get_subsampled_points(logfile.scan_data[i])
        world_points = [LegoLogfile.scanner_to_world(pose, c) for c in subsampled_points]

        # Get the transformation.
        # You may play withe the number of iterations here to see
        # the effect on the trajectory!
        trafo = get_icp_transform(world_points, iterations = 40)

        # Correct the initial position using trafo.
        pose = correct_pose(pose, trafo)

        # Write to file.
        # The pose.
        print("F %f %f %f" % pose, out_file)
        # Write the scanner points and corresponding points.
        write_cylinders(out_file, "W C", [apply_transform(trafo, p) for p in world_points])

    out_file.close()