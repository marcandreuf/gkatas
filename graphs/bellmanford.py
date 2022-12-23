#TODO Extract Edge and Graph class from dijkstra and import the class into both files.


def _sample_graph():
    # Step 1 - create nodes
    #nodeA = Node("A")
    #nodeB = Node("B")
    #nodeC = Node("C")
    #nodeD = Node("D")
    #nodeE = Node("E")
    
    # Step 2 - create edges
    # TODO. create nodes, see the zettler notes at the card "Graph Algorithms & Data Structure 20221216".
    """
    Example code to create the graph.
    But create graph style using Node and Graph classes instead.
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.add_edge("A", "C", 6)
    g.add_edge("A", "D", 6)
    g.add_edge("B", "A", 3)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "C", 2)
    g.add_edge("D", "B", 1)
    g.add_edge("E", "B", 4)
    g.add_edge("E", "D", 2)
    """
    pass

def test_calculate_min_distances():
    #g = _sample_graph()
    #b = BellmanFord()
    #assert b.calculate(g) == {'A':6,'B':3,'C':4,'D':2,'E':0}
    print("test_calculate_min_distances PENDING")


def test_find_min_path():
    #g = _sample_graph()
    #b = BellmanFord()
    #assert b.min_paths_from(g, g['E']) == {'A':['E','D','B','A'],'B':['E','D','B'],'C':['E','D','C'],'D':['E','D']}
    print("test_find_min_path PENDING")

#TODO Implement each test from basic case to final solution.

# Final verification test
test_calculate_min_distances()
test_find_min_path()

