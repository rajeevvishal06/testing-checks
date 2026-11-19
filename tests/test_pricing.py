import pytest

from app.pricing import apply_discount, total


def test_apply_discount():
    assert apply_discount(100, 15) == 85.0


def test_apply_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 150)


def test_total():
    assert total([(2.50, 4), (1.25, 2)]) == 12.5
