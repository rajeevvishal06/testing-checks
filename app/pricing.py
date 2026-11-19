"""Tiny pricing module used in the Chainguard Checks lab."""


def apply_discount(price: float, percent: float) -> float:
    """Return price after a percentage discount, rounded to cents."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def total(items: list[tuple[float, int]]) -> float:
    """Sum (unit_price, quantity) pairs, rounded to cents."""
    return round(sum(price * qty for price, qty in items), 2)
