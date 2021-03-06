from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest


@pytest.mark.xfail(reason="Main page contain different login link #registration_link from other pages #login_link")
def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
