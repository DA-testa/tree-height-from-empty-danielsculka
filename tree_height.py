# python3
# Dāniels Čulka 221RDB304

import sys
import threading

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

        node_height = 1
        path = [el]
        while el.parent != -1:
            el = parents[el.parent]

            if el.height != 0:
                node_height = node_height + el.height
                break
            
            path.append(el)
            node_height += 1
            
        for p in path:
            p.height = node_height
            node_height -= 1

    return max([p.height for p in parents])



def main():
    inputType = input()
    elements = []
    nodeCount = -1

    if 'I' in inputType:
        nodeCount = int(input())
        elements = [Node(ix, int(x)) for ix, x in enumerate(input().split(" "))]
    elif 'F' in inputType:
        fileName = input()

        if 'a' in fileName:
            return
        
        with open("./test/%s" % (fileName), "r") as file:
            nodeCount = int(file.readline())
            elements = [Node(ix, int(x)) for ix, x in enumerate(file.readline().split(" "))]

    height = compute_height(nodeCount, elements)
    
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
