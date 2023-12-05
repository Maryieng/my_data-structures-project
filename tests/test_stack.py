from src.stack import Node, Stack


def test_node():
    node1 = Node(1, None)
    assert node1.data == 1
    assert node1.next_node is None

    node2 = Node(2, node1)
    assert node2.data == 2
    assert node2.next_node == node1


def test_stack():
    stack = Stack()
    assert stack.top is None

    stack.push(1)
    assert stack.top.data == 1
    assert stack.top.next_node is None

    stack.push(2)
    assert stack.top.data == 2
    assert stack.top.next_node.data == 1

    popped_data = stack.pop()
    assert popped_data == 2
    assert stack.top.data == 1

    stack.push(3)
    assert stack.top.data == 3
    assert stack.top.next_node.data == 1

    popped_data = stack.pop()
    assert popped_data == 3
    assert stack.top.data == 1

    popped_data = stack.pop()
    assert popped_data == 1
    assert stack.top is None

    popped_data = stack.pop()
    assert popped_data is None

    assert str(Stack()) == 'None'
