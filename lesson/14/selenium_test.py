import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        # ChromeでWebページを取得
        self.driver.get('http://www.python.org')
        # titleの中身をassert
        self.assertIn('Python', self.driver.title)

        # <a>Downloads</a>をクリック
        self.driver.find_element_by_link_text('Downloads').click()
        # class="widget-title"を取得
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'widget-title')))

        self.assertEqual('Looking for a specific release?', element.text)

        # 検索フォームのelementを取得
        element = self.driver.find_element_by_name('q')
        # placeholderをクリア
        element.clear()
        # 検索フォームにpyconを入力
        element.send_keys('pycon')
        # Keys.RETURNでreturnボタン押下で検索を実行
        element.send_keys(Keys.RETURN)

        assert 'No results found' not in self.driver.page_source
