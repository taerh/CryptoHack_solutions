ASCII_CHARS: str = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
HEX_DIGITS: str = "0123456789abcdef"


def hex_digit_value(character: str) -> int:
    if character.lower() in HEX_DIGITS:
        for i in range(len(HEX_DIGITS)):
            if HEX_DIGITS[i] == character.lower():
                return i
    return None


def ascii_from_value(value: int) -> str:
    if value < 32 or value > 126: 
        return None
    return ASCII_CHARS[value-32]


def decode_hex_message(hex_string: str) -> str:
    if (hex_string == None) or (len(hex_string) % 2 != 0) or (hex_string == ""):
        return None
    string: str = ""
    counter: int = 0
    sum: int = 0
    while counter < len(hex_string):
        if hex_digit_value(hex_string[counter]) is None:
            return None
        else:
            if counter % 2 == 0:
                sum += hex_digit_value(hex_string[counter]) * 16
            else:
                sum += hex_digit_value(hex_string[counter])
                if ascii_from_value(sum) is None:
                    return None
                else:
                    string += ascii_from_value(sum)
                    sum = 0
            counter += 1
    return string

print(decode_hex_message("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
