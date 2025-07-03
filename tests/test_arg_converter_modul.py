import pytest

from app.moduls.arg_converter_modul import arg_converter


@pytest.mark.parametrize(
    "arg, res",
    [
        ("rating>4.4", ["rating", ">", "4.4"]),
        ("rating=4.6", ["rating", "=", "4.6"]),
        ("rating<0", ["rating", "<", "0"]),
        ("brand=apple", ["brand", "=", "apple"]),
        ("brand=audi", ["brand", "=", "audi"]),
    ]
)
def test_arg_converter(arg, res):
    assert arg_converter(arg) == res
    