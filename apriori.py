import itertools

T = [f'T{i}00' for i in range (1,10)]
I = [f'I{i}' for i in range (1,6)]

data = {
        'T100' : ['I1','I2','I5'],
        'T200' : ['I2','I4'],
        'T300' : ['I2','I3'],
        'T400' : ['I1','I2','I4'],
        'T500' : ['I1','I3'],
        'T600' : ['I2','I3'],
        'T700' : ['I1','I3'],
        'T800' : ['I1','I2','I3','I5'],
        'T900' : ['I1','I2','I3']
}

minimumSupport = 2 # selection of this item has to occur at least this many times

def support_counter(itemList, transactions, maxIter = 3, iter=1):

    supportCount = {}
    for items in itemList:
        temp = items if type(items) == list else [items]

        key = ",".join(temp)
        if not key in supportCount:
                supportCount[key] = 0
        
        for tran in transactions:
            if all(i in data[tran] for i in temp):
                supportCount[key] += 1

        if supportCount[key] < minimumSupport:
            del supportCount[key]

    print(supportCount)

    if(maxIter == iter or not supportCount): return

    filteredItemList = []
    for i in list(supportCount.keys()):
        for j in i.split(','):
            if not j in filteredItemList:
                filteredItemList.append(j)

    combinedItemList = []
    
    for item in itertools.combinations(filteredItemList, iter+1):
        combinedItemList.append(list(item))
    support_counter(combinedItemList, transactions, maxIter, iter+1)


support_counter(I, T)