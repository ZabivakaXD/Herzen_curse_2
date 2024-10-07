def binSearch(massiv, findNumber):
    """
    Поиск числа с помощью бинарного поиска

    Функция берёт число по середине и сравнивает его с числом, которое нужно найти.
    Если число из серединны меньше нужного числа оно смещает левую границу на место среднего числа,
    если число из середины больше нужного числа оно смещает правую границу на место среднего числа.

    Функция возвращает загаданное число и попытку, с которой оно было найденно
    """
    comparison = 0
    left = -1
    right = len(massiv)
    while left < right - 1:
        mid = (left + right) // 2
        comparison += 1
        if massiv[mid] < findNumber:
            left = mid
        else:
            right = mid
    return massiv[right], comparison

def GuestNumber(findNumber, start, end):
    """
    Основная функция запуска

    Функция принимает число, которое нужно найти, а также начало и конец диапазона поиска.
    Создаёт массив из этого диапазона и вызывает функцию поиска, откуда и приходит ответ

    Функция возвращает загаданное число и попытку, с которой оно было найденно
    """
    #findNumber, start, end = map(int, input("Загадайте число, а также начало и конец диапазона поиска ").split())
    massiv = list(range(start, end + 1))
    answer = binSearch(massiv, findNumber)
    #print("Загаданное число ", answer[0], " Нашли с ", answer[1], " попытки")
    return answer

#GuestNumber()

def test_GuessNumber():
    answer = GuestNumber(1, 1, 10)
    assert answer[0] == 1 and answer[1] == 3, "dont work"
    answer = GuestNumber(3, 1, 10)
    assert answer[0] == 3 and answer[1] == 3, "dont work"
    answer = GuestNumber(79, 1, 100)
    assert answer[0] == 79 and answer[1] == 6, "dont work"
    answer = GuestNumber(79, -100, 100)
    assert answer[0] == 79 and answer[1] == 7, "dont work"
    answer = GuestNumber(893, 1, 1000)
    assert answer[0] == 893 and answer[1] == 10, "dont work"

test_GuessNumber()