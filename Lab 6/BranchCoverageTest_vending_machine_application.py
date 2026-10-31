import pytest
from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"

def test_item_missing_from_stock_is_sold_out():
    assert select_item("cola", {}, 200) == "sold_out"

def test_sold_out_zero_stock():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"

def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 149) == "insufficient"

def test_exact_credit_ok():
    assert select_item("chips", {"chips": 1}, 100) == "ok"

def test_more_credit_ok():
    assert select_item("candy", {"candy": 1}, 500) == "ok"

def test_negative_amount():
    with pytest.raises(ValueError):
        make_change(-1)

def test_zero_change():
    assert make_change(0) == []

def test_all_coin_types():
    assert make_change(190) == [100, 50, 25, 10, 5]

def test_repeated_coins():
    assert make_change(200) == [100, 100]

def test_small_amount_skips_big_coins():
    assert make_change(5) == [5]

def test_leftover_returns_none():
    assert make_change(3) is None

def test_leftover_after_coins_returns_none():
    assert make_change(52) is None

def test_purchase_invalid():
    assert purchase("water", {}, 100) == ("invalid", [])

def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])

def test_purchase_insufficient():
    assert purchase("cola", {"cola": 1}, 50) == ("insufficient", [])

def test_purchase_no_exact_change():
    stock = {"cola": 2}
    assert purchase("cola", stock, 153) == ("no_exact_change", [])
    assert stock["cola"] == 2

def test_purchase_dispensed_with_change():
    stock = {"candy": 2}
    assert purchase("candy", stock, 100) == ("dispensed", [25])
    assert stock["candy"] == 1

def test_purchase_dispensed_exact_payment():
    stock = {"chips": 1}
    assert purchase("chips", stock, 100) == ("dispensed", [])
    assert stock["chips"] == 0
