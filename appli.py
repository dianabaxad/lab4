from PySide6.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QTextEdit, QPushButton, QLabel, QSpinBox,
    QDoubleSpinBox, QHBoxLayout, QGroupBox,
    QScrollArea, QFrame, QGridLayout
)
from PySide6.QtCore import Qt
import tasks


class TaskTab(QWidget):
    """Базовый класс для вкладок с задачами"""
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

    def add_widget(self, widget):
        self.layout.addWidget(widget)

    def add_layout(self, layout):
        self.layout.addLayout(layout)


class Task1Tab(TaskTab):
    """Вкладка для задачи 1"""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Заголовок
        title = QLabel("Задача 1: Генератор сочетаний из трех цифр")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.add_widget(title)

        # Параметры
        params_layout = QHBoxLayout()

        params_layout.addWidget(QLabel("Цифры:"))
        self.digits_edit = QTextEdit("0123456789")
        self.digits_edit.setMaximumHeight(60)
        params_layout.addWidget(self.digits_edit)

        params_layout.addWidget(QLabel("Длина:"))
        self.length_spin = QSpinBox()
        self.length_spin.setRange(1, 5)
        self.length_spin.setValue(3)
        params_layout.addWidget(self.length_spin)

        params_layout.addWidget(QLabel("Количество:"))
        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 1000)
        self.count_spin.setValue(50)
        params_layout.addWidget(self.count_spin)

        self.add_layout(params_layout)

        # Кнопки
        button_layout = QHBoxLayout()

        self.generate_btn = QPushButton("Сгенерировать")
        self.generate_btn.clicked.connect(self.generate)
        button_layout.addWidget(self.generate_btn)

        self.clear_btn = QPushButton("Очистить")
        self.clear_btn.clicked.connect(self.clear_output)
        button_layout.addWidget(self.clear_btn)

        self.add_layout(button_layout)

        # Вывод результатов
        output_group = QGroupBox("Результаты")
        output_layout = QVBoxLayout()

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)

        output_group.setLayout(output_layout)
        self.add_widget(output_group)

    def generate(self):
        try:
            digits = self.digits_edit.toPlainText().strip()
            length = self.length_spin.value()
            count = self.count_spin.value()

            # Проверяем, что все символы - цифры
            if not all(c.isdigit() for c in digits):
                raise ValueError("Строка должна содержать только цифры")

            generator = tasks.generate_combinations(digits, length)

            results = []
            for i, num in enumerate(generator, 1):
                results.append(f"{i:3d}. {num}")
                if i >= count:
                    break

            self.output_text.setPlainText('\n'.join(results))

        except Exception as e:
            self.output_text.setPlainText(f"Ошибка: {str(e)}")

    def clear_output(self):
        self.output_text.clear()


class Task2Tab(TaskTab):
    """Вкладка для задачи 2"""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Заголовок
        title = QLabel("Задача 2: Генератор значений функции")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.add_widget(title)

        # Параметры функции
        params_group = QGroupBox("Параметры функции")
        params_layout = QGridLayout()

        # Интервал
        params_layout.addWidget(QLabel("Начало (a):"), 0, 0)
        self.a_spin = QDoubleSpinBox()
        self.a_spin.setRange(-1000, 1000)
        self.a_spin.setValue(-20.0)
        params_layout.addWidget(self.a_spin, 0, 1)

        params_layout.addWidget(QLabel("Конец (b):"), 1, 0)
        self.b_spin = QDoubleSpinBox()
        self.b_spin.setRange(-1000, 1000)
        self.b_spin.setValue(100.0)
        params_layout.addWidget(self.b_spin, 1, 1)

        params_layout.addWidget(QLabel("Шаг:"), 2, 0)
        self.step_spin = QDoubleSpinBox()
        self.step_spin.setRange(0.001, 10)
        self.step_spin.setSingleStep(0.01)
        self.step_spin.setValue(0.01)
        self.step_spin.setDecimals(3)
        params_layout.addWidget(self.step_spin, 2, 1)

        # Функция
        params_layout.addWidget(QLabel("Функция f(x):"), 3, 0)
        self.func_edit = QTextEdit("lambda x: -1.5 * x + 2")
        self.func_edit.setMaximumHeight(60)
        params_layout.addWidget(self.func_edit, 3, 1)

        params_layout.addWidget(QLabel("Количество значений:"), 4, 0)
        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 1000)
        self.count_spin.setValue(20)
        params_layout.addWidget(self.count_spin, 4, 1)

        params_group.setLayout(params_layout)
        self.add_widget(params_group)

        # Кнопки
        button_layout = QHBoxLayout()

        self.generate_btn = QPushButton("Вычислить")
        self.generate_btn.clicked.connect(self.generate)
        button_layout.addWidget(self.generate_btn)

        self.clear_btn = QPushButton("Очистить")
        self.clear_btn.clicked.connect(self.clear_output)
        button_layout.addWidget(self.clear_btn)

        self.add_layout(button_layout)

        # Вывод результатов
        output_group = QGroupBox("Результаты")
        output_layout = QVBoxLayout()

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)

        output_group.setLayout(output_layout)
        self.add_widget(output_group)

    def generate(self):
        try:
            a = self.a_spin.value()
            b = self.b_spin.value()
            step = self.step_spin.value()
            count = self.count_spin.value()

            # Безопасное выполнение лямбда-функции
            func_str = self.func_edit.toPlainText().strip()
            if not func_str:
                raise ValueError("Функция не может быть пустой")

            # Ограниченное выполнение кода
            allowed_names = {}
            exec(f"func = {func_str}", {"__builtins__": {}}, allowed_names)
            func = allowed_names['func']

            if not callable(func):
                raise ValueError("Некорректная функция")

            generator = tasks.generate_function_values(a, b, func, step)

            results = []
            for i, (x, y) in enumerate(generator, 1):
                results.append(f"{i:3d}. x = {x:.4f}, f(x) = {y:.6f}")
                if i >= count:
                    break

            self.output_text.setPlainText('\n'.join(results))

        except Exception as e:
            self.output_text.setPlainText(f"Ошибка: {str(e)}")

    def clear_output(self):
        self.output_text.clear()


