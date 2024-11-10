from pages.first_scen_page import SbisPage


class TestFirst:

    def test_sbis(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.fill_fields()

    def test_tensor(self, driver):
        tensor_page = SbisPage(driver, 'https://tensor.ru/')
        tensor_page.open()
        tensor_page.fill2_fields()
