import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from MD_AtomicDistance import calculate_distance


def test_calculate_distance():
    point_a = (0.0, 0.0, 0.0)
    point_b = (3.0, 4.0, 0.0)
    assert calculate_distance(point_a, point_b) == 5.0
