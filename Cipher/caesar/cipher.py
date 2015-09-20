'''
Created on 21 Sep 2015

@author: Sheece
'''

def encode(fileName,shift):
    with open(fileName,'r') as inputFile:
        for line in inputFile:
            with open('encriptedData.txt','w') as outputFile:
                for ch in line:
                    character=chr(ord(ch)+shift)
                    outputFile.write(character)

if __name__ == '__main__':
    fileName='data.txt'
    shift=1
    encode(fileName,shift)