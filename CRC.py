# def xor(x, y):
#     result = bin(int(x, 2) ^ int(y, 2))[2:].zfill(len(x))
#     return result[1:]

# def xor(x, y):
#     result = ''.join('0' if i == j else '1' for i, j in zip(x[1:], y[1:]))
#     return result

def xor(x, y):
    result = ''
    for i, j in zip(x, y):
        if i == j:
            result += '0'
        else:
            result += '1'
    return result[1:]


def modulo_2_division(dividend, divisor, l_divisor):
    pick = l_divisor
    temp = dividend[0: pick]
    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * l_divisor, temp) + dividend[pick]
        pick += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * l_divisor, temp)
    check_word = temp
    return check_word


def encode_data(d, g_p):
    l_g_p = len(g_p)
    append_zeros_with_data = d + ('0' * (l_g_p - 1))
    rem = modulo_2_division(append_zeros_with_data, g_p, l_g_p)
    code_word = d + rem
    return rem, code_word


if __name__ == '__main__':
    data = input('Enter the data : ')

    g_poly = input('Enter the generator polynomial (divisor) in the form of binary digits :')

    remainder, dataSent = encode_data(data, g_poly)

    print(f'Remainder (Check Word) : {remainder}')

    print(f'Data Sent (Code Word) : {dataSent}')
