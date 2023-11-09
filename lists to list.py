lists = [[] for _ in range(1,11)]
for i in range(10):
    lists[i] = [i+1]

positive_indices = [0, 3, 9]
negative_indices = [-1, -5, -7]
print(" index + :")
for index in positive_indices:
    print(lists[index], index)
print(" index - :")
for index in negative_indices:
    print(lists[index], index)

lists[0].extend([11, 12, 13])
lists[1].append(14)
lists[2].insert(0, 15)
lists[3].remove(1)
lists[4].pop(0)

print("all list:")
for lst in lists:
    print(lst)

#as chatGPT vase in kar komak gereftam vali to ghemate metod ha chizi balad nabod mesle in ke chon kate 17 ro eror
#mideh vali kod ejra mishe