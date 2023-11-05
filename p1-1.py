nested_lists = []

for i in range(10):
    inner_list = []
    for j in range(1,51):
        inner_list.append(j)
    nested_lists.append(inner_list)

for lst in nested_lists:
    print(lst)