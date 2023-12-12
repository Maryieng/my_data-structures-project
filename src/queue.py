from typing import Any


class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node) -> None:
        """ Конструктор класса Node
            :param data: данные, которые будут храниться в узле """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.all = []  # type: ignore
        self.head = None

    def enqueue(self, data: str) -> None:
        """ Метод для добавления элемента в очередь
            :param data: данные, которые будут добавлены в очередь """
        node = Node(data, None)
        if self.head is None:
            self.head = node  # type: ignore
            self.tail = node
            self.all.append(data)
        else:
            self.tail.next_node = node
            self.tail = node
            self.all.append(data)

    def dequeue(self) -> Any:
        """ Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента """
        if len(self.all) > 1:
            self.head = self.head.next_node  # type: ignore
        elif len(self.all) == 1:
            self.head = None
            self.tail = None   # type: ignore
        else:
            return None
        return self.all.pop(0)

    def __str__(self) -> str:
        """ представления объекта"""
        return "\n".join(self.all)
