"""
Задание 3. Агрегация.

Среди подозрительных событий засветилось несколько пользовательских ID.
Нужно понять, сколько их было, сколько уникальных и кто «наследил» больше
всех.
"""


def analyze_activity(user_ids: list[str]) -> tuple[dict[str, int], int, str]:
    """
    По списку user_ids (одно действие - один id пользователя в списке)
    вернуть кортеж из трёх элементов:

      1. словарь {user: количество действий этого пользователя};
      2. количество уникальных пользователей;
      3. id пользователя с наибольшим количеством действий.

    Если максимум количества действий делят несколько пользователей,
    вернуть того из них, кто раньше всех встретился в user_ids (по индексу
    первого появления в списке).

    Пример:
        analyze_activity(["a", "b", "a"]) -> ({"a": 2, "b": 1}, 2, "a")
    """
    user_trace = {}
    max_user = ""

    for user in user_ids:
        #unique processing included here
        if user not in user_trace:
            user_trace[user] = 0
        user_trace[user] += 1
        
    unique_count = len(user_trace)
    
    for user in user_ids:
        if user_trace[user] > user_trace.get(max_user, 0):
            max_user = user

    return user_trace, unique_count, max_user


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task3_users.txt", encoding="utf-8") as f:
        user_ids = [line.strip() for line in f if line.strip()]

    counts, unique_count, top_user = analyze_activity(user_ids)
    print("Счётчики:", counts)
    print("Уникальных пользователей:", unique_count)
    print("Больше всего действий у:", top_user)
