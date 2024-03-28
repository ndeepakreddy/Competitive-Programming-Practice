
'''Algorithm for deletion in a binary tree:
1. 1. Start from the root of the tre

2. If the tree is empty, return lione

3. If the root node is the node to be deleted:

    If the root has no children, return Nane

    If the rout has only one child, return the child. 
    If the root has two children:

        Find the deepest node in the right subtree (or left subtree)

        Copy the data of the deepest nade to the root.

        Delete the deepest node

4. Otherwise, perform a level order traversal to find the node to ne del

5. Once the node to be deleted is found)

    If the node has no children, delete the node

    If the node has only one child, replace the node with its child,   
    If the node has two children:

        Find the deepest node in the right sabtree (or left subtree).
        Copy the data of the deepest made to the node to be deleted. Delete the deepest node.

6. Return the root of the modified tree.'''


# class to create a node with data, left child and right child.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal of a binary tree


def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

# function to delete the given deepest node (d_node) in binary tree


def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

# function to delete element in binary tree


def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        key_node.data = x
        deleteDeepest(root, temp)
    return root


# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion: ", end = "")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print();
    print("The tree after the deletion: ", end = "")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print();
    print("The tree after the deletion: ", end = "")
    inorder(root)
    key=30
    root=deletion(root,key)
    print("inorder traversal")
    inorder(root)
