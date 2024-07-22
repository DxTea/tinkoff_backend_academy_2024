def is_even_socks(n, socks):
    if sum(socks) % 2 == 0:
        return "YES"
    return "NO"


def main():
    n = int(input().strip())
    socks = [int(sock) for sock in input().strip().split()]
    result = is_even_socks(n, socks)
    print(f"{result}")


if __name__ == "__main__":
    main()

# Тестовые случаи:
# def test_is_even_socks():
#     assert is_even_socks(1, [0]) == "YES"
#     assert is_even_socks(2, [2, 2]) == "YES"
#     assert is_even_socks(5, [0, 3, 4, 4, 2]) == "NO"
#     assert is_even_socks(3, [1, 1, 1]) == "NO"
#     assert is_even_socks(4, [2, 2, 2, 2]) == "YES"
#     assert is_even_socks(1, [1]) == "NO"
#     assert is_even_socks(1, [2]) == "YES"
#     assert is_even_socks(6, [1, 1, 1, 1, 1, 1]) == "YES"
#     assert is_even_socks(0, []) == "YES"
#
# test_is_even_socks()
