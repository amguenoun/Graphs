from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # Create a graph
    graph = Graph()
    # add vertices and edges to the graph
    for relationship in ancestors:
        # relationship is a tuple
        # check to see if set exists if not create set
        if relationship[1] not in graph.vertices:
            graph.vertices[relationship[1]] = {relationship[0]}
        # if so add connection
        else:
            graph.vertices[relationship[1]].add(relationship[0])
