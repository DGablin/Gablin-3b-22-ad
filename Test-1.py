# Написать программу, которая находит все уникальные комбинации элементов
# заданного списка, таких, что их сумма равна заданному числу.
# Основная функция find_combinations поиска комбинаций. Принимает на вход список чисел и сумму которая должна получиться
# Вызывает рекурсивную функцию
def find_combinations(original, num):
    results = []  # Создает список, в который будут добавляться правильные комбинации
    find_rec(original, num, [], results)  # Первый вызов рекурсивной функции
    return results

# рекурсивная функция. Принимает на вход оригинальный массив, сумму, которая должна получиться. Текущий набор чисел
# и список наборов, который уже был обработан и подходит


def find_rec(original, num, current, results):
    if sum(current) > num:  # Стоп рекурсии, когда сумма текущего набора чисел больше, чем нужно
        return 1
    if sum(current) == num:  # Стоп рекурсии, когда сумма текущего набора чисел равна искомой сумме
        results.append(list(current))
        return 1

    # Перебрать элементы списка original по индексу i:
    # Добавить original[i] к текущей комбинации current.
    # Рекурсивно вызвать функцию с обновленными аргументами
    # Удалить последний добавленный элемент из текущей комбинации current, чтобы пробовать другие комбинации.
    for i in range(len(original)):
        current.append(original[i])
        find_rec(original[i+1:], num, current, results)
        current.pop()


nums = input("Введите числа через пробел: ").split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
flag = int(input("Введите число: "))
result = find_combinations(nums, flag)
print(result)
