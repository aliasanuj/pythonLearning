#bubble sorting
list1 = [23,456,37,6,45,3,87,30,54,88]
for i in range(len(list1)):
    print("i is in first loop", list1[i] )
    for j in range(0,len(list1)-i-1):
        print("j is in second loop", list1[j])
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)


