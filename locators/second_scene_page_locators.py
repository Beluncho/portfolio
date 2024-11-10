from selenium.webdriver.common.by import By


class PageLocators:
    CONTACTS = (By.XPATH, "//a[@href= '/contacts']")
    REGION = (By.XPATH, "//div [@class= 's-Grid-container s-Grid-container--alignBaseline"
                        " s-Grid-container--noGutter pb-4 pb-xm-16 pr-16 pr-xm-0']"
                        "//span[@class= 'sbis_ru-Region-Chooser__text sbis_ru-link']")

    PARTNERS = (By.XPATH, "//div [@title = 'СБИС - Ярославль']")
    REGIONS = (By.XPATH, "//body//div[@class = '']//div[@id = 'contacts_clients']")

    KAMCHATKA = (By.XPATH, "//ul[@class = 'sbis_ru-Region-Panel__list-l']//span[@title = 'Камчатский край']")
    KAMCHATKA_PARTNERS = (By.XPATH, "//div [@title = 'СБИС - Камчатка']")

