from colav_unsafe_set_gen.objects import DynamicObstacleWithMetrics
from typing import List


def unionise_indices_of_interest(
    I1: List[DynamicObstacleWithMetrics],
    I2: List[DynamicObstacleWithMetrics],
    I3: List[DynamicObstacleWithMetrics],
) -> List[DynamicObstacleWithMetrics]:
    """Unionise the indices of interest."""
    return list(set(I1 + I2 + I3))
