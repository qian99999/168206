def QuickSort(myList,start,end):
    #�ж�low�Ƿ�С��high,���Ϊfalse,ֱ�ӷ���
    if start < end:
        i,j = start,end
        #���û�׼��
        base = myList[i]

        while i < j:
            #����б��ߵ���,�Ȼ�׼��������,��ǰ��һλֱ���бȻ�׼��С��������
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #���ҵ�,��ѵ�j��Ԫ�ظ�ֵ���ڸ�Ԫ��i,��ʱ����i,j��Ԫ�����
            myList[i] = myList[j]

            #ͬ���ķ�ʽ�Ƚ�ǰ����
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #�����һ�ֱȽ�֮��,�б��ֳ�����������,����i=j,��Ҫ����������û�base
        myList[i] = base

        #�ݹ�ǰ�����
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


myList = [49,38,65,97,76,13,27,49]
print("Quick Sort: ")
QuickSort(myList,0,len(myList)-1)
print(myList)