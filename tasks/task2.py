class Task2:
    """Класс для выполнения задания №2"""

    def __init__(self):
        self.a = -20
        self.b = 100
        self.step = 0.01

    def function_generator(self, a, b, f):
        """Генератор значений функции f(x) для x∈[a;b] с шагом 0.01"""
        try:
            x = a
            while x <= b + 0.0001:  # Добавляем небольшую погрешность для float
                yield f(x)
                x = round(x + self.step, 2)  # Округляем для избежания ошибок плавающей точки
        except ZeroDivisionError:
            yield float('inf')
        except Exception as e:
            raise Exception(f"Ошибка в генераторе функций: {e}")

    def get_function_values(self, function_str=None, num_values=20):
        """Получает значения функции"""
        try:
            # Определяем функцию по умолчанию или пользовательскую
            if function_str:
                # Пытаемся создать функцию из строки
                try:
                    f = eval(f"lambda x: {function_str}")
                except:
                    f = lambda x: -1.5 * x + 2  # Функция по умолчанию
            else:
                f = lambda x: -1.5 * x + 2  # Функция по умолчанию

            # Создаем генератор
            gen = self.function_generator(self.a, self.b, f)

            # Получаем значения
            results = []
            count = 0

            for value in gen:
                results.append(value)
                count += 1
                if count >= num_values:
                    break

            return results, f
        except Exception as e:
            raise Exception(f"Ошибка при получении значений функции: {e}")

    def update_parameters(self, a, b, step=0.01):
        """Обновляет параметры"""
        try:
            self.a = float(a)
            self.b = float(b)
            self.step = float(step)
            return True
        except ValueError:
            raise Exception("Некорректные значения параметров")