import pytest
from pages.loginpage import login

@pytest.mark.smoke

def test_login(page):
    l1 = login(page)
    l1.login_click()