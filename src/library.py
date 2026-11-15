def calculate_late_fee(
    days_late: int,
    daily_fee: float = 0.50,
    max_fee: float = 10.0,
) -> float:
    if days_late <= 0:
        return 0.0

    return min(days_late * daily_fee, max_fee)
