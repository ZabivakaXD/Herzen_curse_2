def find_country_by_city(countries_cities, cities_to_find):
    dict_city_country = {}
    for country in countries_cities: 
        many_city = countries_cities.get(country)
        for city in many_city:
            dict_city_country[city] = country
    
    for need_to_find in cities_to_find:
        result = dict_city_country.get(need_to_find)
        if result != None:
            print(need_to_find, "-", result)
        else:
            print("Такой страны нет в списке")         

def main():
    countries_cities = {
        "Россия": ["Москва", "Санкт-Петербург", "Сургут"],
        "США": ["Вашингтон", "Нью-Йорк", "Лос-Анджелес"],
        "Франция": ["Париж", "Лион", "Марсель"]
    }
        
    cities_to_find = ["Москва", "Нью-Йорк", "Париж", "Токио"]
    find_country_by_city(countries_cities, cities_to_find)
    
main()