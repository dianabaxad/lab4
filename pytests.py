"""
Единый файл со всеми тестами для задач
"""

import pytest
import itertools
import json


# ==================== ФУНКЦИИ ЗАДАЧ ====================

def generate_combinations(digits: str = "0123456789", length: int = 3):
    """
    Генератор всех сочетаний из трех цифр.
    """
    try:
        if not digits or length <= 0:
            return

        if not all(c.isdigit() for c in digits):
            raise ValueError("Строка должна содержать только цифры")

        seen = set()
        for perm in itertools.permutations(digits, length):
            num_str = ''.join(perm)
            if num_str[0] == '0':
                continue

            num = int(num_str)
            if num not in seen:
                seen.add(num)
                yield num

    except Exception as e:
        raise ValueError(f"Ошибка в генераторе сочетаний: {e}")


def generate_function_values(a: float, b: float, func, step: float = 0.01):
    """
    Генератор значений функции f(x) на интервале [a; b] с заданным шагом.
    """
    try:
        if a > b:
            raise ValueError("Начало интервала (a) не может быть больше конца (b)")

        if step <= 0:
            raise ValueError("Шаг должен быть положительным числом")

        if not callable(func):
            raise ValueError("func должен быть вызываемым объектом (функцией)")

        x = a
        while x <= b + step / 2:
            try:
                yield (x, func(x))
            except Exception as e:
                raise ValueError(f"Ошибка при вычислении f({x}): {e}")
            x += step

    except Exception as e:
        raise ValueError(f"Ошибка в генераторе значений функции: {e}")


def get_sort(dictionary: dict) -> list:
    """
    Сортирует словарь по убыванию ключей и возвращает список значений.
    """
    try:
        if not isinstance(dictionary, dict):
            raise ValueError("Входной параметр должен быть словарем")

        if not dictionary:
            return []

        sorted_keys = sorted(dictionary.keys(), reverse=True)
        return [dictionary[key] for key in sorted_keys]

    except Exception as e:
        raise ValueError(f"Ошибка при сортировке словаря: {e}")


# ==================== ТЕСТЫ ЗАДАЧИ 1 ====================

class TestTask1:
    """Тесты для задачи 1"""

    def test_generate_combinations_basic(self):
        """Тест базовой функциональности"""
        digits = "012"
        generator = generate_combinations(digits, 2)

        results = list(generator)
        expected = [10, 12, 20, 21]

        assert sorted(results) == sorted(expected)

    def test_generate_combinations_first_5(self):
        """Тест первых 5 значений"""
        generator = generate_combinations("0123456789", 3)
        results = []

        for i, num in enumerate(generator, 1):
            results.append(num)
            if i >= 5:
                break

        # Проверяем, что все числа трехзначные
        assert all(100 <= num <= 999 for num in results)
        assert len(results) == 5

    def test_generate_combinations_invalid_digits(self):
        """Тест с некорректными цифрами"""
        with pytest.raises(ValueError):
            list(generate_combinations("012a", 3))

    def test_generate_combinations_empty_string(self):
        """Тест с пустой строкой"""
        generator = generate_combinations("", 3)
        assert list(generator) == []

    def test_generate_combinations_zero_length(self):
        """Тест с нулевой длиной"""
        generator = generate_combinations("012", 0)
        assert list(generator) == []

    def test_generate_combinations_no_leading_zeros(self):
        """Тест что числа не начинаются с нуля"""
        generator = generate_combinations("01", 2)
        results = list(generator)

        # Должен быть только 10, а не 01
        assert results == [10]

    def test_generate_combinations_unique_values(self):
        """Тест уникальности значений"""
        generator = generate_combinations("112", 2)
        results = list(generator)

        # Убираем дубликаты
        unique_results = list(set(results))
        assert len(results) == len(unique_results)

    def test_generate_combinations_specific_case(self):
        """Тест конкретного случая"""
        generator = generate_combinations("123", 2)
        results = sorted(list(generator))
        expected = [12, 13, 21, 23, 31, 32]

        assert results == expected


# ==================== ТЕСТЫ ЗАДАЧИ 2 ====================

