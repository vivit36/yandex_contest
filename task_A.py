def main():
    n = int(input())
    output_str = ''
    for i in range(n):
        input_vect = input().split(',')
        surname, name, patronymic = input_vect[0], input_vect[1], input_vect[2]
        day, month = input_vect[3], input_vect[4]
        term1 = len(set(surname + name + patronymic))
        term2 = 0
        for digit in (day + month):
            term2 += int(digit)
        term3 = ord(surname[0]) - ord('A') + 1
        code = term1 + term2 * 64 + term3 * 256
        final_str = "000" + hex(code)[2:]
        output_str += f"{final_str[-3:].upper()} "
    print(output_str)


if __name__ == '__main__':
    main()
