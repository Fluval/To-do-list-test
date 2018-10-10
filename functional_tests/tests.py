# -*- coding: utf-8 -*-
#!/usr/bin/env python3.6

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''
    def setUp(self):
        self.browser = webdriver.Firefox()

    def check_for_row_list_table(self, row_text):
        '''подтвержжение строки в таблице списка'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.check_for_row_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_list_table('1: Купить павлиньи перья')
        self.check_for_row_list_table('2: Сделать мушку из павлиньих перьев')
        self.fail('Закончить тест')

if __name__ == '__main__':
    unittest.main()