class TestTask2:
    """Тесты для задачи 2"""

    def test_generate_function_values_linear(self):
        """Тест линейной функции"""
        func = lambda x: 2 * x + 1
        generator = generate_function_values(0, 1, func, 0.5)

        results = list(generator)
        expected = [(0.0, 1.0), (0.5, 2.0), (1.0, 3.0)]

        assert len(results) == len(expected)

        for (x1, y1), (x2, y2) in zip(results, expected):
            assert abs(x1 - x2) < 0.0001
            assert abs(y1 - y2) < 0.0001

    def test_generate_function_values_negative_step(self):
        """Тест с отрицательным шагом"""
        with pytest.raises(ValueError):
            list(generate_function_values(0, 1, lambda x: x, -0.1))

    def test_generate_function_values_invalid_interval(self):
        """Тест с некорректным интервалом"""
        with pytest.raises(ValueError):
            list(generate_function_values(10, 1, lambda x: x, 0.1))

    def test_generate_function_values_not_callable(self):
        """Тест с некорректируемой функцией"""
        with pytest.raises(ValueError):
            list(generate_function_values(0, 1, "not a function", 0.1))

    def test_generate_function_values_custom_function(self):
        """Тест с пользовательской функцией"""

        def square(x):
            return x * x

        generator = generate_function_values(0, 2, square, 1)
        results = list(generator)

        assert len(results) == 3
        assert results[0] == (0.0, 0.0)
        assert results[1] == (1.0, 1.0)
        assert results[2] == (2.0, 4.0)

    def test_generate_function_values_quadratic(self):
        """Тест квадратичной функции"""
        func = lambda x: x ** 2 - 2 * x + 1
        generator = generate_function_values(0, 2, func, 1)

        results = list(generator)
        assert len(results) == 3
        assert abs(results[0][1] - 1.0) < 0.0001  # f(0) = 1
        assert abs(results[1][1] - 0.0) < 0.0001  # f(1) = 0
        assert abs(results[2][1] - 1.0) < 0.0001  # f(2) = 1

    def test_generate_function_values_small_step(self):
        """Тест с малым шагом"""
        func = lambda x: x
        generator = generate_function_values(0, 0.1, func, 0.01)

        results = list(generator)
        assert len(results) == 11  # 0.00, 0.01, ..., 0.10

    def test_generate_function_values_assignment_example(self):
        """Тест примера из задания"""
        func = lambda x: -1.5 * x + 2
        generator = generate_function_values(-20, 100, func, 0.01)

        # Получаем первые 20 значений
        results = []
        for i, (x, y) in enumerate(generator, 1):
            results.append((x, y))
            if i >= 20:
                break

        assert len(results) == 20
        # Проверяем первое значение
        assert abs(results[0][0] - (-20.0)) < 0.0001
        assert abs(results[0][1] - (-1.5 * (-20) + 2)) < 0.0001


# ==================== ТЕСТЫ ЗАДАЧИ 3 ====================

class TestTask3:
    """Тесты для задачи 3"""

    def test_get_sort_basic(self):
        """Тест базовой функциональности"""
        d = {
            'cat': 'кот',
            'horse': 'лошадь',
            'tree': 'дерево',
            'dog': 'собака',
            'book': 'книга'
        }

        result = get_sort(d)
        expected = ['дерево', 'лошадь', 'собака', 'кот', 'книга']

        assert result == expected

    def test_get_sort_empty_dict(self):
        """Тест с пустым словарем"""
        result = get_sort({})
        assert result == []

    def test_get_sort_single_element(self):
        """Тест с одним элементом"""
        d = {'apple': 'яблоко'}
        result = get_sort(d)
        assert result == ['яблоко']

    def test_get_sort_not_dict(self):
        """Тест с некорректным типом данных"""
        with pytest.raises(ValueError):
            get_sort([1, 2, 3])

    def test_get_sort_mixed_keys(self):
        """Тест с ключами разного типа"""
        d = {
            'zebra': 'зебра',
            'apple': 'яблоко',
            'banana': 'банан'
        }

        result = get_sort(d)
        # Проверяем, что сортировка по убыванию
        assert result == ['зебра', 'банан', 'яблоко']

    def test_get_sort_numeric_keys(self):
        """Тест с числовыми ключами"""
        d = {
            3: 'три',
            1: 'один',
            2: 'два'
        }

        result = get_sort(d)
        # Ключи сортируются как числа
        assert result == ['три', 'два', 'один']

    def test_get_sort_mixed_case_keys(self):
        """Тест с ключами в разном регистре"""
        d = {
            'Apple': 'яблоко',
            'banana': 'банан',
            'apple': 'маленькое яблоко',
            'Banana': 'БАНАН'
        }

        result = get_sort(d)
        # Сортировка лексикографическая (по ASCII/Unicode)
        assert result[0] == 'банан'  # 'banana'

    def test_get_sort_large_dict(self):
        """Тест с большим словарем"""
        d = {str(i): f'value_{i}' for i in range(100, 0, -1)}

        result = get_sort(d)

        # Проверяем что первый элемент соответствует максимальному ключу
        assert result[0] == 'value_99'  # '99' > '9', '98', etc.

        # Проверяем количество элементов
        assert len(result) == 100