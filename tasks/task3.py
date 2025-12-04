def get_sort(dictionary: dict) -> list:
    """
    Сортирует словарь по убыванию ключей и возвращает список значений.
    
    Args:
        dictionary (dict): Входной словарь
        
    Returns:
        list: Список значений, отсортированных по убыванию ключей
        
    Raises:
        ValueError: Если входные данные некорректны
    """
    try:
        # Проверка типа входных данных
        if not isinstance(dictionary, dict):
            raise ValueError("Входной параметр должен быть словарем")
        
        if not dictionary:
            return []
        
        # Сортируем ключи в обратном порядке (убывание)
        sorted_keys = sorted(dictionary.keys(), reverse=True)
        
        # Возвращаем значения в соответствии с отсортированными ключами
        return [dictionary[key] for key in sorted_keys]
        
    except Exception as e:
        raise ValueError(f"Ошибка при сортировке словаря: {e}")