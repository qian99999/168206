def SellectSort(list):
    # list = [4,1,9,13,34,26,10,7,4]
    m = len(list)
    if m < 2:   # ����ǿձ��ֻ��һ��Ԫ�أ�����
        return list 
    for i in range(m):  # ��ÿһ��Ԫ��
        index = i   # ��ǰԪ�����
        for j in range(i,m):    # ���б���ʣ���Ԫ����ѡ����С��
            if list[j] < list[index]:
                index = j
        if i != index:  # �����ǰԪ�ش���ѡ������СԪ�أ�����������СԪ���뵱ǰԪ�ؽ���
            list[index],list[i] = list[i],list[index]
    return list
        
if __name__== '__main__':
    list_0 = [4,1,9,13,34,26,10,7,4]
    list_1 = SellectSort(list_0)
    print list_1