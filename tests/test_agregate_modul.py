from moduls.agregate_modul import aggregate_func


def test_where_func(test_data):
    assert aggregate_func(test_data, "rating=min") == [{"min": 4.4}]
    assert aggregate_func(test_data, "price=avg") == [{"avg": 674}]
    assert aggregate_func(test_data, "rating=max") == [{"max": 4.9}]
    assert aggregate_func(test_data, "price=max") == [{"max": 1199}]

