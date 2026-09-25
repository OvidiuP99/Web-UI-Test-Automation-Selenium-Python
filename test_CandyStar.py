
from pages.navigation_page import CandyStar


def test_bomboane(driver):
    page = CandyStar(driver)
    page.open()
    page.click_bomboane()

    assert "Bomboane" in page.get_title()

def test_sour_candy(driver):
    page = CandyStar(driver)
    page.open()
    page.click_sour_candy()

    assert "Sour Candy" in page.get_title()


def test_jeleuri(driver):
    page = CandyStar(driver)
    page.open()
    page.click_jeleuri()

    assert "Jeleuri" in page.get_title()
