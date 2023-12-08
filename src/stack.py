from typing import Any


class Node:
    """ Класс для узла стека"""

    def __init__(self, data, next_node) -> None:
        """ Конструктор класса Node"""
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """ отображение информации об объекте класса для пользователей """
        return f"{self.top}"

    def push(self, data) -> None:
        """ вывод следующей очереди """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self) -> Any:
        """ Метод для удаления элемента с вершины стека и его возвращения"""

        if self.top is None:
            return None
        popped_data = self.top.data
        self.top = self.top.next_node
        return popped_data
