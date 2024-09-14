#day-6
#Find all subarrays with zero sum
def find_subarrays(array): 
    temp_dict={}
    output_list=[]
    total=0

    for i in range(len(array)):
        total+=array[i]
        if total==0:
            output_list.append((0,i))
        index=[]
        if total in temp_dict:
            index=temp_dict.get(total)
            for j in range(len(index)):
                output_list.append((index[j]+1,i))
        index.append(i)
        temp_dict[total]=index
    return output_list

            


array=[1, 2, -3, 3, -1, 2]
output=find_subarrays(array)
print("Index of subarrays:",output)
