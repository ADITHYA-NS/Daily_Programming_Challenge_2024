#Day 13
# Longest Palindrome substring
def LongestPalindrome(s):
    if len(s)==0 or len(s)==1:
        return s
    longest=""
    for i in range(1,len(s)):
        l=h=i
        while (l>=0) and (h<=len(s)-1) and (s[l]==s[h]) :
            l-=1
            h+=1
        if h-l-1>len(longest):
            longest=s[l+1:h]
        l=i-1
        h=i
        while(l>=0) and (h<=len(s)-1) and (s[l]==s[h]):
            l-=1
            h+=1
        if h-l-1>len(longest):
            longest=s[l+1:h]
    return longest
s="babad"
longest=LongestPalindrome(s)
print("Longest Palindrome:",longest)
