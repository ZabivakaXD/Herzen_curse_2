def foo(author, x):
    """Пример замыкания
    """

    author = 'Zhukov'  # enclosing, внешняя,
    x = 400

    # объемлющая
    def inner_boo(author, x) -> dict:
        print(author, x + 1)
        return {'author': author, 'year': x + 1}

    return inner_boo

f = foo("Bolotov", 2024)
f_s = f("Kostya", 19)

f_s