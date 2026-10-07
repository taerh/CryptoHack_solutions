HEX_DIGITS = "0123456789abcdef"
BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_digit_value(character: str) -> int | None:
    if character.lower() in HEX_DIGITS:
        for i in range(len(HEX_DIGITS)):
            if HEX_DIGITS[i] == character.lower():
                return i
    return None


def hex_to_bytes(hex_string: str) -> list[int] | None:
    if len(hex_string) % 2 != 0:
        return None
    counter: int = 0
    sum: int = 0
    byte_array: list[int] = []
    while counter < len(hex_string):
        if hex_digit_value(hex_string[counter]) is None:
            return None
        else:
            if counter % 2 == 0:
                sum += hex_digit_value(hex_string[counter]) * 16
            else:
                sum += hex_digit_value(hex_string[counter])
                byte_array.append(sum)
                sum = 0
            counter += 1
    return byte_array


def decimal_to_binary(value: int, width: int) -> str:
    bitstring: str = ""
    counter: int = width - 1
    while counter >= 0:
        if (2**counter) <= value:
            bitstring += "1"
            value -= 2**counter
            counter -= 1
        else: 
            bitstring += "0"
            counter -= 1
    return bitstring

def binary_to_decimal(binary: str) -> int:
    sum: int = 0
    counter: int = len(binary) - 1
    reverse: int = 0
    while counter >= 0:
        if binary[reverse] == "1":
            sum += 2**counter
            counter -= 1
            reverse += 1
        else:
            counter -= 1
            reverse += 1
    return sum

def padding(data_string: str, group_value: int, character: str) -> str:
    padded_string: str = data_string
    if len(padded_string) % group_value != 0:
        padded_string += (group_value - (len(padded_string) % group_value)) * character
        return padded_string
    else:
        return data_string


def bytes_to_base64(byte_values: list[int]) -> str:
    binary_bytes: str = ""
    six_bit_list: list[str] = []
    six_bit_string: str = ""
    base64_string: str = ""
    for byte in byte_values:
        binary_bytes += decimal_to_binary(byte, 8)
    binary_bytes = padding(binary_bytes, 6, "0")
    #if len(binary_bytes) % 6 != 0:
    #    binary_bytes += (6 - (len(binary_bytes) % 6)) * "0"
    for char in binary_bytes:
        six_bit_string += char
        if len(six_bit_string) == 6:
            six_bit_list.append(six_bit_string)
            six_bit_string = ""
    for group in six_bit_list:
        index: int = binary_to_decimal(group)
        base64_string += BASE64_ALPHABET[index]
    base64_string = padding(base64_string, 4, "=")
    #if len(base64_string) % 4 != 0:
    #    base64_string += (4 - (len(base64_string) % 4)) * "="
    return base64_string
        
    
def hex_to_base64(hex_string: str) -> str:
    result = hex_to_bytes(hex_string)
    return bytes_to_base64(result)

print(hex_to_base64("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))
