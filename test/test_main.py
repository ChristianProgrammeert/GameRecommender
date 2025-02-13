import main
import unittest

class MainTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.read_root(),{"message": "Hello World"}, msg="Api output doesn't match expectations.")
