# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from lists.views import home_page
from django.urls import resolve

class HomePageTest(TestCase):
    '''тест на токсичность'''

    def test_root_url_resolves_to_home_page_vies(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
