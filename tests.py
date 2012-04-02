#!/usr/bin/env python
from django.test import TestCase
from django.test.client import Client

__all__ = ('TestOne',)

class TestOne(TestCase):
    c = Client()
    def test_empty(self):
        pass
