import app.error_handling as error
from fastapi import HTTPException
import unittest

class TestRequestErrorHandling(unittest.TestCase):
    def test_request_error_handling(self):
        with self.assertRaises(HTTPException) as _:
            error.raise_request_error("")
        self.assertEqual(_.exception.status_code,400,msg = "Wrong status code was given")

class TestBooleanErrorHandling(unittest.TestCase):
    def test_boolean_error_handling(self):
        with self.assertRaises(HTTPException) as _:
            error.raise_boolean_error()
        self.assertEqual(_.exception.status_code,400,msg = "Wrong status code was given")
