import random

def random_number_generator(parameters):
    for _ in range(parameters[0]):
        yield random.randint(parameters[1], parameters[2])

def main():
    parametrs = [5, 1, 10]
    for number in random_number_generator(parametrs):
        print(number)
    
main()