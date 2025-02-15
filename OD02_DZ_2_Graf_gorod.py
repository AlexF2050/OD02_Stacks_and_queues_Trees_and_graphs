# Эта программа реализует простой направленный граф с помощью класса `Graph` на Python,
# используя библиотеки `matplotlib` и `networkx` для визуализации.

import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):  # Конструктор
        self.graph = {}  # словарь для хранения графа
        self.distances = {}  # словарь для хранения расстояний

    def add_edge(self, u, v, distance):  # u - вершина, v - ребро
        if u not in self.graph:  # если u не входит в словарь
            self.graph[u] = []  # добавляем u в словарь
        self.graph[u].append(v)  # добавляем v в ребро u
        self.distances[(u, v)] = distance  # добавляем расстояние для ребра

    def print_graph(self):  # Вывод графа
        for node in self.graph:  # перебираем словарь
            edges = " -> ".join(f"{neighbor}({self.distances[(node, neighbor)]})" for neighbor in self.graph[node])
            print(f"{node} -> {edges}")  # вывод графа с расстояниями

    def visualize_graph(self, labels):
        G = nx.DiGraph()  # Создаем направленный граф
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G)  # Определяем позиции узлов
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=700, node_color='lightblue', arrowsize=20)
        edge_labels = {(u, v): d for (u, v), d in self.distances.items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Graph Visualization")
        plt.show()

# Создаем граф
g = Graph()

# Добавляем ребра с расстояниями
g.add_edge(0, 1, 10)
g.add_edge(0, 4, 15)
g.add_edge(1, 2, 12)
g.add_edge(1, 3, 13)
g.add_edge(1, 4, 5)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, 8)

# Выводим граф
g.print_graph()

# Определяем метки для узлов
node_labels = {0: 'Москва', 1: 'Питер', 2: 'Томск', 3: 'Омск', 4: 'Тула'}

# Визуализируем граф
g.visualize_graph(node_labels)

# Эта программа реализует простой направленный граф с помощью класса `Graph` на Python, используя библиотеки `matplotlib` и `networkx` для визуализации. Вот краткое описание и суть программы:
#
# 1. **Класс `Graph`:**
#    - Инициализирует две структуры данных: `graph`, представляющую сам граф в виде словаря, и `distances`, хранящую условные расстояния между узлами.
#    - Метод `add_edge` добавляет ребро между двумя узлами (вершинами) `u` и `v` и сохраняет расстояние между ними.
#    - Метод `print_graph` выводит текстовое представление графа, показывая узлы и их соединения с указанием расстояния между ними.
#    - Метод `visualize_graph` визуализирует граф, используя `networkx` для построения графа и `matplotlib` для его отображения. Узлы отображаются с метками, а ребра — с аннотациями расстояний.
#
# 2. **Использование:**
#    - Создается объект класса `Graph`.
#    - В граф добавляются ребра с условными расстояниями между узлами, которые представляют города.
#    - Граф выводится в консоль в текстовом формате с указанием расстояний.
#    - Граф визуализируется с помощью `matplotlib`, где узлы подписаны названиями городов, а на ребрах указаны расстояния.
#
# 3. **Назначение и Суть:**
#    - Программа демонстрирует, как можно создавать и визуализировать направленный граф с использованием Python.
#    - Она подходит для простых приложений, где необходимо представить связи между объектами (например, города и дороги между ними) и показать расстояния между этими объектами.
#    - Пример иллюстрирует базовые принципы работы с графами и их визуализацией, что полезно для изучения алгоритмов графов и их приложений в реальных задачах.