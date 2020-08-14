class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
        #[a=>b=>c=>d=>h=>j=>l=>n]
        #a, none
        #b, a
        #c, b
        #d, c
        #h, d
        #j, h
        #l, j
        #n, l
        #none, n
        #[a<=b<=c<=d<=h<=j<=l<=n]
    def reverse_list(self, node, prev):
        if node != None:
            change = node.get_next()
            node.set_next(prev)
            self.reverse_list(change, node)  
        else:
            self.head = prev

classmake = LinkedList()
classmake.add_to_head(2)
classmake.add_to_head(5)
classmake.add_to_head(4)
print(classmake.head.value)
classmake.reverse_list(classmake.head,None)
print(classmake.head.value)