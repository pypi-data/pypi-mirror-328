import random

class Error(Exception):
    def __init__(self, message):
        super().__init__(message)

def modular_inverse(a, n):
    if type(a) != int or type(n) != int: raise Error('Invalid input type')
    elif a <= 0 or n <= 0: raise Error('Input must be a positive integer')

    s0, s1 = 1, 0
    r0, r1 = a, n

    while r1 > 0:
        q = r0 // r1
        r0, r1 = r1, r0 - (q*r1)
        s0, s1 = s1, s0 - (q*s1)

    if  r0 != 1: raise Error('Inputs must be coprime')
    if s0 < 0: s0 %= n

    return s0

def sieve_of_eratosthenes(n):
    if type(n) != int: raise Error('Invalid input type')

    primes = []
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def random_prime(a, b, accuracy=7, max=300):
    if type(a) != int or type(b) or type(accuracy) or type(max) != int: raise Error('Invalid input type')
    
    for _ in range(max):
        n = random.randint(a, b)
        if miller_rabin(n, accuracy):
            return n
    raise Error(f'No prime found in {max} iterations')

def text_to_number(text):
    if type(text) != str: raise Error('Invalid input type')

    text = text.upper()
    num = '1'
    for char in text:
        if ord(char) <= 99:
            num += str(ord(char))
        else:
            raise Error('Invalid character')

    return int(num)

def number_to_text(number):
    if type(number) != int: raise Error('Invalid input type')

    number = str(number)
    if number[0] != '1':
        raise Error('Invalid number')
    else:
        number = number[1:]
        txt = ''
        for i in range(0, len(number), 2):
            txt += chr(int(number[i]+number[i+1]))

        return txt.lower()