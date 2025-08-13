import math
import time


def calculate_distance(coord_a, coord_b):
    """Return Euclidean distance between two 3D coordinates."""
    return math.sqrt(
        (coord_a[0] - coord_b[0]) ** 2 +
        (coord_a[1] - coord_b[1]) ** 2 +
        (coord_a[2] - coord_b[2]) ** 2
    )


if __name__ == "__main__":
    start_time = time.time()

    # Configuration
    xyz_file = "MD_trajectory.xyz"
    atom_a_index = 4024
    atom_b_index = 331

    coordinates = []
    step_number = 0

    with open(xyz_file, "r") as coordinate_file:
        for line_index, line in enumerate(coordinate_file):
            # Determine position within current frame
            if line_index == 0:
                atom_number = int(line.strip())
                coordinates.append([])

            pos_in_block = line_index - step_number * (atom_number + 2)

            if 1 < pos_in_block < (atom_number + 2):
                parts = line.split()
                atom = [parts[0], float(parts[1]), float(parts[2]), float(parts[3])]
                coordinates[step_number].append(atom)

            elif pos_in_block == (atom_number + 2):
                coordinates.append([])
                step_number += 1

    if len(coordinates[step_number]) == atom_number:
        step_number += 1

    print("Number of steps =", step_number)
    print(f"Distance between {coordinates[0][atom_a_index][0]} "
          f"and {coordinates[0][atom_b_index][0]}")
    print(f"Distance between indices {atom_a_index} and {atom_b_index}")

    distances = []
    for i in range(step_number):
        coord_a = tuple(coordinates[i][atom_a_index][1:])
        coord_b = tuple(coordinates[i][atom_b_index][1:])
        distances.append(calculate_distance(coord_a, coord_b))

    elapsed_time = time.time() - start_time
    print('Elapsed time = %.3f seconds' % elapsed_time)
