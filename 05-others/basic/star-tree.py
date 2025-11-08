""" 
Create a pattern similar to this structure
  *  
 ***
*****

"""

def star_tree(height):
    star = 1
    col = height * 2
    for row in range(height):
        spaces = (col - star) // 2
        print(spaces * " " + star * "*" + spaces * " ")
        star +=2
    
star_tree(3)