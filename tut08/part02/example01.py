'''A function with low cohesion '''
def add():
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter a number: "))
    sum = num_1 + num_2
    return sum

print ("The sum of the numbers is: %d" % add())
