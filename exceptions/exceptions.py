class AlreadyInList(Exception):
    def __init__(self, msg):
        self.msg = msg

    def test(self):
        return 'hey'

    def __str__(self):
        return self.msg



class Roll():

    def __init__(self):
        self.roll = []

    # throws a ZeroDivisionError if already in list
    def add_user(self, name):
        if name in self.roll:
            raise AlreadyInList(name + ' is in list')

        self.roll.append(name)

roll = Roll()
roll.add_user('saer')
try:
    roll.add_user('saer')
except AlreadyInList as error:
    print(error.test())
    print(error)
    s = input('please input again')
    roll.add_user(s)






