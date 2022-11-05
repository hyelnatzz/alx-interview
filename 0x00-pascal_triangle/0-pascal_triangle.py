
def pascal_triangle(depth):
    if depth <= 1:
        return [1] 
    
    triangle = [[1], [1,1]]

    while len(triangle) < depth:
        temp_lst = [1]
        last_val = triangle[-1]
        for i in range(len(last_val) - 1):
            temp_lst.append(last_val[i] + last_val[i+1])
        
        temp_lst.append(1)
        triangle.append(temp_lst)
    
    return triangle