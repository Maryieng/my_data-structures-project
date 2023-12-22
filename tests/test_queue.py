from src.queue import Queue


def test_queue():
    assert str(Queue()) == ""
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    assert queue.head.data == 'data1'
    assert queue.head.next_node.data == 'data2'
    assert queue.tail.data == 'data3'
    assert queue.tail.next_node is None

    assert str(queue) == "data1\ndata2\ndata3"


def test_dequeue_removes_element():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    assert queue.dequeue() == 'data1'
    assert queue.dequeue() == 'data2'
    assert queue.dequeue() == 'data3'
    assert queue.dequeue() is None
