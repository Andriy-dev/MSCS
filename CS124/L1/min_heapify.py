# Min heapify from 6.2-2

from binarytree import Node
from binarytree import build

class Heap:
    def __init__(self,a):
        self.heap=a
        self.size = len(self.heap)
    
    def print_heap(self):
        print(self.heap,self.is_heap())
        root = build(self.heap)
        print(root)

    def is_heap(self):
        
        for i in range(1,self.size + 1):
            l = self.left_child(i)
            r = self.right_child(i)

            if l <= self.size and self.heap[l - 1] < self.heap[i - 1]:
                #print(i,l)
                return False
            if r <= self.size and self.heap[r - 1] < self.heap[i - 1]:
                #print(i,r)
                return False
        
        return True

    def left_child(self,i):
        return (2*i)
    
    def right_child(self,i):
        return (2*i + 1)

    def heapify_at(self,i,verbose=False):
        if i > self.size:
            return

        l = self.left_child(i)
        r = self.right_child(i)

        if l <= self.size and self.heap[l - 1] < self.heap[i - 1]:
            smallest = l
        else:
            smallest = i

        if r <= self.size and self.heap[r - 1] < self.heap[smallest - 1]:
            smallest = r
        
        if smallest != i:
            self.heap[smallest - 1],self.heap[i - 1] = self.heap[i - 1],self.heap[smallest - 1]
            if verbose:
                self.print_heap()
            self.heapify_at(smallest,verbose)

if __name__ == '__main__':

    h = Heap([27,17,3,16,13,10,1,5,7,12,4,8,9,0])
    h.print_heap()

    while not h.is_heap():
        for i in range(1, h.size + 1):
            #print(f"Heapifying at {i}")
            h.heapify_at(i)
            #h.print_heap()

    h.print_heap()