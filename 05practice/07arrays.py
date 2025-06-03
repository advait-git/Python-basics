def arr01():
    fruits = ['apple', 'banana', 'orange']
    print(fruits)
    for i in range(len(fruits)):
        print(str(i)+":"+fruits[i])
    for inx,fruit in enumerate(fruits):
        print(str(inx),fruit)
# arr01()
def arr02():
    s=[65,75,176,88,99]
    l=0
    for i in range(len(s)):
        if s[i]>l:
            l = s[i]
    print(l)
# arr02()
def arr03():
    arr= [0]*10
    print(arr)
    for i in range(len(arr)):
       arr[i] = (i+1)*2
    print(arr)    
# arr03()
def arr04():
    arr = [1,2,3,4,55,66,7,8,9]
    arr.sort()
    print(arr)
    l = len(arr)
    print(arr[l-1])
# arr04()
def arr05():
    arr = [1,2,3,4,55,66,64,7,8,9]
    largest = arr[0]
    second = -1
    for i in arr:
        if i>largest:
            second=largest
            largest=i
        elif largest>i>second:
            second=i
    print(second)
# arr05()
def arr06():
    n=[1,2,3,4,5,7,7]
    for i in range(1,len(n)):
        if n[i-1]<=n[i]:
            continue
        else:
            print("not sorted!")
            return
    print("sorted")
# arr06()   
def arr07():
    n=[1,2,2,3,4,4,5,6,6]
    unique = sorted(set(n)) #converted the set to sorted list
    print(unique)

    for i in range(len(unique)):
        n[i] = unique[i]
    print(n)
# arr07()
def arr08():
    arr= [1,2,2,3,3,4,4,5,6,7]
    i=0
    for j in range(1,len(arr)):
        if arr[i]==arr[j]:
            continue
        else:
            i+=1
            arr[i]=arr[j]
    print(arr)
# arr08()
def arr09():
    arr=[1,2,3,4,5,6]
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1] = temp
    print(arr)
# arr09() #in the arr we are using space o(N) but extra space is o(1)
def arr10():
    arr=[1,2,3,4,5,6,7]
    n=3
    n=n%len(arr) # if no. of n is greater than arr length then also work
    # get temp
    temp = [0]*n
    for i in range(n):
        temp[i]=arr[i]
    print(temp)
    # temp = [1,2,3]
    # shift the rest
    for i in range(n,len(arr)):
        arr[i-n]=arr[i]
    print(arr)
    # add the temp
    for i in range(len(temp)):
        arr[len(arr)-n+i]=temp[i]
    print(arr)
# arr10()
def arr11():
    arr=[1,2,3,4,5]
    left = 0
    right = len(arr)-1
    temp = 0
    while(left<right):
        temp = arr[left]
        arr[left]=arr[right]
        arr[right] = temp
        left+=1
        right-=1
    print(arr)
# arr11()
def rev(arr,left,right):
    temp = 0
    while left<right:
        temp = arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        # arr[left],arr[right]=arr[right],arr[left] easy swap
        left+=1
        right-=1
def arr12():
    arr=[1,2,3,4,5,6,7]
    d = 3
    d = d % len(arr) 
    # reverse till nth
    rev(arr,0,d-1)
    # reverse till arr.length-nth
    rev(arr,d,len(arr)-1)
    # reverse whole
    rev(arr,0,len(arr)-1)
    print(arr)
# arr12()
# do for rotate right

def arr13():
    arr = [1,2,3,0,0,8,7,0,5]
    l = len(arr)
    # define temp
    temp = []
    # get all nz no.s
    for i in arr:
        if i!=0:
            temp.append(i)
    # put all the temp in the arr[i]
    for i in range(len(temp)):
        arr[i]=temp[i]
    # at back print 0 in rest
    for i in range(len(temp),l):
        arr[i]=0
    print(arr)
# arr13()
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def arr14():
    arr = [1,3,4,5,0,0,7,6,0,9]
    j=-1
    for i in range(len(arr)):
        if arr[i] == 0:
            j=i
            break
    if j==-1:
        print(arr)
        return
            
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            swap(arr,i,j)
            j+=1
    print(arr)
# arr14()
def arr15():
    n=[1,2,3,33,5,6,7]
    m=33
    for i in range(len(n)):
        if n[i]==m:
            print(i)
            break
# arr15()
def arr16():
    n1 = [1,2,3,4,5,5,6]
    n2 = [3,4,6,7,8,9,10]
    s = set()
    for i in n1:
        s.add(i)
    for i in n2:
        s.add(i) 
    print(s)
# arr16()
def arr17():
    n1 = [1,2,3,4,5]
    n2 = [2,3,4,5,6,7,9,9]
    i=0
    j=0
    union=[]
    while i<len(n1) and j<len(n2):
        if n1[i]<=n2[j]:
            union.append(n1[i])
            i+=1
        else:
            if len(union)==0 or union[-1]!=n2[j]:
                union.appned(n2[j])
            j+=1

    while i<len(n1):
        if union[-1]!=n1[i]:
            union.append(n1[i])
        i+=1

    while j<len(n2):
        if union[-1]!=n2[j]:
            union.append(n2[j])
        j+=1
    print(union)
# arr17()
def arr18():
    ans = []
    arr1=[1,2,3,3,4,4,5,7]
    arr2=[1,2,3,4,4,6,7]
    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]==arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    print(ans)
# arr18()
def arr19():
    N=5
    arr=[1,2,3,4]
    for i in range(N-1):
        if arr[i]!=i+1:
            print(i+1)
            return
    print(N)
# arr19()
def arr20():
    arr = [1,1,0,0,1,1,1,1,0,1]
    count=0
    maxi=0
    for i in arr:
        if i==1:
           count+=1
        else:
           count=0
        maxi = max(maxi,count)
    print(maxi)
# arr20()
def arr21():
    arr=[1,1,2,3,3,4,4]
    for i in range (len(arr)):
        num = arr[i]
        count=0
        for j in range(len(arr)):
            if arr[j]==num: 
                count+=1
        if count==1:
            print(num)
#arr21()
def arr22():
    arr = [1,1,2,3,3,4,4]
    n=len(arr)
    maxi = max(arr)
    hash = [0]*(maxi+1)
    for i in arr:
        hash[i]+=1
    for i in arr:
        if hash[i]==1:
            return i
    return -1
# print(arr22())
def arr23():

    arr = [1,1,2,2,3,4,4]
    xorr = 0
    for num in arr:
        xorr ^=num
def arr24():
    arr = [1,1,2,3,3,1,1,1,4,5,6]
    k=3
    l=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
                s+=arr[j]
                if s==k:
                    l = max(l,j-i+1)
    print(l)
# arr24()
def arr25():
    arr = [1,1,2,3,3,1,1,1,4,5,6]
    k=3
    i=0
    j=0
    sum =arr[0]
    l = 0
    n = len(arr)
    while j<n:
        while(i<=j and sum>k):
            sum -= arr[i] 
            i+=1
        if sum == k :
            l = max(l , j-i+1)
        j+=1
        if j<n:
            sum+=arr[j]
    return l
# print(arr25())
