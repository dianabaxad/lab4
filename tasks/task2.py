def generate_function_values(a: float, b: float, func, step: float = 0.01):
    """
    Генератор значений функции f(x) на интервале [a; b] с заданным шагом.

    Args:
        a (float): Начало интервала
        b (float): Конец интервала
        func (callable): Функция f(x)
        step (float): Шаг изменения x

    Yields:
        tuple: (x, f(x)) - значение аргумента и функции
    """
    try:
        # Проверка корректности входных данных
        if a > b:
            raise ValueError("Начало интервала (a) не может быть больше конца (b)")

        if step <= 0:
            raise ValueError("Шаг должен быть положительным числом")

        if not callable(func):
            raise ValueError("func должен быть вызываемым объектом (функцией)")

        x = a
        while x <= b + step/2:  # Добавляем step/2 для учета погрешности округления
            try:
                yield (x, func(x))
            except Exception as e:
                raise ValueError(f"Ошибка при вычислении f({x}): {e}")
            x += step

    except Exception as e:
        raise ValueError(f"Ошибка в генераторе значений функции: {e}")