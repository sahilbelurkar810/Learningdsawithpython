class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node0.left=node1
node0.right=node2
print(node0.right.key)



tupple_tree = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
tree = parse_tuple(tupple_tree)
print(tree.left.left.key)


def traverse_inorder(node):
    if node is None:
        return []
    return (traverse_inorder(node.left)+
            [node.key]+
            traverse_inorder(node.right))
list = traverse_inorder(tree)
print(list)