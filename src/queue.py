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
        self.all = []
        self.head = None

    def enqueue(self, data: str) -> None:
        """ Метод для добавления элемента в очередь
            :param data: данные, которые будут добавлены в очередь """
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
            self.all.append(data)
        else:
            self.tail.next_node = node
            self.tail = node
            self.all.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        return "\n".join(self.all)
