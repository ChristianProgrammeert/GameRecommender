import unittest
from fastapi import HTTPException
from app import input_parser as parser

class TestInputChecking(unittest.TestCase):
    def test_check_inputs(self):
        self.assertEqual(parser.check_inputs([True,True,False,False]),True,"Incorrectly tags booleans as None")
        self.assertEqual(parser.check_inputs([None,False,False,True]),False,"Wrong values or None get trough")
        self.assertEqual(parser.check_inputs([True,False,1,False]),False,"Function accepts non-boolean values")

class TestClassConverter(unittest.TestCase):
    def test_class_converter(self):
        testing_list = [True] * 6
        TestClass = parser.convert_into_class(testing_list)
        self.assertEqual(type(TestClass.is_skill_based),bool,"Class variables are not booleans.")
        self.assertEqual(type(TestClass.is_mature), bool, "Class variables are not booleans.")
        self.assertEqual(type(TestClass.is_action_packed), bool, "Class variables are not booleans.")
        self.assertEqual(type(TestClass.is_rage_inducing), bool, "Class variables are not booleans.")
    def test_class_converter_converting_from_string(self):
        testing_string = "True"
        self.assertRaises(TypeError, parser.convert_into_class,testing_string,"Function accepts string as input")

class TestEntireFile(unittest.TestCase):
    def test_parse_input(self):
        test_list = [True,False]*3
        TestClass = parser.parse_input(test_list)

        self.assertEqual(TestClass.is_action_packed, False, "Values are scrambled")
        self.assertEqual(TestClass.is_skill_based, True, "Values are scrambled")
        self.assertEqual(TestClass.is_mature, False, "Values are scrambled")
        self.assertEqual(TestClass.is_open_world, True, "Values are scrambled")
    def test_wrong_input(self):
        with self.assertRaises(HTTPException) as _:
            TestClass = parser.parse_input([1,"a",False,{"Name":"Test"}])
        self.assertEqual(_.exception.status_code,400,msg = "Incorrect or no error raised with wrong datatypes")