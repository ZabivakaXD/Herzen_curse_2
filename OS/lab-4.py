import ctypes
import ctypes.wintypes as wintypes
import psutil

# Константы
PROCESS_ALL_ACCESS = 0x1F0FFF
DUPLICATE_SAME_ACCESS = 0x00000002
kernel32 = ctypes.windll.kernel32

# Файл для отчёта
report_file = "report.txt"

with open(report_file, "w", encoding="utf-8") as f:
    # 1. Получение текущего PID
    pid = kernel32.GetCurrentProcessId()
    f.write(f"[1] Текущий PID: {pid}\n")
    
    # 2. Получение псевдодескриптора процесса
    pseudo_handle = kernel32.GetCurrentProcess()
    f.write(f"[2] Псевдодескриптор процесса: {pseudo_handle}\n")
    
    # 3. Дублирование дескриптора
    # Сначала получаем реальный дескриптор через OpenProcess
    real_handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    current_process_handle = wintypes.HANDLE()
    
    if real_handle:
        success = kernel32.DuplicateHandle(
            real_handle,           # hSourceProcessHandle - реальный дескриптор
            real_handle,           # hSourceHandle - тот же дескриптор
            real_handle,           # hTargetProcessHandle - целевой процесс
            ctypes.byref(current_process_handle),  # lpTargetHandle
            0,                     # dwDesiredAccess
            False,                 # bInheritHandle
            DUPLICATE_SAME_ACCESS  # dwOptions
        )
        # Закрываем временный дескриптор
        kernel32.CloseHandle(real_handle)
    else:
        success = False
    
    if success:
        f.write(f"[3] Дубликат дескриптора процесса: {current_process_handle.value}\n")
    else:
        error_code = kernel32.GetLastError()
        f.write(f"[3] Ошибка при DuplicateHandle: {error_code}\n")
    
    # 4. Открытие процесса по PID
    open_handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if open_handle:
        f.write(f"[4] OpenProcess дескриптор: {open_handle}\n")
    else:
        error_code = kernel32.GetLastError()
        f.write(f"[4] Ошибка при OpenProcess: {error_code}\n")
    
    # 5. Закрытие дубликата
    if success and current_process_handle.value:  # Проверяем success И значение дескриптора
        kernel32.CloseHandle(current_process_handle)
        f.write("[5] Закрыт дубликат дескриптора.\n")
    else:
        f.write("[5] Дубликат дескриптора не был создан или уже закрыт.\n")
    
    # 6. Закрытие дескриптора OpenProcess
    if open_handle:
        kernel32.CloseHandle(open_handle)
        f.write("[6] Закрыт дескриптор OpenProcess.\n")
    else:
        f.write("[6] Дескриптор OpenProcess не был создан.\n")
    
    # 7. Перечисление всех процессов, потоков и модулей
    f.write("\n[7] Перечисление всех процессов, потоков и модулей:\n\n")
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            f.write(f"Процесс: {proc.info['name']} | PID: {proc.info['pid']}\n")
            p = psutil.Process(proc.info['pid'])
            
            # Потоки процесса
            try:
                threads = p.threads()
                for thread in threads:
                    f.write(f"  └─ Поток TID: {thread.id} | Время: {thread.system_time:.2f}s\n")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                f.write("  └─ [!] Нет доступа к потокам процесса.\n")
            
            # Загруженные модули (DLL)
            f.write("  └─ Модули:\n")
            try:
                memory_maps = p.memory_maps()
                dll_count = 0
                for dll in memory_maps:
                    if '.dll' in dll.path.lower():
                        f.write(f"     - {dll.path}\n")
                        dll_count += 1
                        if dll_count > 10:  # Ограничиваем вывод для читаемости
                            f.write(f"     - ... и ещё {len(memory_maps) - dll_count} модулей\n")
                            break
                if dll_count == 0:
                    f.write("     - Нет доступных DLL модулей\n")
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                f.write("     - [!] Нет доступа к модулям процесса.\n")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            f.write("  [!] Нет доступа к процессу или он завершён.\n")
            continue
        
        f.write("\n")  # Пустая строка между процессами для читаемости

print(f"Отчёт сохранён в файл: {report_file}")