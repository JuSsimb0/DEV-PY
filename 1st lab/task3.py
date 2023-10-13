list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_of_players = len(list_players)
size_of_team = count_of_players // 2
first_team = list_players[:size_of_team]
second_team = list_players[size_of_team:]
print(first_team)
print(second_team)