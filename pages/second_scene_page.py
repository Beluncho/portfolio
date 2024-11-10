import time

from pages.base_page import BasePage
from locators.second_scene_page_locators import PageLocators as Locators


class SbisPage(BasePage):

    def fill_fields(self):
        self.element_is_visible(Locators.CONTACTS).click()
        self.element_is_visible(Locators.REGION)
        self.element_is_visible(Locators.PARTNERS)
        self.element_is_visible(Locators.REGIONS)
        self.element_is_visible(Locators.REGION).click()
        self.element_is_visible(Locators.KAMCHATKA).click()
        self.element_is_visible(Locators.KAMCHATKA_PARTNERS)
        time.sleep(5)
