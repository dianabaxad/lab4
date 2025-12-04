def generate_combinations(digits: str = "0123456789", length: int = 3):
    """
    Генератор всех сочетаний из трех цифр.

    Args:
        digits (str): Строка с цифрами
        length (int): Длина сочетаний

    Yields:
        int: Очередное сочетание как целое число
    """
    try:
        if not digits or length <= 0:
            return

        # Проверяем, что все символы - цифры
        if not all(c.isdigit() for c in digits):
            raise ValueError("Строка должна содержать только цифры")

        from itertools import permutations

        # Используем set для исключения дубликатов
        seen = set()
        for perm in permutations(digits, length):
            # Преобразуем кортеж в строку, затем в число
            num_str = ''.join(perm)
            if num_str[0] == '0':  # Пропускаем числа с ведущими нулями
                continue

            num = int(num_str)
            if num not in seen:
                seen.add(num)
                yield num

    except Exception as e:
        raise ValueError(f"Ошибка в генераторе сочетаний: {e}")