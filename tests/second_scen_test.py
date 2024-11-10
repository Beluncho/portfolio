from pages.second_scene_page import SbisPage


class TestPartners:

    def test_sbis(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.fill_fields()
