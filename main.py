import sys
from sys import argv
from sys import exit
import numpy as np
from AStarNode import Node

cavernFile = ""
fl = None
cavern_matrix = None

""""open_list file and write contents to variable"""
def process_file(_file):
    global fl
    cavernFile = (_file + ".cav")
    fl = _file
    with open(cavernFile) as f:
        for l in f: 
            cv = l.split(",")
    return [int(x) for x in cv]

def process_cavern_arr(c_array):
    """First integer - Number of caverns
    The next N*2 integers represent each of the coordinates - each value is non-negative
    The final N*N integers represent the connectivity of the tunnels. 1 - connected, 0 - not connected
    Some tunnels are one-way"""
    global cavern_matrix

    n = c_array[0] # number of caverns - 1st element
    coords = c_array[1:n*2+1] # Unsorted sequence of coordinates - 2nd element ... n*2 element
    coordinates = list(zip(coords[::2], coords[1::2])) # Sorted coordinates (above)
    matrix_seq = c_array[n*2+1:] # Isolated the matrix values
    cavern_matrix = np.reshape(matrix_seq, (n, n)) # Matrix as a 2D 7x7 array
    start = coordinates[0] # First Node
    end = coordinates[-1] # End Node

    AStarAlgorithm(start, end, n, cavern_matrix, coordinates)

"""Just separated this part of the function out for modularity"""    
def showPath(currentNode):
    path = []
    while currentNode:
        path.append(currentNode.number)
        currentNode = currentNode.parent
    write_results(path[::-1])

"""Writes the results to file .csn"""
def write_results(path):
    f = open(fl + ".csn", "w")
    for p in path:
        f.write(str(p) + " ")
    sys.exit()
    
"""Run the A* Algorithm"""
def AStarAlgorithm(_start, _end, n, matrix, coords):
    startNode = Node(_start, None, 1)
    endNode = Node(_end, None, n)
    matrix = matrix
    coordinates = coords

    startNode.G = startNode.H = startNode.F = 0
    endNode.F = endNode.G = endNode.H = 0

    startNode.F = startNode.euclideanDist(endNode)

    open_list = []
    closed_list = []

    # First add startNode to begin
    open_list.append(startNode)
    
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        # Get node with lowest F score
        for idx, node in enumerate(open_list):
            if node.F < current_node.F:               
                current_node = node
                current_index = idx

        # If the next node is the end node
        if current_node == endNode:
            showPath(current_node)

        # Node is expanded
        closed_list.append(current_node)

        children = []

        # Loop over coordinates and create all Nodes
        for idx, coordinate in enumerate(coordinates):
            childNode = Node(coordinate, None, idx+1)
            if current_node.ifPathExists(childNode, matrix):
                children.append(childNode)

        # Check expanded nodes
        for child in children:        
            # Skip closed nodes
            if child in closed_list:
                continue
            
            # If child is yet to be assigned or better path found
            if current_node.G + current_node.euclideanDist(child) < child.G or not child in open_list:
                child.parent = current_node
                child.G = current_node.G + current_node.euclideanDist(child)
                child.H = child.euclideanDist(endNode)
                child.F = child.G + child.H
                open_list.append(child)

        # Current Node has been expanded, remove from open list
        open_list.pop(current_index)
    # Open list is empty
    write_results([0])

"""Program starting point"""
def main():
    _fl = sys.argv[1]
    cavern_array = process_file(_fl)
    process_cavern_arr(cavern_array)

main()