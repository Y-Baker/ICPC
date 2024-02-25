#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        flag = True
        arr = list(map(int, input().split(" ")))
        mapp = {}
        
        for i in range(n):
            if i % 2 == 0:
                if 0 not in mapp:
                    mapp[0] = arr[i] % 2
                else:
                    if mapp[0] != arr[i] % 2:
                        print("NO")
                        flag = False
                        break
            else:
                if 1 not in mapp:
                    mapp[1] = arr[i] % 2
                else:
                    if mapp[1] != arr[i] % 2:
                        print("NO")
                        flag = False
                        break
        
        if flag:
            print("YES")
