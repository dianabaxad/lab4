class Task1:
    """Класс для выполнения задания №1"""

    def __init__(self):
        self.d = "0123456789"

    def create_generator(self):
        """Создает генератор сочетаний из трех цифр"""
        try:
            # Генератор сочетаний из трех цифр
            for i in range(len(self.d)):
                for j in range(len(self.d)):
                    for k in range(len(self.d)):
                        # Преобразуем строку в целое число
                        yield int(self.d[i] + self.d[j] + self.d[k])
        except Exception as e:
            raise Exception(f"Ошибка в генераторе сочетаний: {e}")

    def get_first_n_values(self, n=50):
        """Получает первые N значений из генератора"""
        try:
            generator = self.create_generator()
            results = []
            count = 0

            for num in generator:
                results.append(num)
                count += 1
                if count >= n:
                    break

            return results, count
        except Exception as e:
            raise Exception(f"Ошибка при получении значений: {e}")