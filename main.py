import random
import time

print('-----Generador de contraseñas-----')
time.sleep(0.5)
car = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


long = int(input('Escribe la longitud de tu contraseña (en números)'))

passw = ''


while len(passw) < long:
    passw += random.choice(car)

print('Contraseña lista')
time.sleep(0.5)
print(passw)