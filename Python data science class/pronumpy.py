import numpy as np 

def numpy_operations():
    array1=np.array([2,4,6,8,10])
    array2=np.array([1,3,5,7,9])

    #elemententwise operations

    array_sum=array1+array2
    array_mul=array1-array2
    array_prod=array1*array2
    array_div=array1/array2

    #results print
    print("array1 and array 2 are :",array1,array2)
    print("sum of array is :",array_sum)
    print("product of the array is :",array_prod)
    print("Multiplication of the array is :",array_mul)
    print("Division of the arrays are :",array_div)

    #basic statistics
    mean_value1=np.mean(array1)
    mean_value2=np.mean(array2)
    max_value1=np.max(array1)
    min_value1=np.min(array1)
    min_value2=np.min(array2)
    max_value2=np.max(array2)

    print("mean value is :",mean_value1,mean_value2)
    print("minimum value is :",min_value1,"and",min_value2)
    print("maximum value is :",max_value1,"and",max_value2)

numpy_operations()
    
    
