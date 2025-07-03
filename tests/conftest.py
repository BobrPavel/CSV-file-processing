import pytest

@pytest.fixture
def test_data():
    return [{'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
            {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
            {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
            {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'}]