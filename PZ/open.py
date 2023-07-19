import subprocess

# Путь к первому скрипту
script1_path = "conv.py"
# Путь ко второму скрипту
script2_path = "conn.py"

input_file_name = "logi.txt"
csv_file = "out.csv"

# Запуск первого скрипта через терминал
subprocess.call(["python", script1_path, input_file_name, csv_file])
subprocess.call(["python", script2_path])

# Запуск второго скрипта
# exec(open(script2_path).read())

print("Программа завершена")