import ctypes
import ctypes.wintypes as wintypes
import os

# === Шаг 1. Создание текстового файла
filename = "example.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write("It is lab 2 of OS")  # Исходный текст

# === Шаг 2. Открытие файла через CreateFile
kernel32 = ctypes.windll.kernel32

GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
OPEN_EXISTING = 3
FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2

hFile = kernel32.CreateFileW(
    filename,
    GENERIC_READ | GENERIC_WRITE,
    FILE_SHARE_READ | FILE_SHARE_WRITE,
    None,
    OPEN_EXISTING,
    0,
    None
)

if hFile == -1:
    raise ctypes.WinError()

print(f"Дескриптор файла: {hFile}")

# === Шаг 3. Создание объекта отображения файла
PAGE_READWRITE = 0x04

hMap = kernel32.CreateFileMappingW(
    hFile,
    None,
    PAGE_READWRITE,
    0,
    0,
    None
)

if not hMap:
    raise ctypes.WinError()

# === Шаг 4. Отображение файла в память
FILE_MAP_ALL_ACCESS = 0xF001F

lpBaseAddress = kernel32.MapViewOfFile(
    hMap,
    FILE_MAP_ALL_ACCESS,
    0,
    0,
    0
)

if not lpBaseAddress:
    raise ctypes.WinError()

# === Чтение содержимого
length = os.path.getsize(filename)
buffer = (ctypes.c_char * length).from_address(lpBaseAddress)

original_text = buffer.raw.decode('utf-8')
print(f"Исходное содержимое файла: {original_text}")

# === Изменение регистра и запись обратно
modified_text = original_text.swapcase()
modified_bytes = modified_text.encode('utf-8')

# Перезаписываем память
ctypes.memmove(lpBaseAddress, modified_bytes, len(modified_bytes))
print(f"Изменённое содержимое файла: {modified_text}")

# === Шаг 5. Закрытие всех дескрипторов
kernel32.UnmapViewOfFile(lpBaseAddress)
kernel32.CloseHandle(hMap)
kernel32.CloseHandle(hFile)
