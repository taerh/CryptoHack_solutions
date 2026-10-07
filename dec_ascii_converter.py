ASCII_CHARS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def dec_ascii_converter(decimal_list: list[int]) -> str:
    flag: str = ""
    for num in decimal_list:
        flag += ASCII_CHARS[num-32]
    return flag

print(dec_ascii_converter([99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]))
