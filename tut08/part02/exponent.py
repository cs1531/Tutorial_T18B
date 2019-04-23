''' Question:
    Rewrite the following function with a high degree of cohesion and low coupling

def exponent():
    num = int(input("Enter in a number: "))
    exponent = int(input("Raise the number to the power of: "))
    answer = pow(num, exponent)
    print (answer)
'''


def get_num(question):
    num = int(input(question))
    return num

def exponent(base,exp):
   answer = pow(base, exp)
   return answer

base = get_num("Insert base: ")
exp = get_num("Insert power to raise base to: ")
answer = exponent(base,exp)
print ("Answer: %d" % (answer))
