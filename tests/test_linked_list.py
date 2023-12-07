import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_isinstance(self):
        linked_list = LinkedList()
        self.assertIsInstance(linked_list, LinkedList)

    def test_init(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.list, [])
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_insert(self):
        linked_list = LinkedList()

        linked_list.insert_beginning({'id': 1})
        self.assertEqual(linked_list.head.data, {'id': 1})
        self.assertEqual(linked_list.tail.data, {'id': 1})

        linked_list.insert_beginning({'id': 0})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 1})

        linked_list.insert_at_end({'id': 3})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 3})

        linked_list.insert_at_end({'id': 4})
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 4})

    def test_to_load(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1, 'name': 'Nina'})
        linked_list.insert_at_end({'id': 2, 'name': 'Lina'})
        self.assertEqual(
            linked_list.to_list(),
            ["{'id': 1, 'name': 'Nina'}", "{'id': 2, 'name': 'Lina'}"]
        )

        data = linked_list.to_list()
        self.assertEqual(
            data,
            ["{'id': 1, 'name': 'Nina'}", "{'id': 2, 'name': 'Lina'}"]
        )

    def test_get_data_by_id(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'id': 1, 'name': 'Nina'})
        linked_list.insert_at_end({'id': 2, 'name': 'Lina'})
        self.assertEqual(linked_list.get_data_by_id(2), {'id': 2, 'name': 'Lina'})

    def test_str(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')

        linked_list.insert_beginning({'id': 1})
        linked_list.insert_beginning({'id': 0})

        self.assertEqual(str(linked_list), "{'id': 0} -> {'id': 1} -> None")
