from fastapi import HTTPException

wanted_characters = ["0","1"]
unexpected_characters_message = f"Answer includes unexpected characters. please use one of {wanted_characters}"
wanted_length = 6
unexpected_length_message = f"Answer is not {wanted_length} characters long"

class Answers:
    def __init__(self, rage_inducing,action_packed,skill_based,mature,open_world,multiplayer):
        self.is_rage_inducing = rage_inducing
        self.is_action_packed = action_packed
        self.is_skill_based = skill_based
        self.is_mature = mature
        self.is_open_world = open_world
        self.is_multiplayer = multiplayer

def parse_input(input_string):
    """Central function that combines all functions in this file. Easy to call from outside of file."""
    if check_characters(input_string) and check_length(input_string):
        return convert_into_class(sort_input(input_string))

def check_characters(input_string):
    """Checks whether the input string only contains useful characters. Gives user feedback if input does not meet requirements."""
    for _ in input_string:
        if _ in wanted_characters and input_string: #input_string returns true if the input string is not empty.
            continue
        else:
            raise HTTPException(status_code = 400, detail = unexpected_characters_message)
    return True

def check_length(input_string):
    """Checks whether the input string is of expected length."""
    if len(input_string) != wanted_length:
        raise HTTPException(status_code = 400, detail = unexpected_length_message)
    else:
        return True

def sort_input(sorting_input):
    """Converts string input into a list of booleans."""
    sorted_output = []
    for i in sorting_input:
        sorted_input = False
        if i == wanted_characters[1]:
            sorted_input = True
        sorted_output.append(sorted_input)
    return sorted_output

def convert_into_class(list_input:list):
    """Converts a list of booleans into a class with model Answers"""
    return Answers(*list_input)

TestClass = parse_input("100101")
print(TestClass.is_rage_inducing,TestClass.is_action_packed,TestClass.is_skill_based,TestClass.is_mature,TestClass.is_open_world,TestClass.is_multiplayer)