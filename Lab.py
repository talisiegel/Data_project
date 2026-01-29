
import math 

def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)
    
    

def num_digits(n):
    return len(str(abs(n)))

def tip_amount(total,percent):
    return total * (percent / 100)

