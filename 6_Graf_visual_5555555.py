import matplotlib.pyplot as plt
import networkx as nx

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

    def visualize_graph(self):
        G = nx.DiGraph()  # Создаем направленный граф
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G)  # Определяем позиции узлов
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrowsize=20)
        plt.title("Graph Visualization")
        plt.show()


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
g.visualize_graph()