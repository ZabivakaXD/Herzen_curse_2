import sys
import functools
import json
import sqlite3
from datetime import datetime

def trace(func=None, *, handle=sys.stdout):
    """
    Параметризованный декоратор для логирования вызовов функций.
    Варианты использования:
    - @trace - логирование в консоль (по умолчанию)
    - @trace(handle='logs.json') - логирование в JSON-файл
    - @trace(handle=sqlite3.Connection) - логирование в SQLite базу
    """
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        # Вызываем функцию и получаем результат
        result = func(*args, **kwargs)
        
        # Подготавливаем данные для логирования
        log_data = {
            'datetime': datetime.now().isoformat(),
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
            try:
                with open(handle, 'a+') as f:
                    f.seek(0, 2)  # Перемещаемся в конец файла
                    if f.tell() == 0:
                        json.dump([log_data], f, indent=2)
                    else:
                        f.seek(0)
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError:
                            data = []
                        data.append(log_data)
                        f.seek(0)
                        f.truncate()
                        json.dump(data, f, indent=2)
            except Exception as e:
                print(f"Error writing to JSON file: {e}", file=sys.stderr)
        
        elif isinstance(handle, sqlite3.Connection):
            # Логирование в SQLite базу
            try:
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
            except Exception as e:
                print(f"Error writing to SQLite database: {e}", file=sys.stderr)
        
        else:
            # Логирование в консоль (по умолчанию)
            try:
                print(f"[{log_data['datetime']}] Function '{log_data['func_name']}' called with:", file=handle)
                print(f"  Args: {log_data['params']['args']}", file=handle)
                print(f"  Kwargs: {log_data['params']['kwargs']}", file=handle)
                print(f"  Result: {log_data['result']}\n", file=handle)
            except Exception as e:
                print(f"Error writing to console: {e}", file=sys.stderr)
        
        return result

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
        print(f"Error reading logs from database: {e}", file=sys.stderr)