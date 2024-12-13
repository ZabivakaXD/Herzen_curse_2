import requests

def main():
    # Получить данные с первого адреса
    response = requests.get('https://kodaktor.ru/j/numbers')

    # Преобразование JSON-ответа в Python-объект
    dict_numbers = response.json()
    arr_arr_numbers = [*dict_numbers.values()]
    arr_numbers = arr_arr_numbers[0]
    
    # Суммирование чисел
    total_sum = 0
    for mini_dict in arr_numbers:
        total_sum += mini_dict.get('value')
    
    # Подготовка данных для отправки
    result = f"{total_sum} ({'Болотов'})"
    
    # Отправка результата методом POST
    post_response = requests.post('https://docs.google.com/forms/u/0/d/e/1FAIpQLSeZyDJ_68Mj7io5vtjyNqul7ceNE1t5Z5KkkN7foqxbIcUsbg/formResponse', data={'entry.364005965': result})

    # Проверка успешности POST-запроса
    if post_response.status_code == 200:
        print("Данные успешно отправлены!")
    else:
        print("Ошибка при отправке данных:", post_response.status_code)
        
main()

