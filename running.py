def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

def best_profit(mylist):
    a = len(mylist)
    j = 1
    temp_list = []
    for i in range(0, a, 2):

        temp_list.append(mylist[j] - mylist[i])

        j = j+2
    c = listsum(temp_list)
    return c


print("Give your inputs")
a = [int(x) for x in input().split(',')]
print("The maximum Profit =", best_profit(a))
