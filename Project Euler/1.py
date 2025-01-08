"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


def calculate_sum_of_multiples(multiple_1: int, multiple_2: int, max_number: int) -> int:
    """
    Находит сумму всех натуральных чисел меньше max_number, которые кратны multiple_1 или multiple_2.

    :param multiple_1: Первое кратное число.
    :param multiple_2: Второе кратное число.
    :param max_number: Максимальное натуральное число (не включается).
    :return: Сумма чисел, кратных multiple_1 или multiple_2.
    """
    result = 0
    for i in range(1, max_number):
        if i % multiple_1 == 0 or i % multiple_2 == 0:
            result += i
    return result  # Ответ: 233168


if __name__ == "__main__":
    print(calculate_sum_of_multiples(3, 5, 1000))
