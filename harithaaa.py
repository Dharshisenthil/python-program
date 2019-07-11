# Simple Python 3 program to find subarrays 
# whose averages are equal 
  
# Finding two subarrays with equal average. 
def findSubarrays(arr, n): 
  
    found = False
    lsum = 0
    for i in range(n - 1): 
      
        lsum += arr[i] 
        rsum = 0
        for j in range(i + 1, n): 
            rsum += arr[j] 
  
        # If averages of arr[0...i] and  
        # arr[i+1..n-1] are same. To avoid 
        # floating point problems we compare  
        # "lsum*(n-i+1)" and "rsum*(i+1)"  
        # instead of "lsum/(i+1)" and  
        # "rsum/(n-i+1)" 
        if (lsum * (n - i - 1) == rsum * (i + 1)): 
            print("From", "(", 0, i, ")", 
                  "to", "(", i + 1, n - 1, ")") 
            found = True
  
    # If no subarrays found 
    if (found == False): 
        print("Subarrays not found") 
  
# Driver code 
if __name__ == "__main__": 
      
    arr = [1, 5, 7, 2, 0] 
    n = len(arr) 
    findSubarrays(arr, n) 
