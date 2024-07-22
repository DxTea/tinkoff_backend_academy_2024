from collections import deque

INFINITY = 1e9


def update_stack(min_actions_prev, platform_stack, j):
    while platform_stack and min_actions_prev[platform_stack[-1]] > min_actions_prev[j]:
        platform_stack.pop()
    platform_stack.append(j)
    return platform_stack


def min_platform_actions(track_length, num_tracks, platform_positions):
    platform_start, platform_end = zip(*platform_positions)
    min_actions_prev = [0] * (track_length + 1)
    min_actions_curr = [0] * (track_length + 1)

    for i in range(platform_start[0] - 1, 0, -1):
        min_actions_prev[i] = platform_start[0] - i
    for i in range(platform_end[0] + 1, track_length + 1):
        min_actions_prev[i] = i - platform_end[0]

    for i in range(1, num_tracks):
        min_val = INFINITY
        platform_stack = deque()

        for j in range(platform_start[i], platform_end[i] + 1):
            min_val = min(min_val, min_actions_prev[j])
            platform_stack = update_stack(min_actions_prev, platform_stack, j)

        for j in range(platform_end[i] + 1, track_length + 1):
            while platform_stack and platform_stack[0] <= j - (platform_end[i] - platform_start[i] + 1):
                platform_stack.popleft()
            platform_stack = update_stack(min_actions_prev, platform_stack, j)
            min_actions_curr[j] = j - platform_end[i] + min_actions_prev[platform_stack[0]]

        platform_stack.clear()
        for j in range(platform_end[i], platform_start[i] - 1, -1):
            platform_stack = update_stack(min_actions_prev, platform_stack, j)

        for j in range(platform_start[i] - 1, 0, -1):
            while platform_stack and platform_stack[0] >= j + (platform_end[i] - platform_start[i] + 1):
                platform_stack.popleft()
            platform_stack = update_stack(min_actions_prev, platform_stack, j)
            min_actions_curr[j] = platform_start[i] - j + min_actions_prev[platform_stack[0]]

        for j in range(platform_start[i], platform_end[i] + 1):
            min_actions_curr[j] = min_val
        min_actions_prev, min_actions_curr = min_actions_curr, [0] * (track_length + 1)

    min_total_actions = min(min_actions_prev[1:])
    return min_total_actions


def main():
    try:
        track_length, num_tracks = map(int, input().split())
        platform_positions = [list(map(int, input().split())) for _ in range(num_tracks)]
        result = min_platform_actions(track_length, num_tracks, platform_positions)
        print(f"{result}")
    except ValueError:
        print("Invalid input. Please enter the correct format.")


if __name__ == "__main__":
    main()

# # Тестовые случаи:
# print(min_platform_actions(7, 5, [(1, 4), (2, 3), (6, 7), (2, 2), (4, 7)]))  # Вывод: 5
# print(min_platform_actions(5, 3, [(1, 2), (2, 3), (4, 5)]))  # Вывод: 1
# print(min_platform_actions(10, 2, [(1, 5), (6, 10)]))  # Вывод: 1
# print(min_platform_actions(3, 3, [(1, 1), (2, 2), (3, 3)]))  # Вывод: 2
# print(min_platform_actions(1, 1, [(1, 1)]))  # Вывод: 0
# print(min_platform_actions(8, 4, [(1, 2), (3, 4), (5, 6), (7, 8)]))  # Вывод: 4
# print(min_platform_actions(6, 3, [(1, 2), (2, 3), (4, 5)]))  # Вывод: 1
# print(min_platform_actions(12, 2, [(1, 6), (7, 12)]))  # Вывод: 1
# print(min_platform_actions(4, 4, [(1, 1), (2, 2), (3, 3), (4, 4)]))  # Вывод: 4
# print(min_platform_actions(2, 2, [(1, 1), (2, 2)]))  # Вывод: 1
