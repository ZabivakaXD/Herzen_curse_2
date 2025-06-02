import sys
import functools
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime

def deco(func=None, *, handle=sys.stdout):
    """
    Параметризованный декоратор для логирования вызовов функций.
    Варианты использования:
    - @deco - логирование в консоль (по умолчанию)
    - @deco(handle='logs.json') - логирование в JSON-файл
    - @deco(handle=sqlite3.Connection) - логирование в SQLite базу
    """
    if func is None:
        return lambda func: deco(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            # Вызываем функцию и получаем результат
            result = func(*args, **kwargs)
            
            # Подготавливаем данные для логирования
            log_data = {
                'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'func_name': func.__name__,
                'params': {
                    'args': args,
                    'kwargs': kwargs
                },
                'result': result
            }
            
            # Логирование в зависимости от типа handle
            if isinstance(handle, str) and handle.endswith('.json'):
                # Логирование в JSON файл
                    with open(handle, 'a+') as f:
                        json.dump([log_data], f, indent=2)
                        f.write('\n')    
            elif isinstance(handle, sqlite3.Connection):
                # Логирование в SQLite базу
                cur = handle.cursor()
                # Создаем таблицу, если ее нет
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS logtable (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datetime TEXT,
                        func_name TEXT,
                        params TEXT,
                        result TEXT
                    )
                """)
                # Вставляем запись
                cur.execute(
                    "INSERT INTO logtable (datetime, func_name, params, result) VALUES (?, ?, ?, ?)",
                    (
                        log_data['datetime'],
                        log_data['func_name'],
                        json.dumps(log_data['params']),
                        json.dumps(log_data['result'])
                    )
                )
                handle.commit()
            else:
                # Логирование в консоль (по умолчанию)
                print(f"[{log_data['datetime']}] Function '{log_data['func_name']}' called with:", file=handle)
                print(f"  Args: {log_data['params']['args']}", file=handle)
                print(f"  Kwargs: {log_data['params']['kwargs']}", file=handle)
                print(f"  Result: {log_data['result']}\n", file=handle)
            
            return result
        except Exception as e:
            raise e
        
    return inner

def showlogs(con):
    """
    Утилита для отображения логов из SQLite базы
    """
    if not isinstance(con, sqlite3.Connection):
        print("Error: showlogs expects sqlite3.Connection object", file=sys.stderr)
        return
    
    try:
        cur = con.cursor()
        cur.execute("SELECT datetime, func_name, params, result FROM logtable ORDER BY datetime DESC")
        logs = cur.fetchall()
        
        if not logs:
            print("No logs found in database")
            return
        
        print("\n=== LOGS FROM DATABASE ===")
        for log in logs:
            dt, func_name, params, result = log
            print(f"\n[{dt}] {func_name}")
            print("Params:", json.loads(params))
            print("Result:", json.loads(result))
        print("\n=== END OF LOGS ===")
    except Exception as e:
            raise e

@deco() # Default: Вариант по умолчанию
def f2(x):
    return x**2

f2(20)

@deco(handle='logger.json') # Default: Вариант по умолчанию
def f3(x):
    return x**3

f3(30)

db_con = sqlite3.connect(":memory:")

@deco(handle=db_con)
def f4(x):
        return x ** 4

f4(40)

# Просмотр логов
showlogs(db_con)

# @contextmanager
# def dbc():
#     con = sqlite3.connect(':memory:')
#     try:
#         yield con
#     finally:
#         con.close()

# with dbc() as con:
#     @trace(handle=con)
#     def f4(x):
#         return x ** 4

#     f4(40)

#     cursor = con.cursor()
#     cursor.execute('SELECT * FROM logtable')
#     for row in cursor.fetchall():
#         print(row)

#     print(f4(10))