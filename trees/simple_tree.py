class TreeNode:
    def __init__(self, data, children = None):
        self.data = data
        self.children = children if children else [] 
        
    def __str__(self, level=0):
        if level == 0:
            arrow = ""
        else:
            arrow = "  " * (level-1) + "|_"
        ret = arrow + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, child):
        self.children.append(child)

def test_create_tree():
    child3 = TreeNode('c3')
    child1 = TreeNode('c1', [child3])
    child2 = TreeNode('c2')
    node = TreeNode('r', [child1, child2])    
    print(node)
    assert f"{node}" == "r\n|_c1\n  |_c3\n|_c2\n"
    print("test_create_tree PASS")


def test_append_node():
    child1 = TreeNode('c1')
    node = TreeNode('r')
    node.addChild(child1)
    assert f"{node}" == "r\n|_c1\n"
    
    child3 = TreeNode('c3')
    child1.addChild(child3)
    assert f"{node}" == "r\n|_c1\n  |_c3\n"

    print(node)
    print("test_append_node PASS")

test_create_tree()
test_append_node()

