import random

class Node:
    data = None
    next_node = None 

    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return f"<Node data: {self.data}>" 


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1 
            current = current.next_node

        return count
    
    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def add(self,data):
       #Adds new node at tail
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.tail.next_node = new_node 
            self.tail = new_node
    
    def add_to_head(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self,data,index):
        if index == 0:
            self.add = data

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

        while position > 1:
            current = current.next_node
            position -= 1

        prev = current
        next = current.next_node

        prev.next_node = new
        new.next_node = next

    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True 
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
    
            previous = current
            current = current.next_node

        return current

    def sort(self):

        if self.head == None or self.head.next_node == None:
            return self.head

        mid = self.get_middle(self.head)
        nex_to_mid = mid.next_node
        mid.next_node = None   

        left = LinkedList()
        right= LinkedList()

        left.head = self.head
        right.head = nex_to_mid
        
        left.sort()
        right.sort()

        self.head = self.merge(left.head, right.head)


    def merge(self,left,right):
        if left == None:
            return right
        if right == None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next_node = self.merge(left.next_node , right)
        else:
            result = right
            result.next_node = self.merge(left, right.next_node)


        return result

    def get_middle(self, head):
        if self.head == None:
            return head
        
        slow = head
        fast = head.next_node 

        while fast.next_node and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node

        return slow
        


    def __repr__(self):
        
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head : {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail : {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node

        return '->'.join(nodes)

def main():
    l = LinkedList()
    for i in range(0,15):
        l.add(random.randint(0,40))
    
    print(l)
    l.sort()
    print(l)

    # data_delete = int(input())
    # print(l.remove(data_delete))

main()
