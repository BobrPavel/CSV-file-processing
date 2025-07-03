from app.moduls.where_modul import where_func


def test_where_func(test_data):
    result = where_func(test_data, "brand=xiaomi")
    assert len(result) == 2
    assert result[1]["name"] == "poco x5 pro"

    result = where_func(test_data, "rating=0")
    assert len(result) == 0

    result = where_func(test_data, "name=galaxy s23 ultra")
    assert float(result[0]["rating"]) == 4.8
    assert result[0]["brand"] == "samsung"
