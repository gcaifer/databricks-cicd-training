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

@pytest.mark.parametrize(
    "days_late, daily_fee, max_fee, expected",
    [
        (2, 1.25, 7.0, 2.50),
        (6, 1.25, 7.0, 7.0),
        (20, 1.25, 7.0, 7.0),
    ],
)
def test_late_fee_with_custom_values(
    days_late, daily_fee, max_fee, expected
):
    result = calculate_late_fee(
        days_late,
        daily_fee=daily_fee,
        max_fee=max_fee,
    )
    assert result == expected