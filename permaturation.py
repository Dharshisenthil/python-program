# Python3 code to make a permutation 
# of numbers from 1 to n using  
# minimum changes. 
  
def makePermutation (a, n): 
  
    # Store counts of all elements. 
    count = dict() 
    for i in range(n): 
        if count.get(a[i]): 
            count[a[i]] += 1
        else: 
            count[a[i]] = 1; 
          
    next_missing = 1
    for i in range(n): 
        if count[a[i]] != 1 or a[i] > n or a[i] < 1: 
            count[a[i]] -= 1
              
            # Find next missing element to put 
            # in place of current element. 
            while count.get(next_missing): 
                next_missing+=1
              
            # Replace with next missing and 
            # insert the missing element in hash. 
            a[i] = next_missing 
            count[next_missing] = 1
  
# Driver Code 
A = [ 2, 2, 3, 3 ] 
n = len(A) 
makePermutation(A, n) 
  
for i in range(n): 
    print(A[i], end = " ") 
