from main import CurrencyRates
from controllers import CurrencyRatesCRUD
from controllers import ViewController
from terminaltables import AsciiTable

def main():

    c_r = CurrencyRates(['USD', 'EUR', 'GBP'])
    c_r.values = [("USD", "02-04-2025 11:10", "90"),
                ("EUR", "02-04-2025 11:11", "91"),
                ("GBP", '02-04-2025 11:37', '100')]

    c_r_controller = CurrencyRatesCRUD(c_r)
    c_r_controller.create()
    output = ViewController(c_r)
    print(output())

    title = "Актуальные курсы валют:"
    current_rates = c_r.get_all_rates()
    table_instance = AsciiTable(current_rates, title)
    table_instance.justify_columns[2] = "right"
    print(table_instance.table)
    print()

input("Проверка добавилось ли")

if __name__ == "__main__":
    main()