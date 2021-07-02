class Node:
    def __init__(self, data):
        self.val = data
        self.count = 1
        self.left = None
        self.right = None
        
class Binary_tree:
    def __init__(self):
        self.root = None
        self.height = -1

    def insert(self, root, x):
        if self.root == None:
            self.root = Node(x)
            return
        
        if x < root.val:
            if root.left == None:
                root.left = Node(x)
            else:
                self.insert(root.left, x)
        elif x > root.val:
            if root.right == None:
                root.right = Node(x)
            else:
                self.insert(root.right, x)
        else:
            root.count += 1      

    def delete(self, root, x):
        if root == None:
            return root

        if x < root.val:
            root.left = self.delete(root.left, x)
        elif x > root.val:
            root.right = self.delete(root.right, x)
        else:
            if root.count > 1:
                root.count -= 1
            elif root.left != None and root.right != None:
                new_root = root.right
                while new_root.left != None:
                    new_root = new_root.left
                root.val = new_root.val
                root.right = self.delete(root.right, new_root.val)
            elif root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            
        return root

    def get_height(self, root):
        if root == None:
            return -1
        else:
            height = max(self.get_height(root.left), self.get_height(root.right)) + 1
            return height 

    def search(self, root, x):
        if self.root == None:
            print('Tree is empty')
            return False
        if root == None:
            return False
        elif x < root.val:
            return self.search(root.left, x)
        elif x > root.val:
            return self.search(root.right, x)
        else:
            return True 

    def inOrder(self, root):
        if root == None:
            return

        self.traverse(root.left)
        if root.count == 1:
            print(root.val, end = ' ') 
        else:
            print(f'{root.val}({root.count})', end = ' ')
        self.traverse(root.right)

    def preOrder(self, root):
        if root == None:
            return
 
        if root.count == 1:
            print(root.val, end = ' ') 
        else:
            print(f'{root.val}({root.count})', end = ' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

class Avl_tree(Binary_tree):
    def __init__(self):
        super().__init__()

    def insert(self, root, x):
        if root == None:
            root = Node(x)
        elif x < root.val:
            root.left = self.insert(root.left, x)
        elif x > root.val:
            root.right = self.insert(root.right, x)
        else:
            root.count += 1

        b_val = super().get_height(root.left) - super().get_height(root.right)
        #print(f'val: {x} b_val: {b_val}')
        if b_val == 2 and x < root.left.val: #left-left
            return self.right_rotation(root)
        elif b_val == 2 and x > root.left.val: #left-right
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root.right)
        elif b_val == -2 and x < root.right.val: # right-left
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        elif b_val == -2 and x > root.right.val: #right-right
            return self.left_rotation(root)
        
        return root

    def right_rotation(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def left_rotation(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

if __name__ == '__main__':
    x = [1,2,3,4,5,6,7,8,9,8,7,8,6,7,7]

    mytree = Avl_tree()
    for i in x:
        mytree.root = mytree.insert(mytree.root, i)

    mytree.preOrder(mytree.root)
    print('')
    mytree.delete(mytree.root, 8)
    mytree.preOrder(mytree.root)

