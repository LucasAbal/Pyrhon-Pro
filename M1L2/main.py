import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
long = int(input("Escribe la longitud de la contraseña: "))


for i in range(long):
    num = random.randint(0,71)
    select = caracteres[num]
    password = password + select

print (password)
