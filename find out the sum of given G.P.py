a = int(input("enter the first number of G.P series = "))
n = int(input("enter the total number in G.P series = "))
r = int(input("enter the common ratio of G.P series = "))

sum = (a * (1 - pow(r,n+1))) // (1-r)
tn = a * (pow(r,n-1))

t1 = a
t2 = a

for i in range(n):
    tr = r * t1
    print("{}".format(tr))
    t1 = tr
    t2 = t2 * tr

print("sum of given G.P =",sum)