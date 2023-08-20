def main():
    n = int(input())
    rockets = dict()
    for i in range(n):
        buf_vect = input().split(' ')
        for i in range(len(buf_vect)):
            if buf_vect[i].isdecimal():
                buf_vect[i] = int(buf_vect[i])

        minutes = buf_vect[0] * 24 * 60 + buf_vect[1] * 60 + buf_vect[2]
        if buf_vect[3] not in rockets:
            rockets[buf_vect[3]] = list()

        if buf_vect[4] != 'B':
            rockets[buf_vect[3]].append((minutes, buf_vect[4]))

    for value in rockets.values():
        value.sort()
    rockets = dict(sorted(rockets.items()))

    output_str = ''
    for vect in rockets.values():
        sum_rocket = 0
        for pair in vect:
            if pair[1] == 'A':
                tmp = pair[0]
            if pair[1] == 'S' or pair[1] == 'C':
                sum_rocket += pair[0] - tmp
        output_str += f"{sum_rocket} "
    print(output_str)


if __name__ == '__main__':
    main()
