"""
- Input: we have an array of bytes that encode some text symbols/chars
- Each symbol can be encoded with 1 or 2 bytes
- If symbol is encoded with 1 byte then it's high bit equals to 1
- If symbol is encoded with 2 bytes then first byte has high bit equal to 0 while second byte can have any value
    for the high bit (0 or 1) because we know that there is no 3,4,5... bytes symbols
- Challenge: Create a function that has as input specified array and it's length and finds out whether last symbol
    in this array is 1 or 2-bytes long
"""

from sys import argv


def main():
    import codecs
    import sys

    # Start with arguments: " python M-soft.py ab\xc4\x99c1\xc3\xb1\xc3\xb1 7 "
    if len(argv) == 3:
        print("len 3")
        length_array = int(argv[2])
        binary_array = argv[1]
        binary_array = str(binary_array).replace('\\\\', '\\')[2:-1]
        print(binary_array)
        binary_array = bytes(binary_array, encoding='utf-8', errors="replace")

        # binary_array = binary_array.encode('utf-8', errors='surrogateescape')
        # binary_array = binary_array.decode('ascii', errors='surrogateescape')
        # binary_array = bytearray(binary_array)
        print("binary_array", binary_array)
        count_bytes_last_symbol(binary_array, length_array)

    # Start without arguments: " python M-soft.py "
    else:
        testing()


# Function of calculate size last symbol in bytes
def count_bytes_last_symbol(binary_array, length_array):
    len_array = int(length_array)

    # convert massive from utf-8 coding in binary coding
    array_to_calculate = [bin(i)[2:].rjust(8, '0') for i in list(binary_array)]

    # if massive in binary coding
    # array_to_calculate = list(binary_array)

    print("bin array: ", array_to_calculate)
    double_bytes_symbol = False

    for byte_num in range(len(array_to_calculate)):
        print(len_array, double_bytes_symbol)

        if double_bytes_symbol:
            double_bytes_symbol = False
            continue

        if int(array_to_calculate[byte_num][0]) == 1:
            print("Yesss")
            double_bytes_symbol = True

        if len_array == 1:
            print(array_to_calculate[byte_num][0])
            if int(array_to_calculate[byte_num][0]) == 0:
                print("RESULT: Last symbol size one bytes")
            else:
                print("RESULT: Last symbol size two byte")
            break

        print("array_to_calculate[byte_num][0] >> ", array_to_calculate[byte_num][0])

        len_array -= 1


# Testing function of calculate size last symbol in bytes
def testing():
    """
    testing count size last symbol in bytes in binary massive.
    Binary massive was encoding a seven length symbols massive: 'abęc1ññ'
    Ensoding massive: b'ab\xc4\x99c1\xc3\xb1\xc3\xb1'
    python M-soft.py b'ab\xc4\x99c1\xc3\xb1\xc3\xb1' 7
    """

    binary_array = b'ab\xc4\x99c1\xc3\xb1\xc3\xb1'
    length_array = 7

    count_bytes_last_symbol(binary_array, length_array)


if __name__ == "__main__":
    main()
