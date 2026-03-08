list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2  # Количество игроков в каждой команде без остатка

first_team = list_players[:middle_index]  # Первая половина игроков
second_team = list_players[middle_index:]  # Вторая половина игроков

print(first_team)  # Список первой команды
print(second_team)  # Список второй команды
