# Python Program

# Implementation of hamming code for error detection

def hammingCodeGeneration():
    def noOfParityBits(m):  # getting no.of data bits (m) as argument
        p = 0  # no.of parity bits p -> 0
        while not (m + p + 1 <= 2 ** p):  # while m + p + 1 <= 2 ^ p is not true
            p += 1  # increment p
        return p  # return no.of parity bits (p)

    # getting entered data bits and total bits (t) as arguments
    def positionParityBits(dataBits, t):
        j = 0  # power factor -> 2 ^ j
        k = 0  # index value [0], [1], [2]
        list1 = []  # creating list (array) to add elements
        for i in range(1, t + 1):  # for i = 1 to t + 1 (total)
            # if i == 2 ^ j (ie) i -> parity positions 2 ^ 0 -> 1,
            #  2 ^1 -> 2,
            #  2 ^ 2 -> 4,
            #  8, 16, 32, 64,....
            if i == 2 ** j:
                list1.append('0')  # then append -> adding 0 to the list
                j += 1  # increment power factor -> j
            else:
                # else append -> adding databits of index k (ie) databits[0]..[1]..[2]..[3]..[4]...
                list1.append(dataBits[k])
                k += 1  # increment index value
        # return list (ie) positioned parity bits (0) with data bits list
        return list1

    # getting positioned parity bits list, no.of parity bits (p), total bits (t) as arguments
    def hammingCode(dataBitsWithParity0, p, t):
        # creating list which is copy of positioned parity bits list
        list1 = dataBitsWithParity0.copy()
        # for i = 0 to no.of parity bits (p) (ie) p = 3 -> 0, 1, 2 | p = 4 -> 0, 1, 2, 3 | p = 5 -> 0, 1, 2, 3, 4 |...
        for i in range(p):
            printBitPos = []  # creating list to print bit positions
            parity = ''  # empty string
            # pos-> 2 ^ i (ie) 2 ^ 0 -> 1,
            #  2 ^ 1 -> 2,
            #  4, 8, 16, 32.... parity bit positions 1, 2, 4, 8, 16,...
            pos = 2 ** i
            # printing corresponding bit positions for parity bit position 1, 2, 4, 8...
            print(f'\nFor parity position {pos} -> Bit positions', end='  ')
            for j in range(1, t + 1):  # for j = 1 to t + 1 (total)
                # if j BITWISE AND (&) pos == pos
                # (ie) pos = 1 -> j = 1, 3, 5, 7, 9, 11...bits positions having 1 in the LSB (Least Significant Bit position)
                # pos = 2 -> j = 2, 3, 6, 7, 10, 11, 14, 15...bits positions having 1 in the second position from LSB
                # pos = 4 -> j = 4, 5, 6, 7, 12, 13, 14, 15...bits positions having 1 in the third position from LSB
                # ...in general BITWISE AND (&) of parity bit position (pos) and bits position (j) gives non-zero (1, 2, 4, 8, 16..)
                if j & pos == pos:
                    # adding bits positions (j) to list to print bit positions
                    printBitPos.append(j)
                    # if no.of 1's in parity is even -> parity = 0,
                    # if no.of 1's in parity is odd -> parity = 1
                    # concatenating parity bit positions value (1 or 0) to parity bit
                    parity += str(list1[j - 1])
            # printing bit positions
            print(printBitPos)
            # if parity bit string count of 1 is even -> parity bit = 0
            if parity.count('1') % 2 == 0:
                parity = '0'
            # else parity bit string count of 1 is odd -> parity bit = 1
            else:
                parity = '1'
            print(
                f'\nParity bit of position {pos} at index {pos - 1} -> {parity}')  # printing parity bit
            # changing parity bit (0) to calculated parity bit of index [pos - 1] in the list
            # list1[pos - 1] = parity
            list1[pos - 1] = parity
        return list1  # returning hamming code list

    # getting data bits as list (array) of integers
    dataBits = list(map(int, input('\nEnter the data bits : ')))

    m = len(dataBits)  # no.of data bits

    print(f'\nNo.of data bits(m) : {m}')

    p = noOfParityBits(m)  # calculating no.of parity bits

    print(f'\nNo.of parity bits(p) : {p}')

    t = m + p  # no.of total bits

    print(f'\nNo. of total bits : {t}')

    # positioning parity bits (0) with data bits
    dataBitsWithParity0 = positionParityBits(dataBits, t)

    print('\nPositioned Parity Bits with Data Bits(data + parity) :\n')

    print(dataBitsWithParity0)

    transmissionData = hammingCode(
        dataBitsWithParity0, p, t)  # generating hamming code

    print('\nGenerated Hamming Code :\n')

    print(transmissionData)  # printing hamming code


