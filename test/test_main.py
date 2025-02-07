from GameRecommender.main import read_root
import unittest

class MainTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(read_root(), {"message": "Hello World"}, msg="Api output doesn't match expectations.")