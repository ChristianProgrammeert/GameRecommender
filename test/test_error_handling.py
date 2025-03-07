import app.error_handling as error
from fastapi import HTTPException
import unittest

class TestInputErrorHandling(unittest.TestCase):
    def test_input_error_handling(self):
        with self.assertRaises(HTTPException) as _:
            error.raise_input_error()
        self.assertEqual(_.exception.status_code,400,msg = "Wrong status code was given")

class TestRequestErrorHandling(unittest.TestCase):
    def test_request_error_handling(self):
        with self.assertRaises(HTTPException) as _:
            error.raise_request_error("")
        self.assertEqual(_.exception.status_code,422,msg = "Wrong status code was given")