class Task3Tab(TaskTab):
    """Вкладка для задачи 3"""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Заголовок
        title = QLabel("Задача 3: Сортировка словаря по убыванию ключей")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.add_widget(title)

        # Ввод словаря
        input_group = QGroupBox("Входной словарь (JSON-формат)")
        input_layout = QVBoxLayout()

        self.dict_edit = QTextEdit()
        self.dict_edit.setPlainText(
            '{\n'
            '    "cat": "кот",\n'
            '    "horse": "лошадь",\n'
            '    "tree": "дерево",\n'
            '    "dog": "собака",\n'
            '    "book": "книга"\n'
            '}'
        )
        self.dict_edit.setMaximumHeight(200)
        input_layout.addWidget(self.dict_edit)

        input_group.setLayout(input_layout)
        self.add_widget(input_group)

        # Кнопки
        button_layout = QHBoxLayout()

        self.sort_btn = QPushButton("Отсортировать")
        self.sort_btn.clicked.connect(self.sort_dict)
        button_layout.addWidget(self.sort_btn)

        self.clear_btn = QPushButton("Очистить")
        self.clear_btn.clicked.connect(self.clear_output)
        button_layout.addWidget(self.clear_btn)

        self.add_layout(button_layout)

        # Вывод результатов
        output_group = QGroupBox("Результат сортировки")
        output_layout = QVBoxLayout()

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)

        output_group.setLayout(output_layout)
        self.add_widget(output_group)

    def sort_dict(self):
        try:
            import json
            dict_str = self.dict_edit.toPlainText().strip()

            if not dict_str:
                raise ValueError("Словарь не может быть пустым")

            # Пытаемся распарсить как JSON
            dictionary = json.loads(dict_str)

            if not isinstance(dictionary, dict):
                raise ValueError("Входные данные должны быть словарем")

            # Сортируем
            sorted_values = tasks.get_sort(dictionary)

            # Форматируем вывод
            results = []
            for i, value in enumerate(sorted_values, 1):
                results.append(f"{i:2d}. {value}")

            self.output_text.setPlainText('\n'.join(results))

        except json.JSONDecodeError as e:
            self.output_text.setPlainText(f"Ошибка JSON: {str(e)}")
        except Exception as e:
            self.output_text.setPlainText(f"Ошибка: {str(e)}")

    def clear_output(self):
        self.output_text.clear()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генераторы и встроенные функции Python")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет с вкладками
        self.tab_widget = QTabWidget()

        # Добавляем вкладки
        self.tab1 = Task1Tab()
        self.tab2 = Task2Tab()
        self.tab3 = Task3Tab()

        self.tab_widget.addTab(self.tab1, "Задача 1")
        self.tab_widget.addTab(self.tab2, "Задача 2")
        self.tab_widget.addTab(self.tab3, "Задача 3")

        self.setCentralWidget(self.tab_widget)