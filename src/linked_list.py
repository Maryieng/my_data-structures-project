from typing import Any


class Node:
    """ Класс для узла односвязного списка """

    def __init__(self, data: dict, next_node) -> None:
        """ Конструктор класса Node """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.list = []  # type: ignore

    def insert_beginning(self, data: dict) -> None:
        """ Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка """
        new_node = Node(data, self.head)
        self.head = new_node  # type: ignore
        if not self.tail:
            self.tail = new_node  # type: ignore

    def insert_at_end(self, data: dict) -> None:
        """ Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка """
        new_node = Node(data, None)
        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
        elif self.head is not None:
            self.head.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node  # type: ignore

    def to_list(self) -> Any:
        """ возвращает список с данными, содержащимися в односвязном списке """
        node = self.head
        if node is None:
            return str(None)
        result = []
        while node:
            result.append(str(node.data))
            node = node.next_node
        return result

    def get_data_by_id(self, id_user: Any) -> Any:
        """ возвращает первый найденный в LinkedList словарь с ключом 'id',
         значение которого равно переданному в метод значению """
        node = self.head
        if node is None:
            return str(None)
        while node:
            try:
                if node.data['id'] == id_user:
                    return node.data
                node = node.next_node
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
                node = node.next_node
                if node is None:
                    break

    def __str__(self) -> str:
        """ Вывод данных односвязного списка в строковом представлении """
        node = self.head
        if node is None:
            return str(None)
        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node
        ll_string += 'None'
        return ll_string
