#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n,k = map(int, input().split())
        freqA = [0]*100010
        freqB = [0]*100010

        arrA = list(map(int, input().split()))
        arrB = list(map(int, input().split()))

        def getFreq(arr, freq):
            for i in arr:
                freq[i] += 1

        getFreq(arrA, freqA)
        getFreq(arrB, freqB)

        def countPairs(freq):
            cnt = 0
            for i in arrA:
                freq[i] -= 1
                if k-i > 0:
                    cnt += freq[k-i]
            return cnt

        cnt1 = countPairs(freqA)
        cnt2 = countPairs(freqB)
        if cnt1 == cnt2:
            print("Draw")
        elif cnt1 > cnt2:
            print("Mahmoud")
        else:
            print("Bashar")
