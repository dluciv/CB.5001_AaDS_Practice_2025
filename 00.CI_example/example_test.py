#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO

import library

class LibraryTest(unittest.TestCase):
    def test_who_am_i(self):
        self.assertEqual(library.who_am_i(), "Олег")

    def test_greet(self):
        sio = StringIO()
        with patch('sys.stdout', new=sio) as fakeOutput:
            library.greet()
        self.assertEqual(sio.getvalue(), "Привет, Олег!\n")
