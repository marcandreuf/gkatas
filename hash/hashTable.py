class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
        
    def isEmpty(self):
        for k in self.arr:
            if k is not None:
                return False
        return True

    def hashfn(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def put(self, key, value):
        h = self.hashfn(key)
        self.arr[h] = value

    def get(self,key):
        h = self.hashfn(key)
        return self.arr[h]
        
def test_create_empty_hashTable():
    ht = HashTable()
    assert ht.isEmpty()
    print("test_create_empty_hashTable PASS")
    
def test_simple_hash_function():
    ht = HashTable()
    assert ht.hashfn('Hello') == 0
    assert ht.hashfn('Hello world') == 84
    print("test_simple_hash_function PASS")


def test_put():
    ht = HashTable()
    ht.put('Hello', 'A')
    assert ht.isEmpty() == False
    assert ht.arr[0] == 'A'
    print("test_put PASS")


def test_get():
    ht = HashTable()
    ht.put('Hello', 'A')
    assert ht.get('Hello') == 'A'
    print("test_get PASS")

def test_add_collision_direct_chaining():
    print("test_add_collision_direct_chaining PENDING")


def test_add_collision_oa_linear_probing():
    print("test_add_collision_oa_linear_probing PENDING")


def test_add_collision_oa_quadratic_probing():
    print("test_add_collision_oa_quadratic_probing PENDING")

def test_add_collision_oa_double_hashing():
    print("test_add_collision_oa_double_hashing PENDING")

def test_add_collision_inner_hash_table():
    # Test the idea to use child hast table with 
    # the child hasing function taking as input the parent
    # hash. Insetad of chaining a linked list can we
    # use a set of child hash tables instead?
    print("test_add_collision_inner_hash_table PENDING")


test_create_empty_hashTable()
test_simple_hash_function()
test_put()
test_get()
test_add_collision_direct_chaining()
test_add_collision_oa_linear_probing()
test_add_collision_oa_quadratic_probing()
test_add_collision_oa_double_hashing()
test_add_collision_inner_hash_table()

