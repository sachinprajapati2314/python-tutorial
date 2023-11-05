l = [12,54,9,74,457]

for i in range(0,len(l)-1):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(l)