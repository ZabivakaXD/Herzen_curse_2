def foo(author, x):

    # author = 'Zhukov'  # enclosing, внешняя,
    # x = 400

    # объемлющая
    def inner_boo(author, x) -> dict:
        """
        :returns: dict with author and year values
        """
        print(author, x + 1)
        return {'author': author, 'year': x + 1}

    return inner_boo


f = foo('Pupkin', 100500)
f_s = f('Zhukov', 2024)

print(f_s)


def null_decorator(func):
    import logging

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    print("Вызываем", func.__name__, end=": ")

    def wrapper_f(*args, **kwargs):
        import time
        from time import strftime, gmtime
        logger.info(str(time.time()), strftime("%a, %d %b %Y %H:%M:%S +0000",
                                        gmtime()))
        res = func(*args, **kwargs)
        logger.info(str(time.time()), strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

        return res

    return wrapper_f


@null_decorator
def greet():
    return 'Hello!'


@null_decorator
def bye():
    return 'Bye!!!'


greet = null_decorator(greet)

greet()
# print(bye(), end='\n')


@null_decorator
def calculate(op1, op2, action):
    if action == '+':
        return op1 + op2


# print(foo()())
# calculate = null_decorator(calculate)

res = calculate(1, 2, "+")
print(res)



def f(N, t):
    return "reactive-mass"
d = {"Ra": f}
#d["Ra"](N, t)

d["Ra"] = lambda x: x*0.5**x
