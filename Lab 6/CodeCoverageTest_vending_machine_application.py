import pytest
from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_select_ok():
    assert select_item("chips", {"chips": 3}, 100) == "ok"


def test_no_change_needed():
    assert make_change(0) == []


def test_make_change_valid():
    assert make_change(185) == [100, 50, 25, 10]


def test_make_change_negative():
    with pytest.raises(ValueError):
        make_change(-5)


def test_make_change_not_possible():
    assert make_change(3) is None


def test_purchase_failure_status():
    assert purchase("water", {}, 100) == ("invalid", [])


def test_purchase_no_exact_change():
    assert purchase("cola", {"cola": 2}, 153) == ("no_exact_change", [])


def test_purchase_dispensed():
    stock = {"candy": 2}
    assert purchase("candy", stock, 100) == ("dispensed", [25])
    assert stock["candy"] == 1
