numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None) #Определение элемента None

sum_of_numbers = sum(x for x in numbers if x is not None) #Определение суммы чисел, кроме none

average = sum_of_numbers / len(numbers) #Определение ср.арифметического включая none

numbers[missing_index] = average #Замена none на определённое ср. арифметическое

numbers
print("Измененный список:",numbers) #Выведение всего ряда чисел