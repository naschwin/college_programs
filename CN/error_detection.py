def Onescomp(bits):
    new = ''
    for bit in bits:
        new += str(int(not(int(bit))))
    return new


def twoscomp(bits):
    num = int(bits[1:], 2) + 1
    new = Onescomp(bin(num)[2:])
    return new


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


# Performs Modulo-2 division
def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0'*pick, tmp) + divident[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword


def crc(data, key):
    print("**** CRC ****")
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Transmitted frame is: (Data + Remainder)",
          codeword)


# Driver code
# data = "100100"
# key = "1101"
# crc(data, key)


def checksum(bits):
    print("**** Checksum ****")
    l = len(bits)
    streams = []
    for i in range(int(l/8)):
        str_ = int(bits[i*8:i*8+8], 2)
        streams.append(str_)
    summ = sum(streams)
    cksum = bin(summ)[2:]
    while len(cksum) > 8:
        cksum = twoscomp(cksum)
    print(f"Checksum: {cksum}")


def lrc(bits, parity='E'):
    print('**** LRC ****')
    l = len(bits)
    streams = []
    lrC = None
    for i in range(int(l/8)):
        str_ = int(bits[i*8:i*8+8], 2)
        streams.append(str_)
        if lrC == None:
            lrC = str_
        else:
            lrC = lrC ^ str_
    lrC = bin(lrC)[2:]

    if parity == 'E':
        print(f"Lrc: {int(lrC):08}")
    elif parity == 'O':
        print(f"Lrc: {Onescomp(lrC):1>8}")


def vrc(bits, parity='E'):
    print('**** VRC ****')
    l = len(bits)
    streams = ''
    for i in range(int(l/8)):
        str_ = bits[i*8:i*8+8]
        c = str_.count('1')
        streams += str(int(c % 2 != 0))

    print(f"Vrc: {streams}")


bits = '110011101111000100100010'

# vrc(bits)
# lrc(bits)
# checksum(bits)
# crc('10101010', '1101')


def main():
    while True:
        try:
            ans = int(
                input("Press 1 for LRC\nPress 2 for VRC\nPress 3 for CRC\nPress 4 for checksum\nPress 0 to exit\nEnter your choice: "))
        except ValueError:
            print("Select a correct option")
            continue
        if ans == 1 or ans == 2:
            b = input("Enter no of bits(multiple of 8): ")
            data = input("Enter Data Bits")
            parity = input("Do you want ODD(O)/EVEN(E) Parity: ")
            if ans == 1:
                lrc(data, parity)
            if ans == 2:
                vrc(data, parity)
        elif ans == 3:
            frame_size = input("Enter Frame size: ")
            frame = input("Enter Frame: ")
            generator_size = input("Enter generator size: ")
            generator = input("Enter generator: ")
            crc(frame, generator)
        elif ans == 4:
            temp = input("Enter segment size: ")
            b = input("Enter no of bits(multiple of 8): ")
            data = input("Enter Data Bits")
            checksum(data)
        elif ans == 0:
            break
        else:
            print("*************")
            print("Select a correct option")
        print("*************")


main()
