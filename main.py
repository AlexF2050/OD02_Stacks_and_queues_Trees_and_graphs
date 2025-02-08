import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph:
    def __init__(self):  # Конструктор
        self.graph = {}  # словарь для хранения графа

    def add_edge(self, u, v):  # u - вершина, v - ребро
        if u not in self.graph:  # если u не входит в словарь
            self.graph[u] = []  # добавляем u в словарь
        self.graph[u].append(v)  # добавляем v в ребро u

    def print_graph(self):  # Вывод графа
        for node in self.graph:  # перебираем словарь
            print(node, "->", " -> ".join(map(str, self.graph[node])))  # вывод графа циклом цикла

    def visualize_graph(self, labels, positions):
        G = nx.DiGraph()  # Создаем направленный граф
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        # Рассчитываем расстояния между узлами
        edge_labels = {}
        for u, v in G.edges():
            distance = np.linalg.norm(np.array(positions[u]) - np.array(positions[v]))
            edge_labels[(u, v)] = f'{distance:.1f} px'

        # Определяем позиции узлов
        pos = positions

        # Рисуем граф
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=700, node_color='lightblue', arrowsize=20)

        # Добавляем расстояния на граф
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        plt.title("Graph Visualization")
        plt.show()

# Создаем граф
g = Graph()

# Добавляем ребра
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Выводим граф
g.print_graph()

# Определяем метки для узлов
node_labels = {0: 'Москва', 1: 'Питер', 2: 'Томск', 3: 'Омск', 4: 'Тула'}

# Определяем позиции узлов в пикселях
node_positions = {
    0: (100, 150),
    1: (200, 250),
    2: (300, 100),
    3: (400, 300),
    4: (500, 200)
}

# Визуализируем граф с расстояниями
# g.visualize_graph(node_labels, node_positions)