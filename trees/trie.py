class TrieNode:
    def __init__(self):
        self.childs = {}
        self.endOfString = False

class Trie():
    def __init__(self):
        self.root = TrieNode()


def test_create_Trie():
    t = Trie()
    assert t.root is not None
    print("test_create_Trie PASS")


def test_insert():
    t = Trie()
    #t.insert('APP')
    #assert t.words = ['APP']
    #t.insert('API')
    #assert t.words = ['APP', 'API']
    #t.insert('APIS')
    #assert t.words = ['APP', 'API', 'APIS']
    #t.insert('APIS')
    #assert t.words = ['APP', 'API', 'APIS']
    print("test_insert PENDING")

test_create_Trie()
test_insert()

