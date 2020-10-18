"""
Задача:
Создать функцию, которая имеет в качестве входных данных
указанный массив байтов и его длину, и определяет, имеет ли последний
символ в этом массиве длину 1 или 2 байта.

Особенности:
- Пример входного массива: b'abc1 \xc3\x90\xc2\xb2\xc3\x91\xc2\x8b\xc3\x91\xc2\x88\xc3\x90\xc2\xba\xc3\x91\xc2\x83'  ()
- Каждый символ может быть закодирован 1 или 2 байтами
- Если символ закодирован 1 байтом, то его старший бит равен 1
- Если символ закодирован 2 байтами, то первый байт имеет старший
бит, равный 0, тогда как второй байт может иметь любое значение
для старшего бита (0 или 1), потому что известно, что нет символов
закодированных 3,4,5 ... байтами

"""

from sys import argv


def main():
    if len(argv) == 3:
        print("len 3")
        length_array = int(argv[2])
        binary_array = argv[1].strip("'").replace('\\\\', '\\').encode('utf-8')
        print("binary_array", binary_array)
        count_bytes_last_symbol(binary_array, length_array)
    else:
        testing()


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



def testing():
    """
    testing count bytes in binary massive.
    Binary massive was encoding a seven length symbols massive: 'abęc1ññ'
    Ensoding massive: b'ab\xc4\x99c1\xc3\xb1\xc3\xb1'
    python M-soft.py b'ab\xc4\x99c1\xc3\xb1\xc3\xb1' 7
    """

    binary_array = b'ab\xc4\x99c1\xc3\xb1\xc3\xb1a1'
    length_array = 9

    count_bytes_last_symbol(binary_array, length_array)


if __name__ == "__main__":
    main()
