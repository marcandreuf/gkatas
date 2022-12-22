import heapq

class Edge:
    def __init__(self, weight, vstart, vend):
        self.weight = weight
        self.vstart = vstart
        self.vend = vend

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.pred = None
        self.neighbors = []
        self.min_dist = float("inf")

    def __lt__(self, other_node):
        return self.min_dist < other_node.min_dist

class Dijkstra:
    def __init__(self):
        self.heap = []

    def _calculate_distances(self, vstart):
        #TODO. implement algorithm
        pass

    def get_shortest_path(self, vstart, vend):
        #TODO. call calculate_distance if necessary
        # vstart min dist == infinity
        #Traverse the predecessors
        #Print path start to end nodes
        pass


def _sample_graph():
    # Step 1 - create nodes
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    
    # Step 2 - create edges
    nodeA.add_edge(6, nodeB)
    nodeA.add_edge(10, nodeC)
    nodeA.add_edge(9, nodeD)
    
    nodeB.add_edge(5, nodeD)
    nodeB.add_edge(16, nodeE)
    nodeB.add_edge(13, nodeF)
    
    nodeC.add_edge(6, nodeD)
    nodeC.add_edge(5, nodeH)
    nodeC.add_edge(21, nodeG)
    
    nodeD.add_edge(8, nodeF)
    nodeD.add_edge(7, nodeH)
    
    nodeE.add_edge(10, nodeG)
    
    nodeF.add_edge(4, nodeE)
    nodeF.add_edge(12, nodeG)
    
    nodeH.add_edge(2, nodeF)
    nodeH.add_edge(14, nodeG)

    return {'A':nodeA,
            'B':nodeB,
            'C':nodeC,
            'D':nodeD,
            'E':nodeE,
            'F':nodeF,
            'G':nodeG,
            'H':nodeH}
    

def test_find_min_path():
    #g = _sample_graph()
    #d = Dijkstra()
    #assert d.get_shortest_path(g['A', g['E']]) == ['A','D','F','E']
    #assert d.get_shortest_path(g['A', g['G']]) == ['A','C','H','G']
    print("test_find_min_path PENDING")


#TODO. Implement all TDD tests to implement the algorithms step by step.
# Final verification test
test_find_min_path()
