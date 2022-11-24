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

def test_search():
    t = Trie()
    #t.insert('API')
    #assert t.search('API')
    print("test_search PENDING")

def test_delete_part_prefix():
    t = Trie()
    #t.insert('API')
    #t.insert('APPLE')
    #t.delete('API')
    #assert t.search('APPLE')
    #assert t.search('API') == False
    print("test_delete_part_prefix PENDING")

def test_delete_full_prefix():
    t = Trie()
    #t.insert('APPLE')
    #t.insert('API')
    #t.insert('APIS')
    #t.delete('API')
    #assert t.search('API') == False 
    #assert t.search('APPLE')
    #assert t.search('APIS')
    print("test_delete_full_prefix PENDING")

def test_delete_long_word_on_top_of_other_word():
    t = Trie()
    #t.insert('APIS')
    #t.insert('AP')
    #t.delete('APIS')
    #assert t.search('APIS') == False
    #assert t.search('AP')
    print("test_delete_long_word_on_top_of_other_word PENDING")

def test_delte_word_with_no_dependencies():
    t = Trie()
    #t.insert('APIS')
    #t.insert('K')
    #t.delete('K')
    #assert t.search('K') == False
    #assert t.search('APIS')
    print("test_delte_word_with_no_dependencies PENDING")


test_create_Trie()
test_insert()
test_search()
test_delete_part_prefix()
test_delete_full_prefix()
test_delete_long_word_on_top_of_other_word()
test_delte_word_with_no_dependencies()
