import string


def decrypt(cipher, key):
    result = ""
    for char in cipher:
        if char not in alphabet:
            result += char
        else:
            # ord(char) returns the unicode in ASCII for a character
            # chr(int) returns the character of a given ASCII code
            result += chr(((ord(char) - ord('a')) - key) % 26 + 97)

    return result


alphabet = list(string.ascii_lowercase)
charFrequencies = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, 0.005, 0.005, 0.035,
                   0.030, 0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]

ciphertext = input("Enter the ciphertext: ")
ciphertext = ciphertext.lower()
cipherFrequency = dict()  # dictionary to map characters to their frequencies

for char in ciphertext:
    if char in alphabet:
        cipherFrequency[char] = cipherFrequency.get(char, 0) + 1


length = ciphertext.__len__()

correlation = dict()
for i in range(26):
    sum = 0
    for char in cipherFrequency.keys():
        sum += (cipherFrequency[char] / length) * \
            charFrequencies[((ord(char) - ord('a')) - i) % 26]

    correlation[i] = sum

correlationSorted = dict(
    sorted(correlation.items(), key=lambda item: item[1], reverse=True))

for i in correlationSorted.keys():
    print("for i:", i, " plaintext:", decrypt(ciphertext, i))
    yn = input("is this message valid ?(y/n)")
    print()
    if yn.lower() == "y":
        break
