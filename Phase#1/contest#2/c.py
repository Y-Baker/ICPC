def remove_duplicates(n, a):
    last_occurrence = {}
    result = []

    for i in range(n-1, -1, -1):
        if a[i] not in last_occurrence:
            last_occurrence[a[i]] = i

    for i in range(n):
        if i == last_occurrence[a[i]]:
            result.append(a[i])

    return result


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    result = remove_duplicates(n, a)
    print(len(result))
    print(*result)
