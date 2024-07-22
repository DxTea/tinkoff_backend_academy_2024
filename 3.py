def lcg(e, a, m):
    return (a * e + 11) % m


def generator(seed, a, m):
    while True:
        seed = lcg(seed, a, m)
        yield (abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8


def count_coins(n, k, a, m):
    gen = generator(0, a, m)
    coins = 0
    candies = 0
    total = 0
    while candies < n:
        coin = next(gen)
        total += coin
        coins += 1
        while total >= 3 * k:
            buy, total = divmod(total, 3)
            if buy < k:
                break
            candies += buy
    return coins


def main():
    try:
        n, k, a, m = map(int, input().split())
        result = count_coins(n, k, a, m)
        print(f"{result}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

# # Тестовые случаи:
# print(count_coins(4, 3, 252149039, 281474977))  # Вывод: 4
# print(count_coins(1, 1, 252149039, 281474977))  # Вывод: 2
# print(count_coins(3, 1000, 252149039, 281474977))  # Вывод: 1102
