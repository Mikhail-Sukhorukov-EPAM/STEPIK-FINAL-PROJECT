from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT_TEXT = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")
    AFTER_ADDING_PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    AFTER_ADDING_BASKET_PRICE_TEXT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")


class BasketPageLocators():
    BASKET_HEADER_TEXT = (By.CSS_SELECTOR, "div.page-header.action h1")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")


