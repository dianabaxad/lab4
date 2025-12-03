class Task3:
    """Класс для выполнения задания №3"""

    def __init__(self):
        self.default_dict = {
            'cat': 'кот',
            'horse': 'лошадь',
            'tree': 'дерево',
            'dog': 'собака',
            'book': 'книга'
        }
        self.additional_dict = {
            'zebra': 'зебра',
            'apple': 'яблоко',
            'banana': 'банан',
            'cherry': 'вишня',
            'date': 'финик'
        }

    def get_sort(self, dictionary):
        """Сортирует словарь по убыванию ключей и возвращает список значений"""
        try:
            if not isinstance(dictionary, dict):
                raise ValueError("На вход должен подаваться словарь")

            if not dictionary:
                return []

            # Сортируем ключи по убыванию и получаем соответствующие значения
            sorted_values = [dictionary[key] for key in sorted(dictionary.keys(), reverse=True)]
            return sorted_values

        except KeyError as e:
            raise Exception(f"Ключ {e} не найден в словаре")
        except Exception as e:
            raise Exception(f"Ошибка при сортировке словаря: {e}")

    def parse_dictionary_from_text(self, text):
        """Парсит словарь из текста"""
        try:
            if not text.strip():
                return {}

            # Пытаемся оценить как Python словарь
            try:
                return eval(text)
            except:
                # Парсим вручную из формата key:value
                result = {}
                lines = text.strip().split('\n')
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        result[key.strip().strip("'\"")] = value.strip().strip("'\"")
                return result
        except Exception as e:
            raise Exception(f"Ошибка при парсинге словаря: {e}")

    def dictionary_to_text(self, dictionary):
        """Преобразует словарь в читаемый текст"""
        if not dictionary:
            return "{}"

        result = []
        for key, value in dictionary.items():
            result.append(f"'{key}': '{value}'")
        return "{\n    " + ",\n    ".join(result) + "\n}"