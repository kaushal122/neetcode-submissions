
class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def remove(slef,node:Node) -> None:
        node.prev.next=node.next
        node.next.prev=node.prev

    def adFront(self,node:Node) -> None:
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.adFront(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        node=Node(key,value)
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.adFront(node)
            return
        elif len(self.cache)==self.capacity:
            node=Node(key,value)
            temp=self.tail.prev
            self.remove(temp)
            del self.cache[temp.key]
        self.cache[key]=node
        self.adFront(node)

