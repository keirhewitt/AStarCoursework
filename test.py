from AStarNode import Node
from main import cavern_matrix

# TEST
# Path from Node 4 to Node 2, but no path exists from 2 back to 4 (1-way)
testNode1 = Node((2,8), None, 1)
testNode2 = Node((3,2), None, 2)
testNode3 = Node((14,5), None, 3)
testNode4 = Node((7,6), None, 4)
testNode5 = Node((11,2), None, 5)
testNode6 = Node((11,6), None, 6)
testNode7 = Node((14,1), None, 7)

assert testNode1.ifPathExists(testNode2, cavern_matrix) == 0, "Assertion failed"
assert testNode1.ifPathExists(testNode3, cavern_matrix) == 0, "Assertion failed"
assert testNode1.ifPathExists(testNode4, cavern_matrix) == 1, "Assertion failed"
"""testNode1.ifPathExists(testNode5, cavern_matrix)
testNode1.ifPathExists(testNode6, cavern_matrix)
testNode1.ifPathExists(testNode7, cavern_matrix)"""

"""testNode2.ifPathExists(testNode1, cavern_matrix)
testNode2.ifPathExists(testNode3, cavern_matrix)"""
assert testNode2.ifPathExists(testNode4, cavern_matrix) == 0, "Assertion failed"
assert testNode2.ifPathExists(testNode5, cavern_matrix) == 1, "Assertion failed"
assert testNode2.ifPathExists(testNode6, cavern_matrix) == 0, "Assertion failed"
assert testNode2.ifPathExists(testNode7, cavern_matrix) == 0, "Assertion failed"

"""testNode3.ifPathExists(testNode1, cavern_matrix)
testNode3.ifPathExists(testNode2, cavern_matrix)"""
assert testNode3.ifPathExists(testNode4, cavern_matrix) == 0, "Assertion failed"
assert testNode3.ifPathExists(testNode5, cavern_matrix) == 1, "Assertion failed"
assert testNode3.ifPathExists(testNode6, cavern_matrix) == 1, "Assertion failed"
assert testNode3.ifPathExists(testNode7, cavern_matrix) == 1, "Assertion failed"

# Test class
# Mostly just 