# from fractions import Fraction

# def calculate_xbox_probability_fraction(rows, cols):
#     """
#     Вычисляет вероятность покупки Xbox в виде несократимой дроби.

#     Args:
#         rows: Количество рядов.
#         cols: Количество мест в ряду.

#     Returns:
#         Вероятность покупки Xbox в виде несократимой дроби.
#     """

#     dp = [[Fraction(0, 1)] * cols for _ in range(rows)]

#     # Базовые случаи
#     for j in range(cols):
#         dp[rows - 1][j] = Fraction(1, 1)  # Вероятность 1, если достигнут последний ряд

#     for i in range(rows):
#         dp[i][cols - 1] = Fraction(0, 1)  # Вероятность 0, если достигнуто последнее место

#     # Заполнение таблицы DP
#     for i in range(rows - 2, -1, -1):
#         for j in range(cols - 2, -1, -1):
#             dp[i][j] = (
#                 Fraction(i + 1, i + j + 2) * dp[i + 1][j]
#                 + Fraction(j + 1, i + j + 2) * dp[i][j + 1]
#             )
#             print(dp[i][j])
#         print("\nNew Gate!\n")
#     return dp[0][0]

# # Пример использования
# rows = 10
# cols = 16
# probability = calculate_xbox_probability_fraction(rows, cols)

# print(f"Вероятность покупки Xbox: {probability}")

import math

def gcd(a, b):
    """Вычисляет наибольший общий делитель (НОД) двух чисел."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Вычисляет наименьшее общее кратное (НОК) двух чисел."""
    return (a * b) // gcd(a, b)

def lcm_of_array(numbers):
    """Вычисляет НОК массива чисел."""
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

def generate_and_print_lcms(count):
    """generate+print NOK."""
    for i in range(count):
        numbers = list(range(i + 1, i + 11))  # Генерируем массив k, k+1, ..., k+9
        result = lcm_of_array(numbers)
        print(f"For numbers = {numbers}, NOK = {result}")

# Пример использования: выводим 4 результата
generate_and_print_lcms(10)