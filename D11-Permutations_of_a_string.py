# Day 11
# Permutations of a string

def Permutations(string_arr,freq_map):
    temp=[]
    output=[]
    def backtracking(temp,string_arr,freq_map):
        ans=''.join(temp)
        if (len(temp)==len(string_arr) and ans not in output ):
            output.append(ans)
            return
        else:
            for i in range(len(string_arr)):
                if freq_map[i]=="T":
                    continue
                freq_map[i]="T"
                temp.append(string_arr[i])
                backtracking(temp,string_arr,freq_map)
                temp.pop(-1)
                freq_map[i]="F"
    backtracking(temp,string_arr,freq_map)
    return output

input="abc"
string_arr=list(input)
freq_map={}
for i in range(len(string_arr)):
    freq_map[i]="F"
print(Permutations(string_arr,freq_map))
