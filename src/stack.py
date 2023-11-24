class Node:
    """ Класс для узла стека"""

    def __init__(self, data, next_node):
        """ Конструктор класса Node"""
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data) -> None:
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        """ Метод для удаления элемента с вершины стека и его возвращения"""

        if self.top is None:
            return None
        popped_data = self.top.data
        self.top = self.top.next_node
        return popped_data
