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

entering = "abęc1ññ"
print(len(entering), entering)
print((entering.encode('utf-8')))

print(len(list(entering.encode('utf-8'))), list(entering.encode('utf-8')))

lis = [hex(i) for i in list(entering.encode('utf-8'))]
print("hex", lis)

lis = [bin(i)[2:].rjust(8, '0') for i in list(entering.encode('utf-8'))]
print("binary", lis)

#print(("\xe0\xb4\xa4".encode('utf-8')))
#print(type("\xe0\xb4\xa4"))
# print(bytes('ñ'.encode()))
# str0 = (12, 500, 345, 1000, 123223121231)
# str1 = bytearray([0b011111, 0x00, 0x00, 0x00, 0x08, 0x00, \xe0\xb4\xa4])
# count = 7
# res = ["<1>","<2>"]
# print(str1.decode('utf-8'))
# for i in str1:
#     print(len(list(str(i).encode('utf-8'))))
    # str2 = bin(i)
    # str2 = hex(i)
    # print(count, res[0] if str(str2)[0] == '0' else res[1], str(str2))
    # if count == 1:
        # print(str(str2))
        # print(res[0] if str(str2)[0] == '0' else res[1], i)
        # print(len(list(str(i).encode('utf-8'))))
    # count -= 1


# Основная функция запуска расчета
def main():
    print("args", argv)
    list_args = [*argv]
    print("list_args", list_args)
    length_array = argv[2]
    binary_array = argv[1]
    count_bytes_last_symbol(binary_array, length_array)
    # testing()


def count_bytes_last_symbol(binary_array, length_array):
    len_array = int(length_array)
    array_to_calculate = [bin(i)[2:].rjust(8, '0') for i in list(binary_array)]

    for byte_num in range(len(array_to_calculate)):
        if len_array == 1:
            print(array_to_calculate[byte_num][0])
            if array_to_calculate[byte_num][0] == 0:
                print("RESULT: Last symbol size one bytes")
            else:
                print("RESULT: Last symbol size two byte")
            pass
        if array_to_calculate[byte_num][0] == 0:
            byte_num += 1

        len_array -= 1


def testing():
    """
    testing count bytes in binary massive.
    Binary massive was encoding a seven length symbols massive: 'abęc1ññ'
    python 001.py b'ab\xc4\x99c1\xc3\xb1\xc3\xb1' 7
    """

    binary_array = b'ab\xc4\x99c1\xc3\xb1\xc3\xb1'
    length_array = 7

    count_bytes_last_symbol(binary_array, length_array)


if __name__ == "__main__":
    main()
