import sys
from sys import argv
import os
import numpy as np
from AStarNode import Node

cavernFile = ""
fl = None
CAVERN_ARRAY = []
cavern_matrix = None

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

# Open file and write contents to variable
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

  
def AStar(_matrix, _start, _end):
    start_node = _start
    end_node = _end



def main():
    fl = sys.argv[1]
    load_file(fl)
    cavern_array = process_file(cavernFile)
    process_cavern_arr(cavern_array)


main()