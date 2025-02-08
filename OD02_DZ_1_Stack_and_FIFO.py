# Программа демонстрирует базовые операции и принципы работы стека и очереди,
# которые являются фундаментальными структурами данных. е
# Визуализация помогает лучше понять внутреннее устройство и динамику изменений этих структур данных.

import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def visualize_stack(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.title("Визуализация стека")
        ax.bar(range(len(self.stack)), self.stack, color='lightblue', label='Элемент стека')
        ax.invert_yaxis()
        ax.set_xticks(range(len(self.stack)))
        ax.set_xticklabels(self.stack)
        ax.set_xlabel("Элементы стека")
        ax.set_ylabel("Значение")
        ax.legend()

        # Добавление рамки и текста справа
        explanation = (
            "Объяснение:\n"
            "- Класс Stack: реализует стек с методами push, pop и is_empty. "
            "Метод visualize_stack используется для визуализации текущего состояния стека.\n"
            "- Визуализация: мы используем matplotlib для отображения состояния стека. "
            "Стек отображается в виде столбцов, перевернутых по оси Y, чтобы показать,\n"
            "  что элементы добавляются и удаляются сверху."
        )
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(1.05, 0.5, explanation, transform=ax.transAxes, fontsize=10,
                verticalalignment='center', bbox=props, wrap=True)

        plt.subplots_adjust(right=0.75)  # Увеличение правого отступа для текста
        plt.show()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def visualize_queue(self):
        fig, ax = plt.subplots(figsize=(15, 5))
        plt.title("Визуализация очереди")
        ax.bar(range(len(self.queue)), self.queue, color='lightgreen', label='Элемент очереди')
        ax.set_xticks(range(len(self.queue)))
        ax.set_xticklabels(self.queue)
        ax.set_xlabel("Элементы очереди")
        ax.set_ylabel("Значение")
        ax.legend()

        # Добавление рамки и текста справа
        explanation = (
            "Объяснение:\n"
            "- Класс Queue: реализует очередь с методами enqueue, dequeue и is_empty. "
            "Метод visualize_queue используется для визуализации текущего состояния очереди.\n"
            "- Визуализация: мы используем matplotlib для отображения состояния очереди. "
            "Очередь отображается в виде столбцов, где элементы добавляются справа и удаляются слева."
        )
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(1.05, 0.5, explanation, transform=ax.transAxes, fontsize=10,
                verticalalignment='center', bbox=props, wrap=True)

        plt.subplots_adjust(right=0.75)  # Увеличение правого отступа для текста
        plt.show()

# Пример использования стека
s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.visualize_stack()
s.pop()
s.visualize_stack()

# Пример использования очереди
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.visualize_queue()
q.dequeue()
q.visualize_queue()

# Пояснение:
# 1. **Класс `Stack`:**
#    - **Инициализация:** Создает пустой стек в виде списка.
#    - **Методы:**
#      - `push(item)`: Добавляет элемент `item` на вершину стека.
#      - `pop()`: Удаляет и возвращает элемент с вершины стека, если стек не пуст.
#      - `is_empty()`: Проверяет, пуст ли стек.
#      - `visualize_stack()`: Визуализирует текущее состояние стека в виде перевернутой гистограммы, чтобы отразить принцип добавления и удаления элементов сверху.
#
# 2. **Класс `Queue`:**
#    - **Инициализация:** Создает пустую очередь в виде списка.
#    - **Методы:**
#      - `enqueue(item)`: Добавляет элемент `item` в конец очереди.
#      - `dequeue()`: Удаляет и возвращает элемент из начала очереди, если очередь не пуста.
#      - `is_empty()`: Проверяет, пуста ли очередь.
#      - `visualize_queue()`: Визуализирует текущее состояние очереди в виде гистограммы, показывая, что элементы добавляются справа и удаляются слева.
#
# 3. **Визуализация:**
#    - Оба класса используют `matplotlib` для графического представления. Визуализация показывает элементы в виде столбцов, с метками и пояснением, как работают стек и очередь.
#    - Для стека элементы отображаются в перевернутом порядке по оси Y, чтобы показать, что они добавляются и удаляются сверху.
#    - Для очереди элементы добавляются справа и удаляются слева, что отражает принцип "первый вошел — первый вышел".
