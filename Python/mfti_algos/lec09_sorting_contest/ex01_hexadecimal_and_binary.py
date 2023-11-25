# Сдать решение задачи A-Шестнадцатеричные и двоичные
#
# Вычислите XOR от двух чисел.
# Входные данные
# Два целых шестнадцатеричных числа меньших FF.
# Выходные данные
# Побитовый XOR этих чисел в шестнадцетиричном виде
# Примеры
#
# Вход    Выход
#
# 1 23    22
#
# f0 0f   ff
def create_input_data() -> list:
    """
    Prompts the user to enter two numbers separated by whitespace.

    Returns:
        A list containing the two numbers entered by the user.
    """
    inp = input("Enter two numbers separated by whitespace: ")
    numbers = inp.split(" ")
    return numbers


def hex_to_bin(number_hex: str) -> str:
    """
    Converts a hexadecimal number to binary.

    Args:
        number_hex (str): The hexadecimal number to convert.

    Returns:
        str: The binary representation of the hexadecimal number.
    """
    hex_to_bin_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "a": "1010",
        "b": "1011",
        "c": "1100",
        "d": "1101",
        "e": "1110",
        "f": "1111"
    }
    number_bin = "".join([hex_to_bin_map[digit] for digit in number_hex])
    return number_bin


def bin_to_hex(number_bin: str) -> str:
    """
    Converts a binary number to a hexadecimal number.

    Args:
        number_bin (str): The binary number to be converted.

    Returns:
        str: The hexadecimal representation of the binary number.
    """
    bin_to_hex_map = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "a",
        "1011": "b",
        "1100": "c",
        "1101": "d",
        "1110": "e",
        "1111": "f"
    }
    number_hex = ""
    for idx in range(0, len(number_bin), 4):
        number_hex += str(bin_to_hex_map[number_bin[idx : idx + 4]])
    return number_hex


def exclusive_or(first_number: str, second_number: str) -> str:
    """
    Calculates the exclusive OR of two binary numbers.

    Args:
        first_number (str): The first binary number.
        second_number (str): The second binary number.

    Returns:
        str: The result of the exclusive OR operation.

    """
    # Determine the maximum length of the input numbers and add leading
    # zeros.
    max_len = max(len(first_number), len(second_number))
    first_number = first_number.rjust(max_len, "0")
    second_number = second_number.rjust(max_len, "0")
    # Perform the exclusive OR operation on each pair of corresponding
    # digits.
    number_xor = ""
    for el1, el2 in zip(first_number, second_number):
        if el1 == el2 == "1" or el1 == el2 == "0":
            number_xor += "0"
        else:
            number_xor += "1"
    return number_xor


def main():
    """The entry point."""
    numbers = create_input_data()
    first_number, second_number = numbers
    first_number_bin = hex_to_bin(first_number)
    second_number_bin = hex_to_bin(second_number)
    number_xor = exclusive_or(first_number_bin, second_number_bin)
    output = bin_to_hex(number_xor)
    print(output)

    # # The pythonic way.
    # numbers = create_input_data()
    # first_number, second_number = numbers
    # first_number_hex = int(first_number, 16)
    # second_number_hex = int(second_number, 16)
    # number_xor = first_number_hex ^ second_number_hex
    # output = hex(number_xor)[2:]
    # print(output)


if __name__ == "__main__":
    main()
