"""
Задание 1: Генератор комбинаций из трех цифр.
"""

from typing import Iterator
from itertools import product


def generate_combinations(digits: str = "0123456789", length: int = 3) -> Iterator[int]:
    """
    Генератор всех трехзначных чисел из заданных цифр.

    Args:
        digits: Строка с цифрами
        length: Длина чисел (по умолчанию 3)

    Yields:
        Целые трехзначные числа

    Raises:
        ValueError: Если строка содержит не только цифры или слишком короткая
        RuntimeError: При других ошибках выполнения
    """
    try:
        # Проверяем, что все символы - цифры
        if not digits.isdigit():
            raise ValueError("Строка должна содержать только цифры")

        # Проверяем длину
        if len(digits) < length:
            raise ValueError(f"Длина строки должна быть не менее {length}")

        # Генерируем все комбинации длины length С ПОВТОРЕНИЯМИ
        for combo in product(digits, repeat=length):
            # Для трехзначных чисел первая цифра не может быть 0
            # if combo[0] == '0':
                # continue

            # Преобразуем кортеж символов в строку, затем в число
            try:
                yield int(''.join(combo))
            except ValueError as e:
                raise ValueError(f"Ошибка преобразования комбинации в число: {e}")

    except Exception as e:
        raise RuntimeError(f"Ошибка в генераторе комбинаций: {e}")


def generate_unique_combinations(digits: str = "0123456789", length: int = 3) -> Iterator[int]:
    """
    Генератор уникальных комбинаций без повторений цифр.
    (альтернативный вариант, если нужны именно сочетания без повторений)
    """
    from itertools import combinations

    try:
        if not digits.isdigit():
            raise ValueError("Строка должна содержать только цифры")

        if len(digits) < length:
            raise ValueError(f"Длина строки должна быть не менее {length}")

        # Генерируем комбинации БЕЗ повторений цифр
        for combo in combinations(digits, length):
            # Для трехзначных чисел первая цифра не может быть 0
            if combo[0] == '0':
                continue

            try:
                # Получаем все перестановки этой комбинации
                from itertools import permutations
                for perm in permutations(combo):
                    if perm[0] == '0':
                        continue
                    yield int(''.join(perm))
            except ValueError as e:
                raise ValueError(f"Ошибка преобразования комбинации в число: {e}")

    except Exception as e:
        raise RuntimeError(f"Ошибка в генераторе комбинаций: {e}")


def get_first_n_combinations(n: int = 50, with_repetitions: bool = True) -> list:
    """
    Получить первые N комбинаций.

    Args:
        n: Количество комбинаций для возврата
        with_repetitions: Если True - с повторениями цифр,
                         если False - только уникальные цифры в числе

    Returns:
        Список первых N комбинаций
    """
    result = []
    count = 0

    generator = generate_combinations() if with_repetitions else generate_unique_combinations()

    for value in generator:
        if count >= n:
            break
        result.append(value)
        count += 1
    return result


def format_combinations_output(combinations: list, per_line: int = 10) -> str:
    """
    Форматирует список комбинаций для вывода.

    Args:
        combinations: Список комбинаций
        per_line: Количество комбинаций на строку

    Returns:
        Отформатированная строка
    """
    lines = []
    for i in range(0, len(combinations), per_line):
        line = combinations[i:i+per_line]
        line_str = ", ".join(str(x) for x in line)
        lines.append(line_str)
    return "\n".join(lines)


def get_combinations_count(with_repetitions: bool = True) -> int:
    """
    Вычисляет общее количество возможных комбинаций.

    Args:
        with_repetitions: Если True - с повторениями цифр,
                         если False - только уникальные цифры

    Returns:
        Количество возможных комбинаций
    """
    digits = "0123456789"
    length = 3

    if with_repetitions:
        # С повторениями: 9 * 10 * 10 = 900
        # Первая цифра: 1-9 (9 вариантов)
        # Вторая и третья: 0-9 (10 вариантов каждая)
        return 9 * 10 * 10
    else:
        # Без повторений: P(10,3) - P(9,2) = 720 - 72 = 648
        # Все перестановки 3 цифр из 10: P(10,3) = 10*9*8 = 720
        # Минус те, что начинаются с 0: P(9,2) = 9*8 = 72
        from math import perm
        return perm(10, 3) - perm(9, 2)