def hammingCodeErrorDetection():
    def noOfParityBitsInCode(t):  # getting total bits as argument
        p = 0  # no.of parity bits p -> 0
        while not (t + 1 <= 2 ** p):  # while t + 1 <= 2 ^ p is not true
            p += 1  # increment p
        return p  # return no.of parity bits (p)

    # getting entered error code, no.of parity bits (p) and no.of total bits (t) as arguments
    def hammingCodeDetection(errorData, p, t):
        error = ''  # error -> empty string
        list1 = errorData.copy()  # list -> copy of entered error code
        # for i = 0 to no.of parity bits (p) (ie) p = 3 -> 0, 1, 2 | p = 4 -> 0, 1, 2, 3 | p = 5 -> 0, 1, 2, 3, 4 |...
        for i in range(p):
            # parity = 0  # parity bit -> 0
            parity = ''
            # pos-> 2 ^ i (ie) 2 ^ 0 -> 1,
            #  2 ^ 1 -> 2,
            #  4, 8, 16, 32.... parity positions 1, 2, 4, 8, 16,...
            pos = 2 ** i
            for j in range(1, t + 1):  # for j = 1 to t + 1 (total)
                # if j BITWISE AND (&) pos == pos
                # (ie) pos = 1 -> j = 1, 3, 5, 7, 9, 11...bits positions having 1 in the LSB (Least Significant Bit position)
                # pos = 2 -> j = 2, 3, 6, 7, 10, 11, 14, 15...bits positions having 1 in the second position from LSB
                # pos = 4 -> j = 4, 5, 6, 7, 12, 13, 14, 15...bits positions having 1 in the third position from LSB
                # ...in general BITWISE AND (&) of parity bit position (pos) and bits position (j) gives non-zero (1, 2, 4, 8, 16..)
                if j & pos == pos:
                    # if no.of 1's in parity is even -> parity = 0,
                    # if no.of 1's in parity is odd -> parity = 1
                    # concatenating parity bit positions value (1 or 0) to parity bit
                    parity += str(list1[j - 1])
            # if parity bit string count of 1 is even -> parity bit = 0
            if parity.count('1') % 2 == 0:
                parity = '0'
            # else parity bit string count of 1 is odd -> parity bit = 1
            else:
                parity = '1'
            # concatenation of string of calculated parity bit -> error
            # for eg p1 -> 0, p2 -> 1, p4 -> 0,
            # then error = p1 p2 p4 = 010
            # error = error + parity
            error += parity
        # reversed string of error -> error[::-1]
        # converting binary (010) to decimal (2) -> which is the position of error
        detection = int((error[::-1]), 2)
        return detection  # returning position of detected error

    # getting error code as list of integers
    print('''
Some generated hamming codes are :

[1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]

[0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]

[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]

Change a bit (1 -> 0 or 0 -> 1) in one of the hamming codes

Check whether error is detected or not
        ''')
    errorData = list(map(int, input('Enter the error code : ')))

    t = len(errorData)  # no.of total bits (t)

    p = noOfParityBitsInCode(t)  # no.of parity bits in the code (p)

    # detecting error bit (single bit error)
    errorDetection = hammingCodeDetection(errorData, p, t)

    # if error detection -> 0 then data accepted
    if errorDetection == 0:

        print('\nNo error detected...Data accepted')
    else:
        # printing the detected error position and index
        print(
            f'\nThe error detected at position : {errorDetection} and index : {errorDetection - 1}')


# Driver code
if __name__ == '__main__':
    while True:
        print('''  
----------------------------------------------------------------------------
|        1. Hamming Code Generation (Encoding) -> Sender side              |
|                                                                  		   |
|        2. Hamming Code Error Detection (Decoding) -> Receiver side       |
|                                                        				   |
|        3. Exit                         				                   |
----------------------------------------------------------------------------
            ''')
        # getting user input
        userInput = int(input('Enter the option (1, 2, 3) : '))
        if userInput != 3:
            if userInput == 1:
                hammingCodeGeneration()  # sender side
            elif userInput == 2:
                hammingCodeErrorDetection()  # receiver side
        else:
            break
