import random
import time

def numero_aleatorio():
    return random.randint(1,10)

def dobra_numero_aleatorio(num):
    return num*2

if __name__ == "__main__":
    while True:
        num = numero_aleatorio()
        resultado = dobra_numero_aleatorio(num)
        print(f"O dobro e {num} é {resultado}.")
        time.sleep(2)