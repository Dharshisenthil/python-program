# Python3 program to generate largest possible 
# number with given digits 
  
# Function to generate largest possible 
# number with given digits 
def findMaxNum(arr,n) : 
  
    # sort the given array in 
    # descending order 
    arr.sort(reverse = True) 
  
    # initialize num with starting 
    # element of an arr 
    num = arr[0] 
  
    # generate the number 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
  
    return num 
  
# Driver code 
if __name__ == "__main__" : 
      
    arr = [1,2,3,4,5,0] 
  
    n = len(arr) 
  
    print(findMaxNum(arr,n)) 
