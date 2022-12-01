from queue import PriorityQueue
import sys
from sys import argv
import os
import numpy as np
import math
from AStarNode import Node
import time

cavernFile = ""
fl = None
#CAVERN_ARRAY = []
cavern_matrix = None
#Nodes = []

"""Find the file supplied in the command line arg"""
def load_file(filename):
    global cavernFile
    
    """this_dir = os.getcwd()
    # Look through this directory for given filename
    while 1:
        this_dir_files = os.listdir(this_dir)
        # File found
        if cavernFile in this_dir_files:
            break
        # File NOT found
        else:          
            print("Could not find "+cavernFile+" in current dir!")
            exit(1)"""

""""open_list file and write contents to variable"""
def process_file(_file):
    cavernFile = (_file + ".cav")
    with open(cavernFile) as f:
        for l in f: 
            cv = l.split(",")
    print("Read file --- %s seconds ---" % (time.time() - start_time))
    return [int(x) for x in cv]

def process_cavern_arr(c_array):
    """First integer - Number of caverns
    The next N*2 integers represent each of the coordinates - each value is non-negative
    The final N*N integers represent the connectivity of the tunnels. 1 - connected, 0 - not connected
    Some tunnels are one-way"""
    global cavern_matrix

    #print("Started data readying --- %s seconds ---" % (time.time() - start_time))
    n = c_array[0] # number of caverns - 1st element
    coords = c_array[1:n*2+1] # Unsorted sequence of coordinates - 2nd element ... n*2 element
    coordinates = list(zip(coords[::2], coords[1::2])) # Sorted coordinates (above)
    matrix_seq = c_array[n*2+1:] # Isolated the matrix values
    cavern_matrix = np.reshape(matrix_seq, (n, n)) # Matrix as a 2D 7x7 array
    start = coordinates[0] # First Node
    end = coordinates[-1] # End Node

    #print("Data ready --- %s seconds ---" % (time.time() - start_time))
    global Nodes

    AStarAlgorithm(start, end, n, cavern_matrix, coordinates)

"""Just separated this part of the function out for modularity"""    
def showPath(currentNode):
    path = []
    while currentNode:
        path.append(currentNode.number)
        currentNode = currentNode.parent
    print(path[::-1])
    #print("Finish --- %s seconds ---" % (time.time() - start_time))
    
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
        
        for idx, node in enumerate(open_list):
            #print(f'[Checking Node]{node.coord} F value = {node.F}, ....,[Current Node] {current_node.coord} F value = {current_node.F}')   
            if node.F < current_node.F:               
                current_node = node
                current_index = idx

        # If the next node is the end node
        if current_node == endNode:
            showPath(current_node)
            break
 
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        children = []

        # Loop over coordinates and create all Nodes
        for idx, coordinate in enumerate(coordinates):
            childNode = Node(coordinate, None, idx+1)
            if current_node.ifPathExists(childNode, matrix):
                children.append(childNode)

        for child in children:
            if not child in open_list and not child in closed_list:
                child.G = current_node.G + current_node.euclideanDist(child)
                child.H = child.euclideanDist(endNode)
                child.F = child.G + child.H
                child.parent = current_node
                open_list.append(child)
            else:
                child.G = current_node.G + current_node.euclideanDist(child)
                child.H = child.euclideanDist(endNode)
                child.F = child.G + child.H
                child.parent = current_node
                if child in closed_list:
                    closed_list.remove(child)
                    open_list.append(child)
    return "No path"

"""Program starting point"""
def main():
    _fl = sys.argv[1]
    cavern_array = process_file(_fl)
    process_cavern_arr(cavern_array)

start_time = time.time()
main()