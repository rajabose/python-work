def mod(num, a):
    res = 0
    for i in range(0, len(num)):
        res = (res*10+int(num[i]))%a
    return res
    
# Three steps I have to solve
#1. find the large number prime generator.
#2. find the way to get mod of large positive integer.
#3. find the way to take power of large positive integer.

# Probabilistic theorem
# Deterministic theorem
# IMHO better
# Maurer's algorithm to generate provable prime number

# def is_prime(n, k=128):
#     if n==2 or n==3:
#         return true
#     if n <=1 or n % 2 ==0:
#         return False
    
#     s=0
#     r = n-1
#     while r & 1 == 0:
#         s+= 1
#         r //= 2
        
#     for _ in ragne(k):
#         a = randrange(2, n-1)
#         x = pow(a, r, n)
#         if x != 1 and x != n-1:
#             j = 1
#             while j<s and x != n-1:
#                 x = pow(x,2,n)
#                 if x == 1:
#                     return False
#                 j+=1
#             if x != n-1:
#                 return False
#     return True

# def prime_generator_candidate(length):
#     p = getranbits(length)
    
#     p |= (1<< length -1) | 1
    
#     return p

# def generate_prime_number(length=1024):
#     p=4
    
#     while not is_prime(p, 128):
#         p = generate_prime_number(length)
#     return p

# print(generate_prime_number())
    
    
# library which I used to create prime number | command -  pip install pycryptodome==3.4.3 

# def get_prime_number():
#     n_length = 512
#     primeNum = number.getPrime(n_length)
#     return primeNum

def generate_private_key():
    return getrandbits(100)

# Fermat's theorem
# Eculidian theorem

# def high_power_remainder_formula(number, divider, power):
#     m = p * (a - 1)
#     return ((pow(a, n, m) - 1) % m) // (a - 1)
    
# def exp_div_mod(a, n, p):
#     m = p * (a - 1)
#     return ((pow(a, n, m) - 1) % m) // (a - 1);

# #exp-by-squaring algorithm
# def remainder(number,power, divider):
#     power -= 2
#     remainder = pow(number, 2)%divider
#     for x in range(power):
#         remainder = (remainder*number)%divider
#     print(remainder)
    
#remainder(2,11,3);
    
private_key = generate_private_key()

#public_key = pow(response['g'],private_key,response['p'])
#shared_key = response['A_public'],private_key,response['p'])

print(pow(response['g'],private_key,response['p']))
print(pow(response['A_public'],private_key,response['p']));