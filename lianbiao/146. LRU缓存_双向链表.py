'''
这道题 是非常经典的双链表使用 训练情况。
在这道题里： 充分使用了双链表的删除，插入。
需要知道的是双链表的插入，删除是非常简单的，就是O(1)，因为它不需要遍历
但是同时它的维护，也就是插入或者删除时，需要多一倍的操作，
就是建立自己和前后的联系，以及前后与自己建立联系，两遍。


同时，也可以看到数据结构是为人服务的，不是靠死记硬背才能写出来的。
当实际需求需要我们建立字典的时候，就要构建对应的字典，这个字典的构建就是我们自己定义的。
在这道题中，我们定义的字典是 key:Node类型的。
'''
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_value = dict()

    def get_node(self, key):
        if key not in self.key_to_value:
            return None
        node = self.key_to_value[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_value[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key_to_value) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_value[back_node.key]
            self.remove(back_node)

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x
