def binary_search(vector, key):
    low = 0
    high = len(vector) - 1

    while low <= high:
        mid = (low + high) // 2
        midval = vector[mid]
        if midval == key:
            return mid
        if midval > key:
            high = mid - 1
        else:
            low = mid + 1
    if vector[mid] > key:
        return mid
    else:
        return mid + 1


def main():
    n = int(input())
    freq = dict()
    hours_f = list()
    hours_s = list()
    for i in range(n):
        vect = [int(x) for x in input().split(' ')]
        if vect[0] not in hours_f:
            hours_f.append(vect[0])
        if vect[1] not in hours_s:
            hours_s.append(vect[1])
        if vect[0] not in freq:
            freq[vect[0]] = [0, 0]
        freq[vect[0]][0] += vect[2]
        if vect[1] not in freq:
            freq[vect[1]] = [0, 0]
        freq[vect[1]][1] += vect[1] - vect[0]

    hours_f.sort()
    hours_s.sort()

    q = int(input())
    final_str = ''
    for i in range(q):
        vect = [int(x) for x in input().split(' ')]
        summa = 0
        tip = vect[2] - 1
        if tip == 0:
            index = binary_search(hours_f, vect[0])
            hours_len = len(hours_f)
            search_vect = hours_f
        else:
            index = binary_search(hours_s, vect[0])
            hours_len = len(hours_s)
            search_vect = hours_s

        while index <= hours_len - 1 and search_vect[index] <= vect[1]:
            summa += freq[search_vect[index]][tip]
            index += 1
        final_str = final_str + f"{summa} "
    print(final_str)


if __name__ == '__main__':
    main()
