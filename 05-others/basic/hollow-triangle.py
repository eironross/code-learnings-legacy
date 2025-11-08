"""
*
**
* *
*  *
*   *
******

Create this pattern in python the hollow triangle
"""

def hollow_triangle(height):
    for i in range(1,height+1):
        if i == 1 or i == 2 or i == height:
            print("*" * i)
        else:
            print("*" + " " * (i-2) + "*")

hollow_triangle(15)