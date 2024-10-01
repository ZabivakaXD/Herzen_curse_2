def binSearch(massiv, findNumber):
  global comparison
  left = -1
  right = len(massiv)
  while left < right - 1:
      mid = (left + right) // 2
      comparison += 1
      if massiv[mid] < findNumber:
          left = mid
      else:
          right = mid
  return massiv[right]

findNumber = int(input("Загадайте число "))
start, end = map(int, input("Напишите начало и конец диапазона поиска ").split())
massive = list(range(start, end + 1))
comparison = 0
print("Загаданное число " + str(binSearch(massive, findNumber)) + " Нашли с " + str(comparison) + " попытки")