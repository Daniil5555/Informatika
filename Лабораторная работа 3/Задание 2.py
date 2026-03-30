# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"  # Группа участников 1
participants_second_group = "Петров|Сидоров|Смирнов"  # Группа участников 2
def find_common_participants(group_1, group_2, sep = "," ): # Запишем функцию, введя новые аргументы, и запишем переменную для разделения
    list_1 = set(group_1.split(sep))  # Пусть список для 1 группы найдет уникальные элементы в группе и заменит на запятую
    list_2 = set(group_2.split(sep))  # Пусть список для 2 группы найдет уникальные элементы в группе и заменит на запятую
    common = list_1.intersection(list_2)  # Найдем одинаковых участников групп 1 и 2
    result = list(common)  # Создадим список из участников
    result.sort()  # Отсортируем список участников
    return result  # Возвратим результат
print(find_common_participants(participants_first_group, participants_second_group))



# TODO Провеьте работу функции с разделителем отличным от запятой
