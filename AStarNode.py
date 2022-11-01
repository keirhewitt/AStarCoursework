import math

# Define a Node in the A Star algorithm
# Nodes contain:
#  -> Coordinates (x, y)
#  -> Parent (Node)
#  -> Number (1 -> n)
#  -> G, H + F cost
class Node:
    def __init__(self, coord, parent, number):
        self.coord = ()
        self.parent = None
        self.number = number # i.e. 1 -> n 
        self.G = 0 # distance between current and start nodes
        self.H = 0 # ESTIMATED distance between current and end nodes
        self.F = 0 # Total cost of current node

    """Get the euclidean distance between two Nodes"""
    def euclideanDist(self, t_node):
        tempX = (self.coord[0] - t_node.coord[0])^2
        tempY = (self.coord[1] - t_node.coord[1])^2
        res = math.sqrt(tempX + tempY)
        return res

    """Returns whether tunnel exists towards target node
       ... as described in coursework with 1 or 0 in matrix"""
    def ifPathExists(self, t_node, matrix):
        return matrix[t_node.number-1][self.number-1] # Cross reference node numbers, returns 1 or 0

    