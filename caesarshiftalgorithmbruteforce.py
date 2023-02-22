alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetlower = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = input("Please enter the Cipher text: ")

for key in range(len(alphabet)):

    bruteforce = ""

    for char in ciphertext:
        if char in alphabet:
            num = alphabet.find(char)
            num = num - key

            if num < 0:
                num = num + len(alphabet)

            bruteforce = bruteforce + alphabet[num]
        elif char in alphabetlower:
            num = alphabetlower.find(char)
            num = num - key

            if num < 0:
                num = num + len(alphabetlower)

            bruteforce = bruteforce + alphabetlower[num]
        else:
            bruteforce = bruteforce + char

    print("Decryption Attempt %s:" % (key), bruteforce)
