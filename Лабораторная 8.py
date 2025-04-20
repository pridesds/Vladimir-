# TODO  Напишите функцию count_letters


# TODO Напишите функцию calculate_frequency

from collections import OrderedDict

def count_letters_in_order(text): #Вывожу функцию подсчёта кол-ва каждой буквы
    letter_count = OrderedDict()
    for char in text.lower():  #Текст по нижнему регистру
        if char.isalpha():  #Функция определения является ли символ буквой
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def calculate_frequency(letter_count): #Вывожу функцию подсчёта частоты каждой буквы
    total_letters = sum(letter_count.values())  #Общее количество букв
    frequency = OrderedDict()
    for letter, count in letter_count.items():
        frequency[letter] = count / total_letters  #Вычисляю частоту
    return frequency

# Основной текст
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_count = count_letters_in_order(main_str) #Подсчёт букв

frequency = calculate_frequency(letter_count) #Определение частоты

for letter, freq in frequency.items(): #Вывод букв и частота их появления по порядку в тексте
    print(f"{letter}: {freq:.2f}")