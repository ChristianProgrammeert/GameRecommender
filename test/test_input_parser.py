import unittest
from app import input_parser as parser

very_long_string = "1011"*100
testing_range = 6

class TestCharacterChecker(unittest.TestCase):
    def test_character_checker(self):
        testing_string = ""
        for _ in range(testing_range):
            testing_string += parser.wanted_characters[0]
        self.assertTrue(parser.check_characters(testing_string),"Wanted characters filtered.")

    def test_character_checker_error_handling(self):
        self.assertRaises(BaseException,parser.check_characters,"1!3A56^&K%5`~~/*-\n","Illegal characters got through filter.")

    def test_character_checker_empty_string(self):
        self.assertRaises(BaseException,parser.check_characters,"","Empty string got trough filter.")
    # def test_character_checker_performance(self): #checks whether very long strings affect performance.
    #     self.assertTrue(parser.check_characters(very_long_string))

class TestLengthChecker(unittest.TestCase):
    def test_length_checker(self):
        testing_string = ""
        for _ in range(parser.wanted_length):
            testing_string += "_"
        self.assertTrue(parser.check_length(testing_string),"Doesn't accept wanted length.")

    def test_length_checker_long_string(self):
        self.assertRaises(BaseException,parser.check_length,very_long_string,"String with excess length passes filter.")

    def test_length_checker_short_string(self):
        testing_string = ""
        for _ in range(parser.wanted_length-1):
            testing_string += "_"
        self.assertRaises(BaseException, parser.check_length,testing_string,"String with insufficient length passes .")

    def test_length_checker_empty_string(self):
        self.assertRaises(BaseException,parser.check_length,"","Empty string got trough filter.")

class TestSortInput(unittest.TestCase):
    def test_sort_input(self, testing_string=""):
        testing_list_true = [True] * testing_range
        for _ in range(testing_range):
            testing_string += parser.wanted_characters[1]
        self.assertEqual(parser.sort_input(testing_string), testing_list_true,"Output list not as expected.")

    def test_sort_output_type(self,testing_string=str((parser.wanted_characters[1])*parser.wanted_length)):
        self.assertEqual(type(parser.sort_input(testing_string)[0]),bool,"Output list is not made of booleans.")

class TestClassConverter(unittest.TestCase):
    def test_class_converter(self):
        testing_list = [True] * parser.wanted_length
        TestingClass = parser.convert_into_class(testing_list)
        self.assertEqual(type(TestingClass.is_skill_based),bool,"Class variables are not booleans.")
        self.assertEqual(type(TestingClass.is_mature), bool, "Class variables are not booleans.")
        self.assertEqual(type(TestingClass.is_action_packed), bool, "Class variables are not booleans.")
        self.assertEqual(type(TestingClass.is_rage_inducing), bool, "Class variables are not booleans.")
    def test_class_converter_converting_from_string(self):
        testing_string = "True" * parser.wanted_length
        self.assertRaises(TypeError, parser.convert_into_class,testing_string,"Function accepts string as input")