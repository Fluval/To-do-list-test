# -*- coding: utf-8 -*-
# !/usr/bin/env python3.6

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    """тест нового посетителя"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def wait_for_row_list_table(self, row_text):
        """подтвержжение строки в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_list_table('1 Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(u'Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_list_table('1 Купить павлиньи перья')
        self.wait_for_row_list_table('2 Сделать мушку из павлиньих перьев')
        self.fail(u'Закончить тест')
