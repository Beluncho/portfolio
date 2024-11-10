import time

from pages.base_page import BasePage
from locators.third_scene_locators import PageLocators as Locators


class SbisPage(BasePage):

    def fill_fields(self):
        self.element_is_visible(Locators.LOCAL).click()
        self.element_is_visible(Locators.DOWNLOAD)
        time.sleep(5)
