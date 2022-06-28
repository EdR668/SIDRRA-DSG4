class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap = [0]*4

    def insert(self, food):
        if self.current_size == 0:
            self.heap[1] = food
            self.current_size +=1
            return

        if self.current_size == len(self.heap)-1:
            self.heap += [0]*(((len(self.heap)-1)*2+1)-(len(self.heap)-1))
        
        hole = self.current_size+1
        while hole//2 != 0 and food.tiempoCaducidad < self.heap[hole//2].tiempoCaducidad:
            self.heap[hole] = self.heap[hole//2]
            hole //= 2
        self.heap[hole] = food
        self.current_size += 1

    def delete_min(self):
        if self.current_size == 0:
            print("Error. ¡No hay más elementos!")
            return

        minFood = self.heap[1]
        self.heap[1], self.heap[self.current_size] = self.heap[self.current_size], 0
        self.current_size -= 1
        self.percolate_down(1)

        return minFood

    def percolate_down(self, hole):
        tmp = self.heap[hole]

        while hole*2 <= self.current_size:
            child = hole*2
            if child != self.current_size and self.heap[child+1].tiempoCaducidad < self.heap[child].tiempoCaducidad:
                child += 1
            if self.heap[child].tiempoCaducidad < tmp.tiempoCaducidad:
                self.heap[hole] = self.heap[child]
            else:
                break
            
            hole = child

        self.heap[hole] = tmp