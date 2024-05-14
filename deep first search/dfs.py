class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    
    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    
    def _add(self, val, node):
        if val < node.value:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)
                
    def view_tree(self):
        if self.root:
            self._view_tree(self.root)
    
    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.value, end = " ")
            self._view_tree(node.right)
            
    def dfs(self, looking_for):
        path = []
        elem = self._dfs(self.root, looking_for, path)
        return elem, path
    
    
    def _dfs(self, node, looking_for, path):
        if node is None:
            return None
        if node.value == looking_for:
            path.append(node.value)
            return node.value
        
        left_search = self._dfs(node.left, looking_for, path)
        if left_search:
            path.insert(0, node.value)
            return left_search
        
        right_search = self._dfs(node.right, looking_for, path)
        if right_search:
            path.insert(0, node.value)
            return right_search
        
        return None

tree = Tree()
arr = [1, 4, 2, 5, 5, 8, 10, 15, 6, 50, 7]
def array_to_tree(array, tree):
    for elem in array:
        tree.add(elem)
                
array_to_tree(arr, tree)
tree.view_tree()
print("\n")
print(tree.dfs("""enter element"""))
