import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if len(x)!=len(y): # it will check the lenght of the array and select only which is same if not then raised a error 
        raise ValueError("vector must be in same length")
    x=np.array(x) # it will create an array of x 
    y=np.array(y)
    result=np.sum(x*y) # it will first multiply the dot procudt across array then sum up 
    return float(result)
    
            
    
