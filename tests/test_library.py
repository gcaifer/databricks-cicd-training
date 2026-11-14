
import pytest
from src.library import calculate_late_fee


@pytest.mark.parametrize(
    "days_late,expected",
    [
        (0, 0.0),
        (2, 1.0),
        (5, 2.5),
        (30, 10.0),
        (-1, 0.0),
    ],
)
def test_calculate_late_fee(days_late, expected):
    assert calculate_late_fee(days_late) == expected
