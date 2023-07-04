https://www.youtube.com/watch?v=XCIBOl3FTKo

import random
import string

def generate(min_length, numbers=True, special_characters=True):
    lett = string.ascii_letters
    digi = string.digits
    spec = string.punctuation

    char = lett
    if numbers:
        char += digi
    if special_characters:
        char += spec
    
    passwd = ""
    criteria = False
    contno = False
    contspec = False

    while not criteria or len(passwd) <min_length:
        new = random.choice(char)
        passwd += new

        if new in digi:
            contno = True
        elif new in spec:
            contspec = True
        
        criteria = True
        if numbers:
            criteria = contno
        if special_characters: 
            criteria = criteria and contspec
    
    return passwd

passwd = generate(10)
print("Generated password is:", passwd)
