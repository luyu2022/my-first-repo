"""
Binary search is based on the sorted list.
so using bubble sort, insertion sort or merge sort to sort the list first
"""
# a function that takes a list and target parameter
# multiple variable: middle,start,end,steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track  target position

def binary_search(list,target):
    start=0
    probe=0
    end=len(list)
    steps=0

    while(start<=end):
        print('steps',steps,str(list[start:end+1]))
        probe=(start+end)//2
        steps=steps+1
        if (target==list[probe]):
            return probe
        elif (target<=list[probe]):  #for ascending order
            end=probe-1
        else:
            start=probe+1
    return -1



my_list=[1,2,3,4,5,6,7,8,9,10]
# my_list2=[10,9,8,7,6,5,4,3,2,1]
target_value=28
binary_search(my_list,target_value)
# binary_search(my_list2,target_value)