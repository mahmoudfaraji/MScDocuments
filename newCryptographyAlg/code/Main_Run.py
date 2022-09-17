import Main_Algorithm
import Avalanche
import Key_Schedule
import time
import NIST_Test


def validation_Hex(value):
    
    valueRet = False
    for i in value:
        valueRet = i in ['a', 'b', 'c', 'd', 'e', 'f', '0',
                         '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return valueRet

def validationEncDec():
    global inp
    enc_dec = False

    while enc_dec == False:
        inp = input('Enter which one? Enc = 0, Dec = 1 : ')
        if len(inp) > 1 or len(inp) < 1 or (int(inp) != 0 and int(inp) != 1):
            enc_dec = False
        else:
            enc_dec = True

    return enc_dec

inp = ''

def Run():
    global key

    tt = validationEncDec()

    # Encryption Run
    if tt and inp == '0':

        plaintext = input('Please Enter Your PlainText ( Length = 24 and characters must be hexadecimal ) : ')

        if validation_Hex(plaintext) and len(plaintext) == 24:

            Main_Algorithm.plainText = plaintext
            cyphertext = Main_Algorithm.FinalEncryption()

            key = '\x1b[0;30;47m' + key + '\x1b[0m'
            print('Plain Text is  : ',
                  ('\x1b[0;30;42m' + plaintext + '\x1b[0m'))
            print('Cypher Text is : ',
                  ('\x1b[0;30;43m' + cyphertext + '\x1b[0m'))

    # Decryption Run
    elif tt and inp == '1':

        cyphertext = input('Please Enter Your PlainText ( Length = 24 and characters must be hexadecimal ) : ')

        if validation_Hex(cyphertext) and len(cyphertext) == 24:

            Main_Algorithm.plainText = cyphertext
            plaintext = Main_Algorithm.FinalDecryption()

            key = '\x1b[0;30;47m' + key + '\x1b[0m'
            print('Cypher Text is : ',
                  ('\x1b[0;30;42m' + cyphertext + '\x1b[0m'))
            print('Plain  Text is : ',
                  ('\x1b[0;30;43m' + plaintext + '\x1b[0m'))


# Run Final Algorithm
key = Key_Schedule.KEY
Run()

# Run Tests : Avalanche, Completeness, NIST
print('----------- Avalanche Test Is Started After 3 Seconds For 10.000 Blocks -----------')
time.sleep(3)

Avalanche.avalanche_test()

print(f'Min Value is : {Avalanche.getMin(Avalanche.matrix)}')
print(f'Max Value is : {Avalanche.getMax(Avalanche.matrix)}')

print('----------- NIST Test Is Started After 3 Seconds For 1.000.000 Blocks -----------')
time.sleep(3)

input_NISTTest = NIST_Test.inputOrGenerateRandomSequencOfbLastBit(
    NIST_Test.RANDOM_SEQUENCE_MAX_SIZE)
NIST_Test.nistTestsExec(input_NISTTest)
