# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, separator=','): #Функция поиска участников

    participants_group1 = set(group1.split(separator)) #Разделяю строки на списки фамилий
    participants_group2 = set(group2.split(separator))

    common_participants = participants_group1 & participants_group2 #Нахожу пересечение множеств

    return sorted(common_participants) #Возврат отсортированного списка участников

#Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator='/') #Проверка работы функции с разделителем, отличным от запятой (например, '/')

print("Общие участники:", common)