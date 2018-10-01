# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest

class HomePageTest(TestCase):
    '''тест на токсичность'''

    def test_root_url_resolves_to_home_page_vies(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))
