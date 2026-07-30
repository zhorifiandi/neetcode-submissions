class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hashmap = {}

    def get(self, key: int) -> int:
        print(self.hashmap.keys())
        node = self._getNode(key)
        if node is None:
            return -1
        
        self._moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        existingNode = self._getNode(key)
        if existingNode:
            self._moveToHead(existingNode)
            existingNode.value = value
            return
        
        newNode = Node(key, value)
        self._appendHead(newNode)
        self.hashmap[key] = newNode

        if len(self.hashmap) > self.capacity:
            self._popTail()


        return
    
    def _getNode(self, key):
        if key in self.hashmap:
            return self.hashmap[key]
        
        return None
    
    def _moveToHead(self, node):
        self._deleteNode(node)
        self._appendHead(node)
    
    def _appendHead(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        
        if self.tail is None:
            self.tail = node
        
        node.prev = None
        self.head = node
    
    def _deleteNode(self, node):
        if node == self.head:
            self.head = node.next
        
        if node == self.tail:
            self.tail = node.prev

        prevNode = node.prev
        nextNode = node.next
        node.prev = None
        node.next = None
        
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode

    def _popTail(self):
        if self.tail:
            del self.hashmap[self.tail.key]
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail


        
