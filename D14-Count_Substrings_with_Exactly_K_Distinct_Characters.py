#Day 14
#Count Substrings with Exactly K Distinct Characters
def count_of_substr(s,k):
    n=len(s)
    res=0
    for i in range(n):
        dist_count=0
        cnt=[0]*26 
        for j in range(i, n):
            if cnt[ord(s[j])-ord('a')]==0:
                dist_count+=1
            cnt[ord(s[j])-ord('a')]+=1
            if dist_count==k:
                res+=1
            if dist_count>k:
                break
    return res
s="abc"
k=2
res=count_of_substr(s,k) 
print("Count:",res)

