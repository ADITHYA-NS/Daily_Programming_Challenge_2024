#Day 7
#Trapping rain water
def TrapRainWater(array):
    length=len(array)
    trapped_water=0
    for i in range(length):
        j=i
        max_left=0
        max_right=0
        while j>=0:
            max_left=max(max_left,array[j])
            j-=1
        j=i
        while j<length:
            max_right=max(max_right,array[j])
            j+=1
        trapped_water+=min(max_left,max_right)-array[i]
    return trapped_water

array= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapped_water=TrapRainWater(array)
print("Trapped water:",trapped_water)
