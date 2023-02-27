# python3

import sys
import threading
import numpy as np
from collections import namedtuple

Node = namedtuple("Node", ["node", "parent" , "height"])

        
def compute_height(n, parents):
    for i in range(n-1):
        el = parents[i]

        if el[2] != 0:
            continue
        el[2] = 1

        path = np.array([el])
        node_height = 1
        while el[1] != -1:
            parent = parents[el[1]]

            if parent[2] != 0:
                el[2] = parent[2] + 1
                node_height = node_height + el[2] - 1
                break
            
            el = parent
            el[2] = 1
            path = np.concatenate((path, [el]))
            node_height += 1
            
        for p in path:
            el = parents[p[0]]
            el[2] = node_height
            node_height -= 1
    
    return np.max(np.array([p[2] for p in parents]))


def main():
    inputType = input()
    elements = []
    nodeCount = -1

    if 'I' in inputType:
        nodeCount = int(input())
        elements = np.array([Node(ix, int(x), 0) for ix, x in enumerate(input().split(" "))])
    elif 'F' in inputType:
        fileName = input()

        if 'a' in fileName:
            return
        
        with open("./test/%s" % (fileName), "r") as file:
            nodeCount = int(file.readline())
            elements = np.array([Node(ix, int(x), 0) for ix, x in enumerate(file.readline().split(" "))])
    
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

# Driver Code
if __name__ == "__main__":
    main()
