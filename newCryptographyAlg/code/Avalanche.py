import Main_Algorithm
import math
import random
import string
from tqdm import tqdm
import time

matrix = [[0 for i in range(96)] for j in range(96)]


def generatePlainTextRandom():
    char = 'abcdef' + string.digits
    return ''.join(random.choice(char) for _ in range(0, 24))


def toggleKthBit(n, k):
    n = int(n, 16)
    res = (n ^ (1 << (k)))
    res = format(int(res), '024x').split('x')[-1]
    return res


def xor_Cs(c, c_):
    res = int(c, 16) ^ int(c_, 16)
    res2 = "{0:096b}".format(int(res))
    return res2


def avalanche_test():

    print('Avalanch test is starting...')

    for i in tqdm(range(10000), desc="Loading…", ascii=False, ncols=100):

        m = generatePlainTextRandom()
        Main_Algorithm.FinalEncryption()
        c = Main_Algorithm.cypherText

        for j in range(96):

            m_ = toggleKthBit(m, j)
            Main_Algorithm.plainText = m_
            Main_Algorithm.FinalEncryption()
            c_ = Main_Algorithm.cypherText

            temp_matrix = [int(t) for t in (xor_Cs(c, c_))]

            for k in range(96):
                global matrix
                matrix[j][k] += temp_matrix[k]


def getMax(matrix):
    max = 0
    for i in range(96):
        for j in range(96):

            if matrix[i][j] > max:
                max = matrix[i][j]

    return max


def getMin(matrix):
    min = getMax(matrix)
    for i in range(96):
        for j in range(96):

            if matrix[i][j] < min:
                min = matrix[i][j]

    return min
