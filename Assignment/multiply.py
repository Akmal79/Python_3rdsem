# 1.Write a python function to multiply all elements in a list

def multiply_elements(lst):
    result = 1
    for element in lst:
        result *= element
    return result

l=[1,2,3,4,5]
print(multiply_elements(l)) #output:120