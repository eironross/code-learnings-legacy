"""
Data Structure and Algorithms 

To fully understand the concept of data structure and algorithms

"""
from math import floor


class BasicAlgorithms:
    def __init__(self, array: list[int], start: int, end: int) -> None:
        self.array = array
        self.start = start
        self.end = end
        
    # Search Algorithms
    def linear_search(self, target: int):
        while(self.start <= self.end):
            try: 
                if self.array[self.start] == target:
                    return f"Found it on index {self.start}"
                # print(f"Not in arr[{self.start}]")
                self.start+=1
            except IndexError as e:
                return -1
    
    
    def binary_search(self, target: int) -> str:
        if (self.start > self.end):
            return -1
        
        middle = floor((self.start + self.end) / 2)
        try:
            if self.array[middle] == target:
                return f"I found it @ Index: {middle}" 
            
            if self.array[middle] > target:
                print("Lower")
                return BasicAlgorithms(array, self.start, middle-1).binary_search(target)
            
            if self.array[middle] < target:
                print("Higher")
                return BasicAlgorithms(array, middle+1, self.end).binary_search(target)
            
        except IndexError as e:
            return -1

    def interpolation_search(self, target: int) -> str:
        
            while(target>= self.array[self.start] and target <= self.array[self.end] and self.start <= self.end):
                
                # Formula for computing for the probe
                probe = self.start + (self.end - self.start) * (target - self.array[self.start]) // (self.array[self.end] - self.array[self.start])
                
                print("Current Probe: ", probe)
                
                if self.array[probe] == target:
                    return f"I found it @ Index: {probe}"
                
                # Narrow down the search area
                elif self.array[probe] < target:
                    self.start = probe + 1
                
                else: 
                    self.end = probe - 1

            return -1
        
if __name__ == "__main__":
    array = [i+ 1 for i in range(0, 1000000)]
    data = BasicAlgorithms(array, start=10, end=len(array)-1)
    print(data.interpolation_search(target=9998))
 