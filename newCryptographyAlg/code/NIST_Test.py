from nistTests.FrequencyTest import FrequencyTest
from nistTests.RunTest import RunTest
from nistTests.Matrix import Matrix
from nistTests.Spectral import SpectralTest
from nistTests.TemplateMatching import TemplateMatching
from nistTests.Universal import Universal
from nistTests.Complexity import ComplexityTest
from nistTests.Serial import Serial
from nistTests.ApproximateEntropy import ApproximateEntropy
from nistTests.CumulativeSum import CumulativeSums
from nistTests.RandomExcursions import RandomExcursions
import os
from pyfiglet import Figlet
import Main_Algorithm
import string
import random
import numpy
from pyfiglet import Figlet
from tqdm import tqdm
import time

RANDOM_SEQUENCE_MAX_SIZE = 1000000


f = Figlet(font='basic')


def generatePlainTextRandom():

    char = 'abcdef' + string.digits
    return ''.join(random.choice(char) for _ in range(0, 24))


def generat_inputTest():

    print('NIST test is starting...')

    plaintest = generatePlainTextRandom()
    tempPlain = plaintest

    dataStringList = []

    for i in tqdm(range(RANDOM_SEQUENCE_MAX_SIZE), desc="Loading…", ascii=False, ncols=100):

        Main_Algorithm.plainText = tempPlain
        Main_Algorithm.FinalEncryption()
        tempPlain = Main_Algorithm.cypherText
        tempGetBit = "{0:096b}".format(int(tempPlain, 16))
        dataStringList.append(tempGetBit[95])

    print("Complete.")

    return ''.join(dataStringList)


def inputOrGenerateRandomSequencOfbLastBit(i):
    data_path = os.path.join(os.getcwd(), 'data', 'data.e')
    binary_data = ''
    if os.path.exists(data_path):
        handle = open(data_path)
        data_list = []
        for line in handle:
            data_list.append(line.strip().rstrip())
        binary_data = ''.join(data_list)
    else:
        binary_data = generat_inputTest()
        f = open("data/NISTData.text", "w")
        f.write(binary_data)
        f.close()
    return binary_data.zfill(i)


def nistTestsExec(randomSequence):

    print(f.renderText('NIST test:'))
    successText = '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'
    failText = '\x1b[6;30;41m' + 'Fail!' + '\x1b[0m'
    print('The statistical test of the Binary Expansion of e')
    print('2.01. Frequency Test:\t\t\t\t\t\t\t\t',  successText if FrequencyTest.monobit_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.02. Block Frequency Test:\t\t\t\t\t\t\t',  successText if FrequencyTest.block_frequency(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.03. Run Test:\t\t\t\t\t\t\t\t\t\t',  successText if RunTest.run_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.04. Run Test (Longest Run of Ones): \t\t\t\t',  successText if RunTest.longest_one_block_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.05. Binary Matrix Rank Test:\t\t\t\t\t\t', successText if Matrix.binary_matrix_rank_text(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.06. Discrete Fourier Transform (Spectral) Test:\t', successText if SpectralTest.sepctral_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.07. Non-overlapping Template Matching Test:\t\t', successText if TemplateMatching.non_overlapping_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE], '000000001')[1] == True else failText)
    print('2.08. Overlappong Template Matching Test: \t\t\t', successText if TemplateMatching.overlapping_patterns(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.09. Universal Statistical Test:\t\t\t\t\t', successText if Universal.statistical_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.10. Linear Complexity Test:\t\t\t\t\t\t', successText if ComplexityTest.linear_complexity_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.11. Serial Test:\t\t\t\t\t\t\t\t\t', successText if Serial.serial_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.12. Approximate Entropy Test:\t\t\t\t\t\t', successText if ApproximateEntropy.approximate_entropy_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])[1] == True else failText)
    print('2.13. Cumulative Sums (Forward):\t\t\t\t\t', successText if CumulativeSums.cumulative_sums_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE], 0)[1] == True else failText)
    print('2.13. Cumulative Sums (Backward):\t\t\t\t\t', successText if CumulativeSums.cumulative_sums_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE], 1)[1] == True else failText)
    result = RandomExcursions.random_excursions_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])
    print('2.14. Random Excursion Test:')
    print('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion')

    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              successText if (item[4] >= 0.01) == True else failText)

    result = RandomExcursions.variant_test(
        randomSequence[:RANDOM_SEQUENCE_MAX_SIZE])

    print('2.15. Random Excursion Variant Test:\t\t\t\t\t\t')
    print('\t\t STATE \t\t COUNTS \t\t\t P-Value \t\t Conclusion')
    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              successText if (item[4] >= 0.01) == True else failText)
        pass
