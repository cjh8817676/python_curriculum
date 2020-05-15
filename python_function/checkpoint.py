def main():
    print(min(min(5,6),min(51,6))) 

def min(n1,n2):
    smallest = n1
    if n2 < smallest :
        smallest = n2
    return smallest #可以試試看去掉這一行
    

main()