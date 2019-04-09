import pytest

# returns True on valid username
# throws a UserInputError exception otherwise
def validate_user_name(s):
    pass

class UserInputError(Exception):

    def __init__(self, msg):
        self._msg = msg

class UserInputSpaceError(UserInputError):
    


class Test_validate_user_name(s):

    def test_string_has_space():
        s = 'sa er'
        try:
            validate_user_name(s)
        except UserInputError as e: 
            assert(e._msg == 'user contains space')
            
        
# main function
try:
    validate_user_name(s)
except UserInputSpaceError:
    # do something
except BufferOverFlowError:
    # do something more dramatic


