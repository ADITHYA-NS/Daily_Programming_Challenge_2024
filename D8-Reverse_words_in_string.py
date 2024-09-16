# Day 8 
#Reverse the words in a string
def ReverseWords(s):
    i=j=0
    s=s.strip()
    length=len(s)
    temp_array=[]
        
    while (i<length):
        while (i<length and s[i]==' '):
            i+=1
        j=i
        while (j<length and s[j]!=' '):
            j+=1
        if i<j:
            temp_array.append(s[i:j])
        i=j
    result=""
    for i in range(len(temp_array)-1,-1,-1):
        result+=temp_array[i]
        if i!=0:
            result+=" "
    return result

s= "the sky is blue"
result=ReverseWords(s)
print("Reversed Words: '"+result+"'")
