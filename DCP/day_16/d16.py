class Node:
        """gamer time"""
        def __init__(self, order_id, previous = None, next = None):
            self.order_id = order_id
            self.prev = previous
            self.next = next

class log:
    """think I'm doing this right"""

    def __init__(self):
        self.head = None
        self.tail = None

    def record(self, order_id):
        temp = Node(order_id)
        if (self.head == None): 
            head = tail = temp
        else:
            temp.prev = tail
            tail.next = temp
            tail = temp
    
    def get_last(self, i):
        temp = self.tail
        for _ in range(i-1):
            temp = temp.prev
        return temp.order_id

pog = log()
pog.record(1)
print(pog.get_last(1))
