#day-2
#find missing num
def FindMissingNum(array):
    n=len(array)+1 #length of array+1 to find the range
    total=(n*(n+1))//2 #finds the sum of all numbers from 1 to n
    total_in_given_array=0
    for i in array:
        total_in_given_array=total_in_given_array+i #find the sum of all elements in the array
    return total-total_in_given_array #missing element

array= [1, 2, 4, 5]
missing_value=FindMissingNum(array)
print("Missing Value:",missing_value)
