# coding=utf-8
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест')

if __name__ == '__main__':
    unittest.main()