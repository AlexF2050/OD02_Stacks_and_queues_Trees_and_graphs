# Напишем код с использованием графов

# Начнем с создания класса, который назовём Graph,
# и добавим метод инициализации, конструктор класса.
# В нём создаём словарь для хранения графа:

class Graph:                                       # Класс графа
   def __init__(self):                             # Конструктор
       self.graph = {}                             # словарь для хранения графа

   def add_edge(self, u, v):                       # u - вершина, v - ребро
       if u not in self.graph:                     # если u не входит в словарь
           self.graph[u] = []                      # добавляем u в словарь
       self.graph[u].append(v)                     # добавляем v в ребро u

   def print_graph(self):                          # Вывод графа
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]} # словарь для хранения графа
       for node in self.graph:                     # перебираем словарь
           print(node, "->", " -> ".join(map(str, self.graph[node]))) # вывод графа циклом цикла

g = Graph()                                        # создаём граф

g.add_edge(0, 1)                             # 0 - вершина, 1 - ребро
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()                                    # вывод графа





