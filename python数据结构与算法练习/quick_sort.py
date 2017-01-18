# # -*- coding=utf-8 -*-
#
# #固定基准元快速排序
# def sub_sort(array,low,high):
#     key = array[low]
#     while low<high:
#         while low<high and array[high]>=key:
#             high-=1
#         while low<high and array[high]<key:
#             array[low]=array[high]
#             low+=1
#             array[high]=array[low]
#
#     array[low]=key
#     return low
# def quick_sort(array,low,high):
#     if low<high:
#         key_index = sub_sort(array,low,high)
#         quick_sort(array,low,key_index)
#         quick_sort(array,key_index+1,high)
##
#第二种写法，极简
# if __name__ == '__main__':
#     array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
#     print array
#     # quick_sort(array,0,len(array)-1)
#     quickSort(array)
#     print array
# quickSort()
def quicksort(arg):
    if arg==[]:
        return []
    big=[]
    small=[]
    middle=arg[0]
    for i in arg[1:]:
        if i<=middle:
            small.append(i)
        else:
            big.append(i)
    return quicksort(small)+[middle]+quicksort(big)
print quicksort([12,14,25,23,2,17,13,25,34,777])
def partition(sort_list, left, right):
    key = sort_list[left]
    while left < right :
        while left < right and sort_list[right] >= key :
            right -= 1
        if left < right and sort_list[right] < key:
            sort_list[left] = sort_list[right]
            left += 1
        while left < right and sort_list[left] >= key:
            left += 1
        if left < right and sort_list[left] < key:
            sort_list[right] = sort_list[left]
            right -= 1
    sort_list[left] = key
    return left
def quickSort(sort_list, left, right):
    if left < right :
        i = partition(sort_list, left, right)
        quickSort(sort_list, left, right-1)
        quickSort(sort_list, left+1, right)
    return sort_list