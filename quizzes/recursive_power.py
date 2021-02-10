from random import randint


# Assume all inputs are reasonable and only whole numbers
# Have a range from -inf to inf
# Accept (-) exponents and (-) bases

# Base case 

# 0 exponent returns 1
# 0 base returns 0
# 1 base returns 1

def raise_power(base:int,exponent:int):
    """
    Return a float showing the answer of the raised base num
    
    """

    if base == 1:
        return 1
    elif base == 0:
        return 0
    
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1/(base * 1/raise_power(base,exponent+1))
    else:
        return base * raise_power(base,exponent-1)

for i in range(0,10):
    base     = randint(-25,25)
    exponent = randint(-25,25)
    print(base,exponent)
    assert raise_power(base,exponent) == base**exponent 