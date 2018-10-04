# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest

class HomePageTest(TestCase):
    '''тест на токсичность'''

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do list</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response,'home.html')
