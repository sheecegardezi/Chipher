'''
Created on 21 Sep 2015

@author: Sheece Gardezi
'''

def decodePartial(encriptedFileName, shift):
    data = ""
    with open(encriptedFileName, 'r') as inputFile:
        for line in inputFile:
            for ch in line:
                character = chr(ord(ch) + shift)
                data = data + character
                if(len(data)>20):
                    break;
    return data

def decode(encriptedFileName,shift):
    with open(encriptedFileName,'r') as inputFile:
        for line in inputFile:
            with open('decriptedData.txt','w') as outputFile:
                for ch in line:
                    character=chr(ord(ch)+shift)
                    outputFile.write(character)

if __name__ == '__main__':
    encriptedFileName = 'encriptedData.txt'
    for shift in range(26):
        print('is this the correct decription?')
        print (decodePartial(encriptedFileName, shift))
        response= input('Enter Y/N:')
        if(response=='Y'):
            decode(encriptedFileName,shift)
            break;
    
