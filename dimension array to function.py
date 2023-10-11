# one demension array
def array(arr):
    for i in arr:
        print(i)

my_list = "Sachin "

array(my_list)


# two demension array
def array(arr):
    for row in arr:
        for i in row:
            print(i, end="  ")
        print()

my_list = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    "prajapati"
]

array(my_list)