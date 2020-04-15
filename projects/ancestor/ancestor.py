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

    # if no parents then return -1
    if starting_node not in graph.vertices:
        return -1

    # use DFT to find greatest distance
    visited = set()
    stack = Stack()
    stack.push([starting_node])
    max_path = []
    while stack.size() != 0:
        path = stack.pop()
        if path[-1] not in visited:  # prevent cycles
            visited.add(path[-1])
            if len(path) > len(max_path):
                max_path = path
            # if more than one, return the one with smaller numeric id
            elif len(path) == len(max_path):
                if max_path[-1] > path[-1]:
                    max_path = path
            if path[-1] in graph.vertices:
                for parent in graph.get_neighbors(path[-1]):
                    stack.push(path + [parent])

    return max_path[-1]
