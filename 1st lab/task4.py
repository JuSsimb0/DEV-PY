users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

session_log = {
    "Общее количество":0,
    "Уникальные посещения":0
}

session_log["Общее количество"] = len(users)
session_log["Уникальные посещения"] = len(set(users))

print(session_log)
