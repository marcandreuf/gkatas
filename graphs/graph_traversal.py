from collections import defaultdict

class Graph:
    def __init__(self, numVertices):
        self.graph = defaultdict(list)
        self.numVertices = numVertices

    def addEdge(self, vertex, edge):
        sefl.graph[vertex].append(edge)


    #def bfs(self)
    #def dfs(self)
    #def topologicalSort(self)

def _trav_sample_graph():
    return {"a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]}

def _sample_graph():
    g = Graph(8)
    v.addEdge("A", "C")
    v.addEdge("C", "E")
    v.addEdge("E", "H")
    v.addEdge("E", "F")
    v.addEdge("F", "G")
    v.addEdge("B", "D")
    v.addEdge("B", "C")
    v.addEdge("D", "F")
    return v    

def _sample_ssspp():
    return { "a" : ["b", "c"],
             "b" : ["d", "g"],
             "c" : ["d", "e"],
             "d" : ["f"],
             "e" : ["f"],
             "g" : ["f"]}

# TODO test_bfs_traversal
def test_bfs_traversal():
    #g = _trav_sample_graph()
    #assert g.bfs() == ['a', 'b', 'c', 'd', 'e', 'f']
    print("test_bfs_traversal PENDING")

# TODO test_dfs_traversal
def test_dfs_traversal():
    #g = _trav_sample_graph()
    #assert g.dfs() == ['a', 'c', 'e', 'f', 'd', 'b' ]
    print("test_dfs_traversal PENDING")

# TODO test_topolocialSort
def test_topolocialSort():
    #g = _sample_graph()
    #assert g.topologicalSort() == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']
    print("test_topolocialSort PENDING")

# TODO test_sssp_bfs
def test_sssp_bfs():
    #g = _sample_ssspp()
    #assert g.sssp_bfs("a", "f") = ['a', 'b', 'd', 'f']
    #assert g.sssp_bfs("a", "e") = ['a', 'c', 'e']
    #assert g.sssp_bfs("a", "z") = ?
    print("test_sssp_bfs PENDING")


test_bfs_traversal()
test_dfs_traversal()
test_topolocialSort()
test_sssp_bfs()

