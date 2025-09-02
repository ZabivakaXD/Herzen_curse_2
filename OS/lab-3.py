import ctypes
import matplotlib.pyplot as plt

class MEMORYSTATUS(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("dwTotalPhys", ctypes.c_ulong),
        ("dwAvailPhys", ctypes.c_ulong),
        ("dwTotalPageFile", ctypes.c_ulong),
        ("dwAvailPageFile", ctypes.c_ulong),
        ("dwTotalVirtual", ctypes.c_ulong),
        ("dwAvailVirtual", ctypes.c_ulong)
    ]

def get_memory_status():
    memory_status = MEMORYSTATUS()
    memory_status.dwLength = ctypes.sizeof(MEMORYSTATUS)
    ctypes.windll.kernel32.GlobalMemoryStatus(ctypes.byref(memory_status))
    return memory_status

def draw_memory_chart(mem):
    labels = ['Total Phys', 'Avail Phys', 'Total Virtual', 'Avail Virtual']
    values = [
        mem.dwTotalPhys / (1024**2),
        mem.dwAvailPhys / (1024**2),
        mem.dwTotalVirtual / (1024**2),
        mem.dwAvailVirtual / (1024**2)
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
    plt.ylabel('MB')
    plt.title('GlobalMemoryStatus - Память в системе')
    for i, v in enumerate(values):
        plt.text(i, v + 50, f'{v:.0f} MB', ha='center')

    plt.tight_layout()
    plt.show()

mem = get_memory_status()
draw_memory_chart(mem)

import ctypes
import ctypes.wintypes as wintypes
import psutil

# Константы WinAPI
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
MEM_COMMIT = 0x1000

# Структура MEMORY_BASIC_INFORMATION
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),
        ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", wintypes.DWORD),
        ("RegionSize", ctypes.c_size_t),
        ("State", wintypes.DWORD),
        ("Protect", wintypes.DWORD),
        ("Type", wintypes.DWORD)
    ]

# Получение карты виртуальной памяти одного процесса
def get_virtual_memory_map(pid):
    entries = []
    try:
        h_process = ctypes.windll.kernel32.OpenProcess(
            PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
            False,
            pid
        )
        if not h_process:
            return ["  [!] Не удалось открыть процесс."]

        mbi = MEMORY_BASIC_INFORMATION()
        addr = 0
        while ctypes.windll.kernel32.VirtualQueryEx(
            h_process, ctypes.c_void_p(addr),
            ctypes.byref(mbi), ctypes.sizeof(mbi)
        ):
            if mbi.State == MEM_COMMIT:
                line = (
                    f"  Адрес: {hex(mbi.BaseAddress)} | "
                    f"Размер: {mbi.RegionSize / 1024:.0f} KB | "
                    f"Защита: {mbi.Protect}"
                )
                entries.append(line)
            addr += mbi.RegionSize
        ctypes.windll.kernel32.CloseHandle(h_process)
        return entries
    except Exception as e:
        return [f"  Ошибка: {e}"]

# Главная функция: записывает всё в файл
def generate_memory_map_report(filename="memory_map.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for proc in psutil.process_iter(['pid', 'name']):
            pid = proc.info['pid']
            name = proc.info.get('name', 'Неизвестно')
            f.write(f"\n=== PID: {pid} | Процесс: {name} ===\n")
            entries = get_virtual_memory_map(pid)
            for entry in entries:
                f.write(entry + "\n")
    print(f"Карта виртуальной памяти сохранена в файл: {filename}")

# Запуск
generate_memory_map_report()
