
def myfun(n):
    return abs(n-50)

nx_list = [ 30 , 70 , 100 , 20 , 90]

nx_list.sort(key = myfun)
print(nx_list)




