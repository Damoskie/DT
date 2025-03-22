def OddOccuring(arr):
    res=0
    for elements in arr:
        res=res^element
    return res
arr=[]
n=int(input("Enter array size")) 
while(n):
    num=int(input("Enter number:"))
    arr.append(num)
    n-=1
print(arr)
print("OddOcurring number is",OddOccuring(arr))       