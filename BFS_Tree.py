from collections import deque


class Node:
    def __init__(self,val=0,left=None,right=None):
        self.data = val
        self.left=left
        self.right = right

class BFT:
    def BfsTraversal(self, root):
        queue = deque()
        visited=[]

        queue.append(root)
        while queue:
            node = queue.popleft()
            visited.append(node.data)
            if(node.left):
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited


if __name__ == "__main__":
    tree = Node(5)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.right.left = Node(15)
    tree.right.right = Node(21)
    bft = BFT()
    print(bft.BfsTraversal(tree))


    