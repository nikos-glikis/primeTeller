from __future__ import print_function

import re
import sys

MAC_REGEX = "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"


def verify_mac(value):
    return re.match(MAC_REGEX, value.lower())


def is_number_even(number):
    return number % 2 == 0


def convert_string_to_hex_integer(string):
    return int(string, 16)


def convert_int_to_hex_string(number):
    return hex(number).lower().replace("0x", "")


def generate_password_list(mac, outfile=None):
    # get latest digits
    latest_digits_string = mac[12:17].replace(":", "")

    # convert them to int
    latest_digits_string = convert_string_to_hex_integer(latest_digits_string)

    # find out password latestDigits
    # don't have data for the edges. Guessing %0xffff
    if is_number_even(latest_digits_string):
        password_end_int = (latest_digits_string - 8) % 0xffff
    else:
        password_end_int = (latest_digits_string - 1) % 0xffff

    password_end_string = convert_int_to_hex_string(password_end_int)

    for i in range(1000, 10000):
        final_value = repr(i) + password_end_string
        if outputFile:
            with open(outputFile, "a+") as f:
                f.write(final_value + "\n")
        else:
            print(final_value)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " mac [outputFilename]")
        print("If no outputFilename is specifier results will be printed on stdout")
        exit()

    outputFile = False
    if len(sys.argv) > 2:
        outputFile = sys.argv[2]

    mac = sys.argv[1]

    # verify mac
    if not verify_mac(sys.argv[1]):
        print("Mac must be in the format ab:ab:ab:ab:ab:ab")
        exit()

    generate_password_list(mac, outputFile)
