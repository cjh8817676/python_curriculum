
def swap(x,y):
    temp = x
    x = y
    y = temp
    return

x = 2
y = 4
print(x,' ',y)
swap(x,y)
print(x,' ',y)
swap(id(x),id(y))
print(x,' ',y)


