#Day 15
#Longest Substring Without Repeating Characters

def LongestSubstring(s):
    hash_map={}
    i=j=0
    max_len=0
    while j<len(s):
        if s[j] not in hash_map:
            hash_map[s[j]]=j
        else:
            if hash_map[s[j]] >=i :
                i=hash_map[s[j]]+1
            hash_map[s[j]]=j
            
        max_len=max(max_len,j-i+1)
        j+=1
    return max_len

s="pwwkew"
print("Length of longest substring without repeating chars:",LongestSubstring(s))
