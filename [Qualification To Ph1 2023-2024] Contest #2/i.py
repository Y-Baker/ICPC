#!/usr/bin/python3

def is_beautiful_pair(n, m, tower1, tower2):
    if tower1[0] == tower2[m - 1] or tower1[n - 1] == tower2[0]:
        return "NO"
    return "YES"


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        tower1 = input().strip()
        tower2 = input().strip()
        
        result = is_beautiful_pair(n, m, tower1, tower2)
        print(result)