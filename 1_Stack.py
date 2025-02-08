# Программа для реализации стека на Python, используя классы и списки для создания стека

# Создание класса
class Stack:
   def __init__(self):                  # Конструктор класса
       self.items = []                  # Создание списка циклическим ссылочным типом для хранения элементов стека

   def is_empty(self):                  # Проверка на пустоту стека
       return self.items == []          # Проверка на пустоту списка циклическим ссылочным типом

   def push(self, item):                # Добавление элемента в стек
       self.items.append(item)          # Добавление элемента в список

   def pop(self):                       # Удаление верхнего элемента из стека
       return self.items.pop()          # Удаление верхнего элемента из списка

   def peek(self):                      # Получение верхнего элемента из стека
       return self.items[-1]            # Получение верхнего элемента из списка items (-1 - первый с конца=последний элемент)

# Создаем объекта класса Stack, который также называем Stack:
stack = Stack()

print(stack.is_empty())                 # Проверка на пустоту стека - True - стек пуст

stack.push(1)                           # Добавление элемента в стек
stack.push(2)                           # Добавление элемента в стек
stack.push(3)                           # Добавление элемента в стек

print(stack.is_empty())                 # Проверка на пустоту стека - False - стек НЕ пуст

print(stack.peek())                     # Получение верхнего элемента из стека
