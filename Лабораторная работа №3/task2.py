def find_common_participants(first, second, separator=","):
    participants1 = set(first.split(separator))
    participants2 = set(second.split(separator))
    common_participants = participants1.intersection(participants2)
    return sorted(list(common_participants))



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
