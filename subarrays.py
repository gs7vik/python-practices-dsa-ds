# Python3 code to print all possible subarrays 
# for given array using recursion
# Recursive function to print all possible subarrays 
# for given array
def printSubArrays(arr, start, end):

    # Stop if we have reached the end of the array    
    if end == len(arr):
        return

    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)

# Driver code
arr = [1, 2, 3]
#
# printSubArrays(arr, 0, 0)

#brute force solution
def print_all_subarrays(arr):
    n = len(arr)
    # Fix starting index i
    for i in range(n):
        # Fix ending index j
        for j in range(i, n):
            # Print subarray from i to j
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            print(sum)

# Example
arr = [1, 2, 3, 4]
print_all_subarrays(arr)

