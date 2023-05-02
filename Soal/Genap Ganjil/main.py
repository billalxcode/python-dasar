## Program Genap Ganjil
## Soal:
## Buatlah program yang menanyakan sebuah bilangan kepada user.
## Program kemudian memunculkan apakah bilangan yang dimasukkan itu genap atau ganjil.
import random

def is_ganjil(angka: int):
    return angka % 2

# Test
# angka = random.randint(1, 999)
angka = 10
ganjil = is_ganjil(angka)
if ganjil == 1:
    print (f"Angka {angka} merupakan angka ganjil")
else:
    print (f"Angka {angka} merupakan angka genap")
