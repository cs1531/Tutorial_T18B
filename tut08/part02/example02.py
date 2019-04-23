'''A function with high cohesion, but strong coupling'''
def get_num():
    num = float(input("Enter Number One: "))
    return num

def add():
    num_1 = get_num()
    num_2 = get_num()
    addition = num_1 + num_2
    return addition

print("Sum: " + str(add()))
