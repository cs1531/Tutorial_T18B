
def test_avail():

    ing = ['beef', 'tomato', 'bread']
    m = MenuItem(1, ing, 5, True, 'nut-free')
    menu = MenuSystem([m])

    test1 = menu.viewMenuItem(1)
    assert test1 != None
    assert test1.is_avail() == True



