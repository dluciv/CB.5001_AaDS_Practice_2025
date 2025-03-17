import unittest
from unittest.mock import patch
from io import StringIO

class ASCII85Test(unittest.TestCase):
    def test_who_am_i(self):
        self.assertEqual(1, 1)

    def test_greet(self):
        sio = StringIO()
        with patch('sys.stdout', new=sio) as fakeOutput:
            print("Привет, ASCII85!")
        self.assertEqual(sio.getvalue(), "Привет, ASCII85!\n")
