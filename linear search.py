def linearsearch(lst,l,p_n):
    for i in range(0,l):
        if lst[i] == p_n:
            return i
    return -1

lst = [41, 85, 9, 7, 20]
p_n = 9
l = len(lst)

result = linearsearch(lst,l,p_n)
if result == -1:
    print("Element not found")
else:
    print("element position number =",result)