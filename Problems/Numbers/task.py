# put your python code here
def multiply(*kargs):
    result = 1
    for n in kargs:
        result *= n
    return result
