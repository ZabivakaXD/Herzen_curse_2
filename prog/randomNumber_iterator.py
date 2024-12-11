import random

class RandomNumberIterator:
    def __init__(self, parametrs):
        self.count = parametrs[0]  # Количество случайных чисел
        self.start = parametrs[1]  # Начало диапазона
        self.end = parametrs[2]    # Конец диапазона
        self.generated = 0  # Счетчик сгенерированных чисел

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:
            self.generated += 1
            return random.randint(self.start, self.end)
        else:
            raise StopIteration

def main():
    parametrs = [5, 1, 10]
    random_iterator = RandomNumberIterator(parametrs)
    for number in random_iterator:
        print(number)
        
main()