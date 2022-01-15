import random

abc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"


def create_passwor(dlugosc):
    out = ""
    for x in range(dlugosc):
        pozycja = random.randint(0, 71)
        #  dasdasdaprint(abc[pozycja])pozycja
        out += (abc[pozycja])
        print(out)
while True:
    a = input('podaj dlugosc hasla:')
    create_passwor(int(a))