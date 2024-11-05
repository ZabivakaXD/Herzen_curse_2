def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)
    return None  # Возвращаем None, если подходящие индексы не найдены

def two_sum_hushed(lst, target):
    # Создаем список пар (значение, индекс)
    indexed_lst = [(value, index) for index, value in enumerate(lst)]
    print(indexed_lst)
    
    # Сортируем по значениям
    indexed_lst.sort(key=lambda x: x[0])
    print(indexed_lst)
    
    left = 0
    right = len(indexed_lst) - 1
    
    while left < right:
        current_sum = indexed_lst[left][0] + indexed_lst[right][0]
        
        if current_sum == target:
            # Возвращаем индексы в исходном списке, наименьшие по значению
            return tuple(sorted([indexed_lst[left][1], indexed_lst[right][1]]))
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return None  # Возвращаем None, если подходящие индексы не найдены

def two_sum_hushed_lst(lst, target):
    # Создаем список пар (значение, индекс)
    indexed_lst = [(value, index) for index, value in enumerate(lst)]
    print(indexed_lst)
    
    # Сортируем по значениям
    indexed_lst.sort(key=lambda x: x[0])
    print(indexed_lst)
    
    left = 0
    right = len(indexed_lst) - 1
    result = []
    
    while left < right:
        current_sum = indexed_lst[left][0] + indexed_lst[right][0]
        
        if current_sum == target:
            # Возвращаем индексы в исходном списке, наименьшие по значению
            result.append(sorted([indexed_lst[left][1], indexed_lst[right][1]]))
            indexed_lst.remove(indexed_lst[left])
            indexed_lst.remove(indexed_lst[right])
            left = 0
            right = len(indexed_lst) - 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    if len(result) != 0:         
        return result
    else:
        return None  # Возвращаем None, если подходящие индексы не найдены

lst = [3, 2, 1, 9, 5, 7, 6, 8, 4]
#lst = list(map(int, input("Введите числа ")).split(" "))
target = 8
#target = int(input("Введите цель "))
result = two_sum(lst, target)
result_fast = two_sum_hushed(lst, target)
result_fast_lst = two_sum_hushed_lst(lst, target)
print(result)
print(result_fast)
print(result_fast_lst)
