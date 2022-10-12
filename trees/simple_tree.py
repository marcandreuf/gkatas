class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        if level == 0:
            arrow = ""
        elif level == 1:
            arrow = "|_"
        else:
            arrow = " " * (level) + "|_"
        ret = arrow + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def test_create_tree():
    child3 = TreeNode('c3')
    child1 = TreeNode('c1', [child3])
    child2 = TreeNode('c2')
    node = TreeNode('r', [child1, child2])    
    print(node)

test_create_tree()
