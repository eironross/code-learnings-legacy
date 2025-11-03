
    
def linear_search(arr: list[int], target: int, start: int , end: int ):
    while(start <= end):
        if arr[start] == target:
            return f"Found it on index {start}]"
        # print(f"Not in arr[{start}]")
        start+=1
    return f"Input was not found"
        


if __name__ == "__main__":
    linear_search()