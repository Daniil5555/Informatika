items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  # Список товаров
def find(list, product):  # Зададим в функции два аргумента: список и товар
    for i in range(len(list)):  # Пусть будет перебор количества товаров в списке
        if list[i] == product:  # Если товар есть в списке,то возвращаем индекс первого вхождения:
            return i  # Иначе возвращаем
for find_item in ['банан', 'груша', 'персик']: # product
    index_item = find(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None: # При отсутствии индекса
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
