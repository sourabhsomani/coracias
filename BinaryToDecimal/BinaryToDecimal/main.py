import BinaryToDecimal
import datetime
import binascii

TakingBits=50000

SourceFileName = input("Enter the source file name: ")

#Reading Image File and Getting Result in ByteArray Format
imgByteArray = BinaryToDecimal.ConvertImageToByteArray(SourceFileName)

#Converting Byte Array To Binary Format
binary = BinaryToDecimal.ConvertByteArrayToBinary(imgByteArray)
binary=binary.replace("0b","");

#Saving Binary File
filename = "binary" + datetime.datetime.now().strftime("%d_%B_%Y_%H_%M_%S_%p") + ".txt"
BinaryToDecimal.WriteContentToFile("E:\\MCNSolutions\\temp\\Python\\"+filename,binary);

#Take 50 bits at a time and save every 50 bits in an array
lengthOfBinaryArr = len(binary) // TakingBits

counter = 0
lstBinaryChunk = []
for x in range(0,lengthOfBinaryArr):
    lstBinaryChunk.append((binary[counter:counter + TakingBits]))
    counter+=TakingBits
#Remaining bits are appending
lstBinaryChunk.append((binary[TakingBits * lengthOfBinaryArr:TakingBits * lengthOfBinaryArr + len(binary) % TakingBits]))


#Converting each binary chunk of bits from the array and converting into
#decimal format
filename="decimal" + datetime.datetime.now().strftime("%d_%B_%Y_%H_%M_%S_%p") + ".txt"
decimalFormatedData=[]
for x in range(0,len(lstBinaryChunk)):
    content=int(str(lstBinaryChunk[x]),2);
    BinaryToDecimal.AppendContentToFile("E:\\MCNSolutions\\temp\\Python\\"+filename,(str(content)+","));
    decimalFormatedData.append(content);

#for x in decimalFormatedData:
for _dData in decimalFormatedData:
    while(_dData>1000):
        base=BinaryToDecimal.isqrt(_dData)
        print("%d ^ %d + "%(base,2))
        _dData-=base**2
    print(_dData)
    print("-----------------------------------");
'''
inhexa = hex(int("0b" + binary,2)).replace("0x","")

print("\n\n\n")


_imgByteArray = binascii.unhexlify(inhexa)
if _imgByteArray == imgByteArray:
    print("""Both are same""");

    '''