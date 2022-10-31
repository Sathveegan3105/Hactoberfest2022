size = int(input("size: "))
while size !=0 :
    if 0 < size <= 26:
        for i in range(1,size+1):
            for j in range(1,size+1-i):
                print(' ',end='')
            c = 97+size
            for k in [-1]*i + [1]*(i-1) :
                c += k
                print(chr(c),end='')
            print()
        for a in range(1,size):
            for b in range(1,a+1):
                print(' ',end='')
            c = 97+size
            for d in [-1]*(size-a) + [1]*(size-a-1):
                c += d
                print(chr(c),end='')
            print()


    else:print("wrong input!")
    size = int(input("size: "))
