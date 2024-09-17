# Day-9
# Longest Common Prefix
def LongestCommonPrefix(array):
    array.sort()
    f=array[0]
    l=array[-1]
    new=""
    for i in range(min(len(f),len(l))):
        if f[i]==l[i]:
            new+=f[i]
        else:
            return new
    return new

array=  ["flower", "flow", "flight"]
new_prefix=LongestCommonPrefix(array)
print("Prefix:",new_prefix)


