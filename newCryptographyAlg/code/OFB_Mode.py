import pdb
import random
import string
import Main_Algorithm
import binascii
import Key_Schedule


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


def Run():
    global key

    tt = validationEncDec()

    # Encryption Run
    if tt and inp == '0':

        plaintext = input(
            'Please Enter Your PlainText ( Length = unlimited and characters must be string(text) ) : ')

        cyphertext = FinalEncryption(plaintext)

        key = '\x1b[0;30;47m' + key + '\x1b[0m'
        print('Plain Text is     : ',
              ('\x1b[0;30;42m' + plaintext + '\x1b[0m'))
        print('Cypher Text is    : ',
              ('\x1b[0;30;43m' + cyphertext + '\x1b[0m'))
        print('Key is            : ', ('\x1b[0;30;43m' + key + '\x1b[0m'))
        print('Initial Vector is : ', ('\x1b[0;30;45m' + ini_iv + '\x1b[0m'))

    # Decryption Run
    elif tt and inp == '1':

        cyphertext = input(
            'Please Enter Your PlainText ( Length = unlimited and characters must be hexadecimal ) : ')

        plaintext = FinalDecryption(cyphertext)

        key = '\x1b[0;30;47m' + key + '\x1b[0m'
        print('Cypher Text is    : ',
              ('\x1b[0;30;42m' + cyphertext + '\x1b[0m'))
        print('Plain  Text is    : ',
              ('\x1b[0;30;43m' + plaintext + '\x1b[0m'))
        print('Key is            : ', ('\x1b[0;30;43m' + key + '\x1b[0m'))
        print('Initial Vector is : ', ('\x1b[0;30;45m' + ini_iv + '\x1b[0m'))


inp = ''


def generate_blocks(text):

    hexText = ''.join(hex(ord(c))[2:] for c in text)

    if len(hexText) % 24 != 0:
        hexText = hexText + ('0' * (24 - (len(hexText) % 24)))

    split_text = [hexText[i:i+24] for i in range(0, len(hexText), 24)]

    blocks = []
    for i in range(len(split_text)):
        blocks.append(split_text[i])

    return blocks


def iv_generator():

    char = 'abcdef' + string.digits
    iv = ''.join(random.choice(char) for _ in range(0, 24))
    return iv


# initial vector can be selected Random with iv_generator()
ini_iv = '454298fb3ee731a94f77eed3'


def encrypt_iv(iv):

    Main_Algorithm.plainText = iv
    res = Main_Algorithm.FinalEncryption()
    return res


def xor_iv_plaintext(enc_iv, plainText):

    enciv = format((int(enc_iv, 16) ^ int(plainText, 16)),
                   '024x').split('x')[-1]
    return enciv


def FinalEncryption(text):

    blocks = generate_blocks(text)

    cyphertext = []
    iv = ini_iv

    for i in range(len(blocks)):
        iv = encrypt_iv(iv)
        cyphertext.append(xor_iv_plaintext(iv, blocks[i]))

    return ''.join(cyphertext)


def FinalDecryption(text):

    cyphertext = [text[i:i+24] for i in range(0, len(text), 24)]
    plaintext = []
    iv = ini_iv

    for i in range(len(cyphertext)):
        iv = encrypt_iv(iv)
        plaintext.append(xor_iv_plaintext(iv, cyphertext[i]))

    plaintext = ''.join(plaintext)
    ppp = ''.join([chr(int(''.join(c), 16))
                   for c in zip(plaintext[0::2], plaintext[1::2])])

    return ppp


key = Key_Schedule.KEY
# Run OFB Mode
Run()
