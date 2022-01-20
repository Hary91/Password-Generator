import random

def create_passwor(dlugosc, special=True, numbers=True):
    out = ""
    abc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    if special == True:
        abc += '!@#$%^&*()'
    if numbers == True:
        abc += '1234567890'

    for x in range(dlugosc):
        pozycja = random.randint(0, len(abc)-1)
        out += (abc[pozycja])
    return out

while True:
    a = input('podaj dlugosc hasla:')
    create_passwor(int(a))