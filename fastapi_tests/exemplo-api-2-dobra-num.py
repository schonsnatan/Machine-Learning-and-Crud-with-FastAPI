import time

def double_random_number(num):
    return num*2

def read_last_number():
    try:
        with open("numbers.txt", "r") as file:
            lines = file.readlines()
            if lines:
                return int(lines[-1].strip())
            else:
                print("empty file.")
    except FileNotFoundError:
        print("file not found.")
        return None
    
if __name__ == "__main__":
    while True:
        num = read_last_number()
        if num is not None:
            result = double_random_number(num)
            print(f"The number double of {num} is {result}.")
            time.sleep(1)