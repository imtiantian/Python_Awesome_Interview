# -*- coding=utf-8 -*-
# 合并排序
def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0;j=0;k=0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)