class AlreadyInListError(Exception):

    def __init__(self, name):
        self._name = name

    def test(self):
        return 'error'

    def __str__(self):
        return self._name + ' is already in the list'

class Roll:

    def __init__(self):
        self._roll = []

    def add_user(self, name): # throws an AlreadyInListError if name is in list
                              # throws a ZeroDivisionError for some reason
        if name in self._roll:
            raise AlreadyInListError(name)

        self._roll.append(name)


roll = Roll()
roll.add_user('saer')

try:
    roll.add_user('saer')
    # and other methods
    
except AlreadyInListError as error:
    print(error.test())
    s = input(str(error))
    roll.add_user(s)
except ZeroDivisionError:
    # do something else about this


def test_raises_error_add_user():
    roll = Roll()
    roll.add_user('saer')
    try:
        roll.add_user('saer')
        # and other methods
        
    except AlreadyInListError as error:
        assert error.name == 'saer'
        return

    assert('False')



