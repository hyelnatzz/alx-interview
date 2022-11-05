#!/usr/bin/python3

"""
a module for creating a pascal triangle
"""

def pascal_triangle(depth):
    """
    :input: triangle depth
    :returns: list of list
    """
    if depth <= 0:
        return [] 
    
    triangle = [[1], [1,1]]

    while len(triangle) < depth:
        temp_lst = [1]
        last_val = triangle[-1]
        for i in range(len(last_val) - 1):
            temp_lst.append(last_val[i] + last_val[i+1])
        
        temp_lst.append(1)
        triangle.append(temp_lst)
    
    return triangle