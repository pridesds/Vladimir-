# TODO решите задачу

import json
def task() -> float: #Решение
    with open('input.json', 'r') as file: #Чтение данных из json
        data = json.load(file)

    total_sum = sum(item["score"] * item["weight"] for item in data) #Вычисление суммы произведений

    return round(total_sum, 3) #Округление результатов до 3х знаков

print(task()) #Печать результата