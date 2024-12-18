import time

class Timer:
    """Менеджер контекста для измерения времени выполнения блока кода."""
    def __enter__(self):  # Начало отсчета времени
        self.start = time.perf_counter()  
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # Конец отсчета времени
        self.end = time.perf_counter()  
        self.elapsed = self.end - self.start
        print(f"Время выполнения: {self.elapsed:.2f} секунд")

def fibonacci_generator(n):
    """Функция-генератор чисел Фибоначчи до n элементов."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    N = 10**6  # Количество чисел Фибоначчи
    with Timer():
        for _ in fibonacci_generator(N):
            pass

main()