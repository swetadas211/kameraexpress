import pytest
from pages.productpage import product

@pytest.mark.smoke

def test_product(page):
    t1 = product(page)
    t1.add_product()