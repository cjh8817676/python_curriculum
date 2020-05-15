#數字與字串是不可變更物件

x = 4
y = x
print(id(x))
print(id(y)) #對電腦來說y跟x參考同個物件，而對人來說x、y同值

y = y + 1
print(id(y)) #id不再一樣，因為值不一樣