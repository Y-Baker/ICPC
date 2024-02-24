#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    database = {}

    for _ in range(t):

        query = input()
        if query not in database:
            database[query] = []
            print("OK")
        else:
            i = len(database[query]) + 1
            database[query].append(i)
            query = query + str(i)
            print(query)
