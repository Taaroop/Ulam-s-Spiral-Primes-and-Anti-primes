import math
import turtle

turtle.speed(0)

# Prime function

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True

# Highly composite number (Anti-primes) function

def factor_count(num):
    factor_counter = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            factor_counter += 1
    
    if math.sqrt(num) == int(math.sqrt(num)):
        return (factor_counter-1)*2 + 1
    else:
        return factor_counter*2       

def anti_prime(num):
    f = factor_count(num)
    for check in range(1, num):
        if factor_count(check) >= f:
            return False
    else:
        return True

# Ulam spiral function

def ulam_spiral(num, m):
    length = m
    increment = m
    step = 0
    n = 1
    for i in range(num):
        L = length+step
        for j in range(2):
            for k in range(0, L, m):
                turtle.penup()
                turtle.forward(m)
                if anti_prime(n) == True: # Try out the anti-prime Ulam spiral yourself!
                    turtle.dot()
                n += 1
            turtle.right(90)
        step += increment

# ulam_spiral(1000, 5)
