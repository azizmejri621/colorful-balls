from array import*
t=int(input("type the number of testcases: ")) #number_of_testcases
arr=array('i',[])
for i in range (t):
    n=int(input("type the length of the array: ")) #length_of_the_array
    for i in range(n):
        a=int(input())
        arr.append(a)
    if len(arr)==1:
        s=1

    else:
        s=0
        for x in arr:
            if arr[x]==arr[x+1]:
                s=s+1
        arr *= 0
    print(s)