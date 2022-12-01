from queue import PriorityQueue
import sys
from sys import argv
import os
import numpy as np
import math
from AStarNode import Node

cavernFile = ""
fl = None
CAVERN_ARRAY = []
cavern_matrix = None
Nodes = []

# Find the file supplied in the command line arg
def load_file(filename):
    global cavernFile
    cavernFile = (filename + ".cav")
    this_dir = os.getcwd()
    # Look through this directory for given filename
    while 1:
        this_dir_files = os.listdir(this_dir)
        if cavernFile in this_dir_files:
            print("Found file: "+cavernFile+"!")
            break
        else:
            # Exit code if file not found
            print("Could not find "+cavernFile+" in current dir!")
            exit(1)

# open_list file and write contents to variable
def process_file(_file):
    with open(_file, 'r') as filestream:
        for l in filestream:
            cv = l.split(",")
    return [int(x) for x in cv]

def process_cavern_arr(c_array):
    """First integer - Number of caverns
    The next N*2 integers represent each of the coordinates - each value is non-negative
    The final N*N integers represent the connectivity of the tunnels. 1 - connected, 0 - not connected
    Some tunnels are one-way"""
    global cavern_matrix

    # Create small validation effort to ensure cavern array is correct length before proceeding
    num_elems = 1 + c_array[0] * 2 + c_array[0] * c_array[0]
    if len(c_array) == num_elems:
        print("Length checked, OK.")
    else:
        print("Error - length of array is not correct!\nShould be " + str(num_elems) + " elements long "+
         "is instead " + str(len(c_array)) + " elements long!")
        exit(1)

    n = c_array[0] # number of caverns - 1st element
    coords = c_array[1:n*2+1] # Unsorted sequence of coordinates - 2nd element ... n*2 element
    coordinates = list(zip(coords[::2], coords[1::2])) # Sorted coordinates (above)
    matrix_seq = c_array[n*2+1:] # Isolated the matrix values
    cavern_matrix = np.reshape(matrix_seq, (n, n)) # Matrix as a 2D 7x7 array
    start = coordinates[0] # First Node
    end = coordinates[-1] # End Node

    global Nodes

    print(AStarAlgorithm(start, end, n, cavern_matrix, coordinates))

    
def showPath(cameFrom, end_node):
    total_path = {end_node.number}
    for end_node in cameFrom:
        end_node = cameFrom[end_node]
        total_path.add(end_node.number)
    print(total_path)
  
def AStarAlgorithm(_start, _end, n, matrix, coords, cost=1):
    """
    startNode = Node(_start, None, 1)
    endNode = Node(_end, None, n)
    matrix = matrix
    coordinates = coords

    openSet = PriorityQueue()
    openSet.put((math.inf, startNode))

    closedSet = []

    cameFrom = {}
    gScore = {}
    gScore[startNode] = 0

    fScore = {}
    fScore[startNode] = startNode.euclideanDist(endNode) 
    fScore[endNode] = 0

    loops = 0

    while not openSet.empty():

        loops += 1
        #print(f'Current loop: {loops}')
        print('Open set:')
        for item in openSet.queue:
            print(f'Node {item[1].number}.. F Cost: {fScore[item[1]]}')
        current = openSet.get()[1]
        
        print(f'Opening node {current.number}')
        if current.coord == endNode.coord:
            showPath(cameFrom, current)
            exit(1)      
        
        children = []
        for idx, coordinate in enumerate(coordinates):
            childNode = Node(coordinate, None, idx+1)
            if current.ifPathExists(childNode, matrix):
                #print(f'Path from {current.number} to {childNode.number} exists')
                children.append(childNode)

        for child in children:
            tempG = gScore[current] + current.euclideanDist(child)

            if not child in gScore:
                gScore[child] = math.inf

            if tempG < gScore[child]:
                cameFrom[child] = current
                gScore[child] = tempG
                fScore[child] = tempG + child.euclideanDist(endNode)
                #print(f'F score of child: {fScore[child]}')

                if (any(fScore[child], child) in n for n in openSet.queue):
                    #print(f'Putting node {child.number} in open set with F Cost: {fScore[child]}')
                    openSet.put((fScore[child], child))
        
    return False
    """


    startNode = Node(_start, None, 1)
    endNode = Node(_end, None, n)
    cost = cost
    matrix = matrix
    coordinates = coords

    startNode.G = startNode.H = startNode.F = 0

    endNode.F = 0
    endNode.G = 0 
    endNode.H = 0

    startNode.F = startNode.euclideanDist(endNode)

    open_list = []
    closed_list = []

    open_list.append(startNode)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        
        for idx, node in enumerate(open_list):

            #print(f'[Checking Node]{node.coord} F value = {node.F}, ....,[Current Node] {current_node.coord} F value = {current_node.F}')
            
            if node.F < current_node.F:               
                current_node = node
                current_index = idx
        
        print(f'Node :     {current_node.number} ')

        if current_node.coord == endNode.coord:
            while current_node:
                print(f'{current_node.number}: {current_node.F}')
                current_node = current_node.parent
            exit(1)
        
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        children = []

        # Loop over coordinates
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


def main(fl="input1"):
    _fl = fl
    try:
        _fl = sys.argv[1]
    except Exception as e:
        print("Filename not given as param. Continuing as test run...")
    finally:
        pass
    load_file(_fl)
    cavern_array = process_file(cavernFile)
    process_cavern_arr(cavern_array)


main()