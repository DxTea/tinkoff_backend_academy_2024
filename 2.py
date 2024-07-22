def find_free_days(input_data):
    days = [0] * 28
    week_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    for i, week in enumerate(input_data):
        for day in week.split():
            days[i * 7 + week_days.index(day)] = 1
    max_length = max_start = max_end = start = 0
    for i, day in enumerate(days):
        if day == 1:
            if i - start > max_length:
                max_length = i - start
                max_start = start
                max_end = i
            start = i + 1
    if 28 - start > max_length:
        max_start = start
        max_end = 28
    if max_length == 0 and days[-1] == 0:
        return start+1, 28
    elif max_start == max_end:
        return 0, 0
    else:
        return max_start + 1, max_end


def main():
    weeks = [input() for _ in range(4)]
    start, end = find_free_days(weeks)
    print(f"{start} {end}")


if __name__ == "__main__":
    main()

# # Тестовые случаи:
# print(find_free_days(['MON', 'MON', 'MON', 'MON SAT']))  # Вывод: (2, 7)
# print(find_free_days(['', 'TUE MON']))  # Вывод: (10, 28)
# print(find_free_days(['', '', '', '']))  # Вывод: (1, 28)
# print(find_free_days(['MON THU SAT SUN FRI TUE WED', 'SUN TUE MON FRI THU SAT WED', 'FRI THU WED SAT MON SUN TUE',
#                       'WED MON THU SAT TUE FRI SUN']))  # Вывод: (0, 0)
# print("_____________________")
# # Тест 1: Все дни недели заняты, кроме воскресенья
# print(1,find_free_days(['MON TUE WED THU FRI SAT', '', '', '']))  # Вывод: (7, 28)
#
# # # Тест 2: Все дни недели заняты, кроме понедельника
# print(2,find_free_days(['TUE WED THU FRI SAT SUN', '', '', '']))  # Вывод: (8, 28)
#
# # Тест 3: Все дни недели заняты в первую и последнюю неделю, но свободны во вторую и третью
# print(3,find_free_days(['MON TUE WED THU FRI SAT SUN', '', '', 'MON TUE WED THU FRI SAT SUN']))  # Вывод: (8, 21)
#
# # Тест 4: Все дни недели заняты в первую и третью неделю, но свободны во вторую и четвертую
# print(4,find_free_days(['MON TUE WED THU FRI SAT SUN', '', 'MON TUE WED THU FRI SAT SUN', '']))  # Вывод: (8, 14)
#
# # Тест 5: Все дни недели свободны, кроме понедельника и воскресенья
# print(5,find_free_days(['MON SUN', 'MON SUN', 'MON SUN', 'MON SUN']))  # Вывод: (2, 6)
# # Тест 6: Все дни недели заняты в первую и вторую неделю, но свободны в третью и четвертую
# print(6,find_free_days(['MON TUE WED THU FRI SAT SUN', 'MON TUE WED THU FRI SAT SUN', '', '']))  # Вывод: (15, 28)
# # Тест 7: Все дни недели заняты в первую и четвертую неделю, но свободны во вторую и третью
# print(7,find_free_days(['MON TUE WED THU FRI SAT SUN', '', '', 'MON TUE WED THU FRI SAT SUN']))  # Вывод: (8, 21)
#
# # Тест 8: Все дни недели заняты в первую и вторую неделю, но свободны в третью и четвертую
# print(8,find_free_days(['MON TUE WED THU FRI SAT SUN', 'MON TUE WED THU FRI SAT SUN', '', '']))  # Вывод: (15, 28)
#
# # Тест 9: Все дни недели заняты в первую неделю, но свободны во вторую, третью и четвертую
# print(9,find_free_days(['MON TUE WED THU FRI SAT SUN', '', '', '']))  # Вывод: (8, 28)
#
# # Тест 10: Все дни недели заняты в четвертую неделю, но свободны в первую, вторую и третью
# print(10,find_free_days(['', '', '', 'MON TUE WED THU FRI SAT SUN']))  # Вывод: (1, 22)
#
# # Тест 11: Все дни недели заняты во вторую и четвертую неделю, но свободны в первую и третью
# print(11,find_free_days(['', 'MON TUE WED THU FRI SAT SUN', '', 'MON TUE WED THU FRI SAT SUN']))  # Вывод: (8, 14)
#
# # Тест 12: Все дни недели заняты в первую и третью неделю, но свободны во вторую и четвертую
# print(12,find_free_days(['MON TUE WED THU FRI SAT SUN', '', 'MON TUE WED THU FRI SAT SUN', '']))  # Вывод: (8, 14)
# print(13,find_free_days(['', 'MON', 'MON', 'MON']))  # Вывод: (1, 7)
# print(14,find_free_days(['', 'SUN MON', 'MON', 'MON']))  # Вывод: (2, 28)
