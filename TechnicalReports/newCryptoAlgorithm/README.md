### New Cryptography Algorithm

Designing a cryptographic algorithm can be one of the solutions in order to evaluate the level of knowledge of an active expert in the field of applied cryptography. In this project, we have designed a new algorithm by using different parts of several encryption algorithms. In this project, the input of the algorithm is a 96-bit fragment. The structure used to do this project is Feistel type 1 structure. After entering the parts into the algorithm, a part of it is affected by the function f and then it is XORed with the other part. Finally, the first round ends with the moving of the parts. This is done for twelve consecutive rounds. The f function used in this project is designed similar to the Blowfish function. Also, another part of this project is related to the key part, where 96 bits of the main key are entered into the system. By applying the function on this key, a total of 36 subkeys are produced, which are used in 12 rounds. The function applied to the key is similar to the structure of the AES key function with a slight modification. Finally, this algorithm is implemented in OFB mode (both encryption and decryption) and avalanche, integrity and NIST tests are performed on it. In addition, the number of lines of this algorithm is 344 lines in Python along with the codes related to Avalanche test and completeness and OFB mode. This number of lines is defined without considering the codes related to NIST tests and tables.
Also this algorithm was passed NIST, Avalanche, Completeness and other Frequency test.

<p style='padding-left: 30px;'> Overview:</p>
<img style='border: 3px solid #111;width: 600px;' alt="Cryptography Algorithm" src="/TechnicalReports/newCryptoAlgorithm/images/Cryptography Alg. pic1.png">

<p style='padding-left: 30px;'> Function f:</p>
<img style='border: 3px solid #111;width: 600px;' alt="Cryptography Algorithm" src="/TechnicalReports/newCryptoAlgorithm/images/Cryptography Alg. pic2.png">

<p style='padding-left: 30px;'> Key Generation:</p>
<img style='border: 3px solid #111;width: 600px;' alt="Cryptography Algorithm" src="/TechnicalReports/newCryptoAlgorithm/images/Cryptography Alg. pic3.png">
