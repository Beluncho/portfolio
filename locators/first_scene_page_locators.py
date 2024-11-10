from selenium.webdriver.common.by import By


class PageLocators:
    CONTACTS = (By.XPATH, "//a[@href= '/contacts']")
    TENZOR = (By.XPATH, "//a[@href= 'https://tensor.ru/']")
    STRENGHT = (By.XPATH, "//p[@class= 'tensor_ru-Index__card-title tensor_ru-pb-16']")
    ABOUT = (By.XPATH, "//a[@href='/about']")
    WORK = (By.XPATH, "//img[@width='270'][@height='192']")
