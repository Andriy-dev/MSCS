class Heap:
    def __init__(self,a):
        self.heap=a
        self.size = len(self.heap)
    
    def print_heap(self):
        print(self.heap,self.is_heap())

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

    h = Heap([27,17,3,16,13,10,1,5,7,12,4,8,9,0])
    h.print_heap()
    h.heapify_at(3,True)
        