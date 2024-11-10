from pages.third_scene_page import SbisPage
import requests
import os

class TestThird:

    def test_sbis(self, driver):
        sbis_page = SbisPage(driver, 'https://sbis.ru/')    # BasePage
        sbis_page.open()    # def open()
        sbis_page.fill_fields()

    def test_file(self):
        r = requests.get('https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe')
        with open('data.exe', "wb") as file:
            file.write(r.content)

    def test_size_file(self):
        file_size = os.path.getsize('data.exe')
        assert file_size == 12039392, 'file is larger than 11.4 mb'
        path = 'data.exe'
        os.remove(path)




