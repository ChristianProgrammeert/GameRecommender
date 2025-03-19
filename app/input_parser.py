from app.error_handling import raise_request_error

class Answers:
    def __init__(self, rage_inducing,action_packed,skill_based,mature,open_world,multiplayer):
        self.is_rage_inducing = rage_inducing
        self.is_action_packed = action_packed
        self.is_skill_based = skill_based
        self.is_mature = mature
        self.is_open_world = open_world
        self.is_multiplayer = multiplayer

error_message = "Please make sure all values are entered with booleans. rage_inducing | action_packed | skill_based | mature_themes | open_world | multiplayer"

def parse_input(input_list):
    """Central function that combines all functions in this file. Easy to call from outside of file."""
    if check_inputs(input_list):
        return convert_into_class(input_list)
    else: raise_request_error(error_message)

def check_inputs(input_list):
    """Checks whether all values have been given and if they are a boolean"""
    for _ in input_list:
        if _ is not None and type(_) is bool:
            continue
        else:
            return False
    return True

def convert_into_class(list_input:list):
    """Converts a list of booleans into a class with model Answers"""
    return Answers(*list_input)
