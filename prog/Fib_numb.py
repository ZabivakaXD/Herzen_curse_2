def fibonacci_hand(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_hand(n - 1, memo) + fibonacci_hand(n - 2, memo)
    return memo[n]

from functools import cache

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#n = int(input("Введите номер числа Фибоначи"))
n = 10
memo = {0 : 0}
print(f"{n} по номеру число Фибоначи это, {fibonacci(n)}")
print(f"{n} по номеру число Фибоначи это, {fibonacci_hand(n, memo)}")
