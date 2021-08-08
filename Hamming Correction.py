# Python Program

# Implementation of hamming code for error detection

def hammingCodeGeneration():
    def noOfParityBits(m):
        p = 0
        while not (m + p + 1 <= 2 ** p):
            p += 1
        return p

    def positionParityBits(dataBits, t):
        j = 0
        k = 0
        list1 = []
        for i in range(1, t + 1):
            if i == 2 ** j:
                list1.append('0')
                j += 1
            else:
                list1.append(dataBits[k])
                k += 1
        return list1

    def hammingCode(dataBitsWithParity0, r, t):
        list1 = dataBitsWithParity0.copy()
        for i in range(r):
            parity = 0
            powOf2 = 2 ** i
            print('\nFor parity', end=' ')
            for j in range(1, t + 1):
                if j & powOf2 == powOf2:
                    print(j, end=' ')
                    parity = parity ^ int(list1[j - 1])
            print(f'\nParity bit of position {powOf2} at index {powOf2 - 1} -> {parity}')
            list1[powOf2 - 1] = str(parity)
        return list1

    dataBits = list(map(int, input('\nEnter the data bits : ')))

    m = len(dataBits)

    print(f'\nNo.of data bits(m) : {m}')

    p = noOfParityBits(m)

    print(f'\nNo.of parity bits(p) : {p}')

    t = m + p

    print(f'\nNo. of total bits : {t}')

    dataBitsWithParity0 = positionParityBits(dataBits, t)

    print('\nPositioned Parity Bits with Data Bits(data + parity) :\n')

    print(dataBitsWithParity0)

    transmissionData = hammingCode(dataBitsWithParity0, p, t)

    print('\nGenerated Hamming Code :\n')

    print(transmissionData)


def hammingCodeErrorDetection():
    def noOfParityBitsInCode(t):
        p = 0
        while not (t + 1 <= 2 ** p):
            p += 1
        return p

    def hammingCodeDetection(errorData, r, t):
        error = ''
        list1 = errorData.copy()
        for i in range(r):
            parity = 0
            powOf2 = 2 ** i
            for j in range(1, t + 1):
                if j & powOf2 == powOf2: parity = parity ^ int(list1[j - 1])
            error = error + str(parity)
        detection = int(str(error[::-1]), 2)
        return detection

    errorData = list(map(int, input('\nEnter the error code : ')))

    t = len(errorData)

    parity = noOfParityBitsInCode(t)

    errorDetection = hammingCodeDetection(errorData, parity, t)

    print(f'\nThe error detected at position : {errorDetection} and index : {errorDetection - 1}')


# Driver code
if __name__ == '__main__':
    while True:
        print(
            '''   
=======================================================================
|        1. Hamming Code Generation (Encoding) -> Sender side         |
|                                                                     |
|        2. Hamming Code Error Detection (Decoding) -> Receiver side  |
|                                                                     |
|        3. Exit                                                      |
=======================================================================
             '''
        )
        userInput = int(input('Enter the option (1, 2, 3) : '))  # getting user input
        if userInput != 3:
            if userInput == 1:
                hammingCodeGeneration()  # sender side
            elif userInput == 2:
                hammingCodeErrorDetection()  # receiver side
        else:
            break
