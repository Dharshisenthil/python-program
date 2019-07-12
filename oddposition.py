# Python3 implementation to 
# arrange odd and even numbers 
  
def arrangeOddAndEven(arr,  n): 
      
    oddInd = 1
    evenInd = 0
    while (True): 
          
        while (evenInd < n and arr[evenInd] % 2 == 0): 
            evenInd += 2
               
        while (oddInd < n and arr[oddInd] % 2 == 1): 
            oddInd += 2
               
        if (evenInd < n and oddInd < n): 
                temp = arr[evenInd] 
                arr[evenInd] = arr[oddInd] 
                arr[oddInd] = temp; 
               
        else: 
            break
   
# function to print the array 
def printArray(arr,  n): 
    for i in range(0,n): 
        print(arr[i] , "",end="") 
  
       
# Driver function  
def main(): 
    arr = [ 1, 2, 3, 4, 5, 6, 7 ] 
    n = 7
   
    print("Original Array: ",end="") 
    printArray(arr, n) 
   
    arrangeOddAndEven(arr, n) 
   
    print("\nModified Array: ",end="") 
    printArray(arr, n) 
      
if __name__ == '__main__': 
    main()
