from collections import defaultdict


def determine_soldier_order(num_soldiers, height_pairs):
    adj = defaultdict(list)
    for taller, shorter in height_pairs:
        adj[taller].append(shorter)

    visited = [0] * (num_soldiers + 1)
    order = []

    def dfs(soldier):
        visited[soldier] = 1
        for other_soldier in adj[soldier]:
            if visited[other_soldier] == 1:
                return False
            elif visited[other_soldier] == 0 and not dfs(other_soldier):
                return False
        visited[soldier] = 2
        order.append(soldier)
        return True

    for soldier in range(1, num_soldiers + 1):
        if visited[soldier] == 0 and not dfs(soldier):
            return []
    return order[::-1]


def main():
    try:
        num_soldiers, num_pairs = map(int, input().split())
        height_pairs = [tuple(map(int, input().split())) for _ in range(num_pairs)]
        result = determine_soldier_order(num_soldiers, height_pairs)
        if not result:
            print("No")
        else:
            print("Yes")
            print(' '.join(map(str, result)))
    except ValueError:
        print("Invalid input. Please enter the correct format.")


if __name__ == "__main__":
    main()

# # Тестовые случаи:
# print(determine_soldier_order(2, [(1, 2), (2, 1)]))  # Вывод: ("No", [])
# print(determine_soldier_order(3, [(1, 2), (2, 3), (1, 3), (2, 3), (1, 2), (1, 2), (1, 3)]))  # Вывод: ("Yes", [1, 2, 3])
# # Тестовый случай 1:
# # В этом случае, каждый солдат выше следующего в строю. Поэтому, они могут стоять в строю в порядке 1, 2, 3, 4.
# print(determine_soldier_order(4, [(1, 2), (2, 3), (3, 4), (1, 4)]))  # Вывод: ("Yes", [1, 2, 3, 4])
#
# # Тестовый случай 2:
# # В этом случае, образуется цикл, где каждый солдат выше следующего, но последний солдат также выше первого, что является противоречием.
# print(determine_soldier_order(5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]))  # Вывод: ("No", [])
#
# # Тестовый случай 3:
# # В этом случае, образуется цикл, где каждый солдат выше следующего, но последний солдат также выше первого, что является противоречием.
# print(determine_soldier_order(3, [(1, 2), (3, 2), (3, 1)]))  # Вывод: ("No", [])
#
# # Тестовый случай 4:
# # В этом случае, каждый солдат выше следующего в строю. Поэтому, они могут стоять в строю в порядке 1, 2, 3, 4, 5.
# print(determine_soldier_order(5, [(1, 2), (2, 3), (3, 4), (4, 5)]))  # Вывод: ("Yes", [1, 2, 3, 4, 5])
#
# # Тестовый случай 5:
# # В этом случае, образуется цикл, где каждый солдат выше следующего, но последний солдат также выше первого, что является противоречием.
# print(determine_soldier_order(6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]))  # Вывод: ("No", [])
# print(determine_soldier_order(3, [(1, 3), (2, 3)]))  # Вывод: ("No", [])
