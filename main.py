def summation(lst1, lst2):
    updated_list = []
    for i in range(len(lst1)):
        updated_list.append(lst1[i] + lst2[i])
    return updated_list

def find_min_max(lst):
    min_lst = min(lst)
    max_lst = max(lst)
    return min_lst, max_lst

n = int(input())
lst1 = []
for add in range(n):
    lst1.append(int(input()))

lst2 = []
for add in range(n):
    lst2.append(int(input()))

current = summation(lst1, lst2)
print(current)

print(find_min_max(current))
