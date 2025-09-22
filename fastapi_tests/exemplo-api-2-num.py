import random
import time
from meu_decorador import alou_decorator

@alou_decorator
def generate_random_number():
    num = random.randint(1,10)
    print(num)
    with open("numbers.txt", "a") as file:
        file.write(f"{num}\n")

if __name__ == "__main__":
    while True:
        generate_random_number()
        time.sleep(1)