def find_common_participants(first_list, second_list, separator=','):
    first_set = set(first_list.split(sep=separator))
    second_set = set(second_list.split(sep=separator))
    common_list = first_set.intersection(second_set)
    common_list = list(common_list)
    common_list.sort()
    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(
    f"Список общих участников : {find_common_participants(participants_first_group, participants_second_group, separator='|')}")
