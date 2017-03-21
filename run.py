# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ad = search.GPSProblem('A', 'D', search.romania)
ba = search.GPSProblem('B', 'A', search.romania)
ac = search.GPSProblem('A', 'C', search.romania)

print "---------EN ANCHURA----------"
print search.breadth_first_graph_search(ab).path()
print "---------EN PROFUNDIDAD----------"
print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()
print "---------SIN HEURISTICA----------"
print search.Lista_coste(ab).path()
print "---------CON HEURISTICA----------"
print search.Lista_costeh(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
