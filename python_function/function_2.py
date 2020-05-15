def function(x):
    print('Function\'s argument x = ',x)
    x = 4.5
    y = 3.4
    print('Local variable x = ',x)
    print('Local variable y = ',y)

x = 2
y = 4

function(x)
print('Main function variable x = ',x)
print('Main function variable y = ',y)