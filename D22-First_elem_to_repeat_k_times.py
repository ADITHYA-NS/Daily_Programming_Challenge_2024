#Day 22
#First Element to Repeat k Times
def firstelem(array,k):
    hash_map={}
    for i in range(len(array)):
        if array[i] not in hash_map:
            hash_map[array[i]]=1
        else:
            hash_map[array[i]]+=1
    for j in array:
        if hash_map[j]==k:
            return j
    return -1
array=[2, 3, 4, 2, 2, 5, 5]
k=2
print("First element that appears k times:",firstelem(array,k))
