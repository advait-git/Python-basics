def arr01():
    arr =  [2,6,5,8,11]
    target = 14
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            if arr[i] +arr[j]==target:
                print(i,j)
# arr01()
def arr02():
    arr= [1,3,5,7,8,11]
    k=8

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                print(i , j)
# arr02()
def arr03():
    arr = [1,2,3,4,5,6,7,8]
    k = 15
    hmap = {}
    for i in range(len(arr)):
        num = arr[i]
        diff =k-num
        if diff in hmap:
            print(hmap[diff],i)
            break
        hmap[num] = i
        print(hmap)
# arr03()
def arr04():
    arr = [1,2,3,5,4,6,8,6,11,10]
    k=160
    i=0
    j=len(arr)-1
    arr.sort()

    while i<j:
        s = arr[i]+arr[j]
        if s==k:
            return True
        elif s<k:
            i+=1
        else:
            j-=1
    return False
# print(arr04())
def swap(arr,i,j):
    arr[i],arr[j]  = arr[j],arr[i]
def arr05():
    arr = [1,3,2,5,4,5,7,8]
    for i in range(len(arr)):
        m=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[m]:
                m=j
        swap(arr , m , i)
        print(arr)
# arr05()
def arr06(): #bubble sort
    arr = [13,9,40,23,44,32]
    for i in range(len(arr)-1,-1,-1):
        swapd = 0
        for j in range(i):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                swapd+=1
        if (swapd ==0):
            break        
    print(arr)
# arr06()
def arr07(): #insertion sort
    arr = [1,2,3,4,5]
    for i in range(len(arr)):
       j=i
       while j>0 and arr[j-1]>arr[j]:
           swap(arr,j-1,j)
           j-=1
       print(arr)
# arr07()
def arr08():
    arr=[2,0,2,1,1,0]
    z=0
    o=0
    t=0
    for i in arr:
        if i==0:
            z+=1
        if i==1:
            o+=1
        if i==2:
            t+=1
    for i in range(z):
        arr[i] = 0
    for i in range(z,z+o):
        arr[i]=1
    for i in range(z+o,z+o+t):
        arr[i]=2
    print(arr)
# arr08()
def arr09():
    arr = [1,0,0,1,1,2,1,2,0]
    i=0
    j=0
    k=len(arr)-1
    while(j<=k):
        if arr[j]==0:
            swap(arr,i,j)
            i+=1
            j+=1
        elif arr[j]==1:
            j+=1
        else:
          swap(arr,j,k)
          k-=1  
    print(arr)
# arr09()
def arr10():
    