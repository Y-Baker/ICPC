t = int(input())
while t>0 :
    a, b = map(int, input().split())
    if (a+b)%2==0 :
        print("Bob")
    else :
        print("Alice")
    t -=1
