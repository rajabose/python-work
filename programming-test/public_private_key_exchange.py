import requests
from random import getrandbits
import math

ALICE_INFORMATION_URL = 'https://shortrndexercise.singular.net/get-key?'
BOB_RESPONSE_BACK_URL = 'https://shortrndexercise.singular.net/submit?'

# Count number of bits
def count_bits(number):
    return int((math.log(number)/math.log(2))+1)

# Generate number with given nunber of bits
def generate_private_key(number):
    bit_count = count_bits(number)
    return getrandbits(bit_count)

def make_request(email_address):
    url = ALICE_INFORMATION_URL
    params = {'email': email_address}
    headers = {"Content-Type":"application/json"}
    r = requests.get(url, params=params, headers=headers)
    return r.json()

def make_share_secret_request(email_address):
    response = make_request(email_address) 
    
    url = BOB_RESPONSE_BACK_URL
    private_key = generate_private_key(response['p'])
    
    params = {
        'email':email_address,
        'B_public': pow(response['g'], private_key, response['p']),
        'solution': pow(response['A_public'], private_key, response['p']),
        }
    
    headers = {"Content-Type":"application/json"}  
    res = requests.get(url, params=params, headers = headers)
    print(res.json())
    
make_share_secret_request('rajabose@gmail.com')