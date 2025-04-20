# TODO Напишите функцию для поиска индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
# Функция для поиска индекса первого вхождения товара в списке
def find_item_index(items_list, item): #Функция определения индекса товара в списке

    if item in items_list: #Проверка наличия товара в перечне
        return items_list.index(item)  #Возвращаю индекс первого
    else:
        return None  #Возвращаю None, если товар не найден

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] #Список товаров

for find_item in ['банан', 'груша', 'персик']: #Поиск товаров в списке

    index_item = find_item_index(items_list, find_item) #Поиск индекса

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")