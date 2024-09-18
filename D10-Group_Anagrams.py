# Day-10
# Anagrams
def Anagrams(array):
    hash_map={}
    for i in array:
        sorted_string="".join(sorted(i))

        if sorted_string not in hash_map:
            hash_map[sorted_string]=[i]
        else:
            hash_map[sorted_string].append(i)
    output=list(hash_map.values())
    return output
    
array=["abc", "bca", "cab", "xyz", "zyx", "yxz"]
output=Anagrams(array)
print(output)
        
        
