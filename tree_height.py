# python3

import sys
import threading
# import numpy as np
# from collections import namedtuple

# Node = namedtuple("Node", "node parent height")

class Node:
  def __init__(self, node, parent):
    self.node = node
    self.parent = parent
    self.height = 0

        
def compute_height(n, parents):
    for i in range(n-1):
        el = parents[i]

        if el.height != 0:
            continue
        el.height = 1

        # path = np.array([el])
        path = [el]
        node_height = 1
        while el.parent != -1:
            parent = parents[el.parent]

            if parent.height != 0:
                el.height = parent.height + 1
                node_height = node_height + el.height - 1
                break
            
            el = parent
            # el =  = 1
            # path = np.concatenate((path, [el]))
            path.append(el)
            node_height += 1
            
        for p in path:
            el = parents[p.node]
            el.height = node_height
            node_height -= 1
    
    # return np.max(np.array([p[2] for p in parents]))
    return max([p.height for p in parents])



def main():
    inputType = input()
    elements = []
    nodeCount = -1

    if 'I' in inputType:
        nodeCount = int(input())
        # elements = np.array([Node(ix, int(x), 0) for ix, x in enumerate(input().split(" "))])
        elements = [Node(ix, int(x)) for ix, x in enumerate(input().split(" "))]
    elif 'F' in inputType:
        fileName = input()

        if 'a' in fileName:
            return
        
        with open("./test/%s" % (fileName), "r") as file:
            nodeCount = int(file.readline())
            elements = [Node(ix, int(x)) for ix, x in enumerate(file.readline().split(" "))]
            # elements = np.array([Node(ix, int(x), 0) for ix, x in enumerate(file.readline().split(" "))])
    
    if nodeCount == -1:
        return

    height = compute_height(nodeCount, elements)
    
    print(height)
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
