import ctypes
import os
import platform
import getpass
import locale
import win32api
import win32con
import win32gui
import calendar

# 1. Имя компьютера и пользователя
def get_user_info():
    computer_name = os.environ['COMPUTERNAME']
    user_name = getpass.getuser()
    return computer_name, user_name

# 2. Пути к системным каталогам
def get_system_paths():
    from ctypes.wintypes import MAX_PATH, HWND, HANDLE, DWORD, LPCWSTR
    from ctypes import windll, create_unicode_buffer

    CSIDL_SYSTEM = 0x0025  # C:\Windows\System32
    CSIDL_WINDOWS = 0x0024  # C:\Windows

    buf = create_unicode_buffer(MAX_PATH)
    windll.shell32.SHGetFolderPathW(None, CSIDL_SYSTEM, None, 0, buf)
    system_path = buf.value

    buf = create_unicode_buffer(MAX_PATH)
    windll.shell32.SHGetFolderPathW(None, CSIDL_WINDOWS, None, 0, buf)
    windows_path = buf.value

    return system_path, windows_path

# 3. Версия ОС
def get_os_version():
    return platform.platform()

# 4. Системные метрики
def get_system_metrics():
    width = ctypes.windll.user32.GetSystemMetrics(0)  # SM_CXSCREEN
    height = ctypes.windll.user32.GetSystemMetrics(1)  # SM_CYSCREEN
    cursor_width = ctypes.windll.user32.GetSystemMetrics(13)  # SM_CXCURSOR
    return width, height, cursor_width

# 5. Системные параметры
def get_system_parameters():
    SPI_GETMOUSESPEED = 0x0070
    SPI_GETSCREENSAVEACTIVE = 0x0010
    SPI_GETFOREGROUNDLOCKTIMEOUT = 0x2000

    mouse_speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETMOUSESPEED, 0, ctypes.byref(mouse_speed), 0)

    screen_saver = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETSCREENSAVEACTIVE, 0, ctypes.byref(screen_saver), 0)

    timeout = ctypes.c_uint()
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETFOREGROUNDLOCKTIMEOUT, 0, ctypes.byref(timeout), 0)

    return mouse_speed.value, screen_saver.value, timeout.value

# 6. Работа с цветами
def handle_colors():
    indexes = [win32con.COLOR_3DDKSHADOW, win32con.COLOR_BTNTEXT, win32con.COLOR_ACTIVECAPTION]
    old_colors = [win32gui.GetSysColor(idx) for idx in indexes]

    return old_colors

# 7. Время: GetSystemTime, GetTimeZoneInformation, EnumCalendarInfo
def get_time_info():
    # GetSystemTime
    system_time = win32api.GetSystemTime()

    # GetTimeZoneInformation
    tz_info = win32api.GetTimeZoneInformation()

    # EnumCalendarInfo — используем модуль calendar
    month_names = list(calendar.month_name[1:])  # Январь - Декабрь
    return system_time, tz_info, month_names

# 8. Дополнительные WinAPI-функции
def extra_api_functions():
    layout = win32api.GetKeyboardLayout(0)  # Получение раскладки
    locale.setlocale( locale.LC_ALL, '' )
    curr = locale.currency(18851898218, grouping=True)
    currency = curr.replace('\xa0', ',')
    error_code = win32api.GetLastError()
    converted = ctypes.create_string_buffer(100)
    ctypes.windll.user32.OemToCharA(b"HELLO", converted)
    return hex(layout), currency, error_code, converted.value.decode()

# Запуск всех функций
if __name__ == "__main__":
    print("1. Имя компьютера и пользователя:", get_user_info())
    print("2. Пути к системным каталогам:", get_system_paths())
    print("3. Версия ОС:", get_os_version())
    print("4. Системные метрики (ширина, высота, шир. курсора):", get_system_metrics())
    print("5. Системные параметры:", get_system_parameters())

    old_colors = handle_colors()
    print("6. Старые цвета:", old_colors)

    st, tz, months = get_time_info()
    print("7. Системное время:", st)
    print("   Временная зона:", tz)
    print("   Названия месяцев:", months)

    print("8. Дополнительные API-функции:", extra_api_functions())
