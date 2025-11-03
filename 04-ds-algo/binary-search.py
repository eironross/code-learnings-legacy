from math import floor

def binary_search(arr: list[int] , target:int , start:int , end: int) -> str:
    
    if (start > end):
        return "Not Found"
    
    middle = floor((start + end) / 2)
    
    print(arr[middle])
    
    if arr[middle] == target:
        print("Hello")
        return f"I found it @ Index: {middle}" 
    
    if arr[middle] > target:
        print("Lower")
        return binary_search(arr, target, start, middle-1)
    
    if arr[middle] < target:
        print("Higher")
        return binary_search(arr, target, middle+1, end)


    

if __name__ == "__main__":
    binary_search()