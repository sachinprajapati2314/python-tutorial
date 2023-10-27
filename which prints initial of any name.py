def name(st):
    l = st.split()
    n = " "

    for i in range(len(l)):
        st = l[i]

        n += (st[0].upper()+" ")
    
    return n

st = input("enter string = ")
print("initial of string = ",name(st))