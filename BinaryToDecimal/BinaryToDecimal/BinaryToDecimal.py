#############################################################################
##################################Algorithm##################################
'''
1. Reading and Image file in binary format
2. Convering into Byte Array
3. Again Byte Array converting into ascii format
4. Ascii values converting into hex format
5. That hex value converting into binary format
6. Take 1000 bits at a time and save every 1000 bits in an array 
7. Now read each index of that array and convert it into decimal and save it
8. Now convert each decimal in to form of exponent
'''
#############################################################################
import math
import io
import binascii

##################Reading Image to Byte Array######################
def ConvertImageToByteArray(SourceFileName):
    with open(SourceFileName, "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)
    return b
###############################################################



##################Converting Byte Array to Binary######################
def ConvertByteArrayToBinary(ImgByteArray):
    binAsciiInHex = binascii.hexlify(ImgByteArray)
    binary = bin(int(binAsciiInHex, 16))
    return binary
###############################################################




############################Writing File############################
def WriteContentToFile(FilePath,Content):
    f = open(FilePath,"w")
    f.write(Content)
    f.close()
#####################################################################


############################Appending File############################
def AppendContentToFile(FilePath,Content):
    f = open(FilePath,"a+")
    f.write(Content)
    f.close()
#####################################################################


############################Nearest Sqrt############################
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
####################################################################


