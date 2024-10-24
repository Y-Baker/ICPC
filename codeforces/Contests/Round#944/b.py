#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        x = input()
        flag = False
        if len(set(x)) == 1:
            print("NO")
        else:
            print("YES")
            for i in range(len(x)):
                for j in range(i + 1, len(x)):
                    if x[i] != x[j]:
                        flag = True
                        print(x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:])
                        break
                if flag:
                    break

