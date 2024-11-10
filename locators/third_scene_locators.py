from selenium.webdriver.common.by import By


class PageLocators:
    LOCAL = (By.XPATH, "//div[@class = 'sbisru-Footer__cell pb-16 pb-sm-8']//a[@href='/download']")
    DOWNLOAD = (By.XPATH, "//div[@class = 'sbis_ru-DownloadNew-loadLink']"
                          "//a[@href = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")

