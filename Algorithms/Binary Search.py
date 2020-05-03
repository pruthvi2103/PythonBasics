'''
Binary Search Algorithms for arrays, lists etc.

Usually the best algorithm to use when a set range of array is given like 0 to n and an element is to be found in a sorted or uniformly odered array

Worst case timecomplexity : O(Log(n))

Divide and Conquer Algorithm

Requires a sorted or a uniform pattern array!!

Following function is for ascending array reverse the > in line 24 for desc array

'''

def binarySearch(l,r,svalue,arr):
    if l<=r:
        m = (l + r)//2
        #print("l = %d \n r = %d \n svalue = %d \n m = %d " %(l,r,svalue,m))
        if arr[m] == svalue:
            return m
        elif arr[m] > svalue:
            return binarySearch(l,m-1,svalue,arr)
        elif arr[m] < svalue:
            return binarySearch(m+1,r,svalue,arr)   
    else:
        return -1 


#driver 

A = [1,2,3,4,5,6,7,8]
s = 8

print("The Element is present at position: %d of the Array" % binarySearch(0,len(A),s,A))
