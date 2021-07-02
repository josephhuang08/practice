class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def insert_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node
    
    def insert_to_end(self, data):
        new_node = Node(data)
        if self.start_node == None:
            self.start_node = new_node
        else:
            n = self.start_node
            while n.next != None:
                n = n.next
            n.next = new_node

    def insert_after_x(self, x, data):
        n = self.start_node
        while n != None:
            if n.val == x:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                break
            else:
                n = n.next

            if n == None:
                print(f'{x} is not in the list')

    def insert_before_x(self, x, data):
        n = self.start_node
        if n == None:
            print('List has no elements')
            return

        if x == self.start_node.val:
            self.insert_to_start(data)
            return

        while n.next != None:
            if n.next.val == x:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                break

            n = n.next
            if n.next == None:
                print(f'{x} is not in the list')
    
    def insert_at_index(self, i, data):
        n = self.start_node
        count = 0
        while n != None:
            #index is the last + 1 element in the list
            if n.next == None and count + 1 == i:
                self.insert_to_end(data)
                break
                
            if count == i:
                self.insert_before_x(n.val, data)
                break

            n = n.next
            count += 1

            if n == None:    
                print(f'index {count} is the end of list, cannot insert to index {i}')
    
    def length(self):
        n = self.start_node
        count = 0
        while n != None:
            count += 1
            n = n.next

        return count

    def search(self, x):
        n = self.start_node
        while n != None:
            if n.val == x:
                return True
            n = n.next

        return False
    
    def delete_at_start(self):
        if self.start_node == None:
            print('The list has no elements to delete')
        else:
            self.start_node = self.start_node.next

    def delete_at_end(self):
        if self.start_node == None:
            print('The list has no elements to delete')
        elif self.start_node.next == None:
            self.start_node = None
        else:
            n = self.start_node
            while n.next.next != None:
                n = n.next
            n.next = None
    
    def delete_x(self, x):
        if self.start_node == None:
            print('The list has no elements to delete')
        elif self.start_node.val == x:
            self.start_node = self.start_node.next
        else:
            n = self.start_node
            while n.next != None:
                if n.next.val == x:
                    n.next = n.next.next
                    break
                n = n.next 
            if n.next == None:
                print(f'{x} not found in list')
    
    def reverse(self):
        prev = None
        n = self.start_node
        while n != None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.start_node = prev


    def traverse(self):
        n = self.start_node
        while n != None:
            print(n.val, end = ' ')
            n = n.next
        print('')
            
if __name__ == '__main__':
    x = [1,2,3,4,5]
    mylist = LinkedList()
    for i in x:
        mylist.insert_to_end(i)

    mylist.traverse()


