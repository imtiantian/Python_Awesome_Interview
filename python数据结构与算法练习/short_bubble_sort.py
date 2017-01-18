#-*- coding=utf-8 -*-
#冒泡排序
def short_bubble_sort(list):
    exchanges=True
    pass_num=len(list)-1
    while pass_num>0 and exchanges:
        exchanges=False
        for i in range(pass_num):
            if list[i]>list[i+1]:
                exchanges=True
                list[i],list[i+1]=list[i+1],list[i]
        pass_num=pass_num-1
if __name__=='__main__':
    list=[2,4,3,9,5,8,7,6,11,10]
    short_bubble_sort(list)
    print list


def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        # temp = a_list[fill_slot]
        # a_list[fill_slot] = a_list[pos_of_max]
        # a_list[pos_of_max] = temp
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)