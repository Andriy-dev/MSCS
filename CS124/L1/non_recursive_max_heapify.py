from math import *
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

            if l <= self.size and self.heap[l - 1] > self.heap[i - 1]:
                return False
            if r <= self.size and self.heap[r - 1] > self.heap[i - 1]:
                return False
        
        return True

    def left_child(self,i):
        return (2*i)
    
    def right_child(self,i):
        return (2*i + 1)

    def build_max_heap(self):
        for i in range(floor(self.size/2),0,-1):
            self.heapify_at(i)

    def heapify_at(self,i,verbose=False):
        if i > self.size:
            return

        swap = True
        while swap:    
            swap = False

            l = self.left_child(i)
            r = self.right_child(i)

            if l <= self.size and self.heap[l - 1] > self.heap[i - 1]:
                largest = l
            else:
                largest = i

            if r <= self.size and self.heap[r - 1] > self.heap[largest - 1]:
                largest = r
            
            if largest != i:
                self.heap[largest - 1],self.heap[i - 1] = self.heap[i - 1],self.heap[largest - 1]
                if verbose:
                    self.print_heap()
                i = largest
                swap = True

if __name__ == '__main__':

    h = Heap([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    h.print_heap()
    h.build_max_heap()
    h.print_heap()
        