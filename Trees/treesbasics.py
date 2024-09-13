from collections import deque




class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None



def build_simple_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.value)
        result.extend(inorder_traversal(root.right))

    return result


def preorder_traversal(root):
    result = []
    if root:
        result.append(root.value)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))

    return result


def postorder_traversal(root):
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.value)
    return result


# Remember that BFS is done using Queue 

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result


def tree_height(root):
    if not root:
        return 0
    
    return 1 + max(tree_height(root.left), tree_height(root.right))


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0
        left = check_balance(node.left)
        right = check_balance(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1 :
            return -1
        return 1 + max(left, right)
    return check_balance(root) != -1

## understand the recursive calls of both is balanced, count nodes, tree height 



simple_tree_root = build_simple_tree()
print("the in order traversal is " , inorder_traversal(simple_tree_root))
print("the Pre order traversal is " , preorder_traversal(simple_tree_root))
print("the Post order traversal is " , postorder_traversal(simple_tree_root))
print("the level order traversal is " , level_order_traversal(simple_tree_root))
