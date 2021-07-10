def leftrotate(arr,r):
    n = len(arr)
    temp1 = []
    for i in range(r,n):
        temp1.append(arr[i])
    for i in range(r):
        temp1.append(arr[i])
    return temp1
    

def rightrotate(arr2,r):
    n1 = len(arr2)
    temp2 = []
    for i in reversed(range(n1-r,n1)):
        temp2.append(arr2[i])
    for i in range(n1-r):
        temp2.append(arr2[i])
    return temp2


arr = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7]
r = 6
print("Actual Array is",arr2)
print("Array Left  Rotation by ",r," ",leftrotate(arr,r))
print("Array Right Rotation by ",r," ",rightrotate(arr2,r))
# rightroatate [7,6,1,2,3,4,5] by 2  
# leftrotate [3,4,5,6,7,1,2] by 2