
import math

# Define a Node in the A Star algorithm
# Nodes contain:
#  -> Coordinates (x, y)
#  -> Parent (Node)
#  -> Number (1 -> n)
#  -> G, H + F cost
class Node:
    def __init__(self, coord, parent, number):
        self.coord = coord
        self.parent = parent
        self.number = number # i.e. 1 -> n 
        self.G = math.inf # distance between current and start nodes
        self.H = math.inf # ESTIMATED distance between current and end nodes
        self.F = math.inf # Total cost of current node

    """Get the euclidean distance between two Nodes"""
    def euclideanDist(self, t_node):
        tempX = (self.coord[0] - t_node.coord[0])**2
        tempY = (self.coord[1] - t_node.coord[1])**2
        return math.sqrt(tempX + tempY)
        
    """Override the __eq__ function, 
        ... Nodes are equal if they share the same coordinates"""
    def __eq__(self, other):
        return self.number == other.number

    """Returns whether tunnel exists towards target node
       ... as described in coursework with 1 or 0 in matrix"""
    def ifPathExists(self, t_node, matrix):
        return matrix[t_node.number-1][self.number-1] # Cross reference node numbers, returns 1 or 0

    