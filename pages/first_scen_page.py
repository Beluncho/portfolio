import time

from pages.base_page import BasePage
from locators.first_scene_page_locators import PageLocators as Locators


class SbisPage(BasePage):

    def fill_fields(self):
        self.element_is_visible(Locators.CONTACTS).click()
        self.element_is_visible(Locators.TENZOR).click()
        time.sleep(5)

    def fill2_fields(self):
        self.element_is_visible(Locators.STRENGHT)
        self.element_is_visible(Locators.ABOUT).click()
        self.elements_are_visible(Locators.WORK)
        time.sleep(5)
