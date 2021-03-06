def SellectSort(list):
    # list = [4,1,9,13,34,26,10,7,4]
    m = len(list)
    if m < 2:   # 如果是空表或只有一个元素，返回
        return list 
    for i in range(m):  # 对每一个元素
        index = i   # 当前元素序号
        for j in range(i,m):    # 从列表中剩余的元素中选择最小的
            if list[j] < list[index]:
                index = j
        if i != index:  # 如果当前元素大于选出的最小元素，交换：将最小元素与当前元素交换
            list[index],list[i] = list[i],list[index]
    return list
        
if __name__== '__main__':
    list_0 = [4,1,9,13,34,26,10,7,4]
    list_1 = SellectSort(list_0)
    print list_1