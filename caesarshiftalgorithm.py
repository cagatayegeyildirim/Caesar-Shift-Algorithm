def caesar_encrypt(received_letter, shiftstep):
    ciphertext_out = []
    crypted_text = []

    alphabetupper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                     "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabetlower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    space = [" "]

    for each_letter in received_letter:
        if each_letter in alphabetupper:
            index = alphabetupper.index(each_letter)
            caesarshiftalgorithm = (index + shiftstep) % 26  # Enc(x+n)mod26
            crypted_text.append(caesarshiftalgorithm)
            new_letter = alphabetupper[caesarshiftalgorithm]
            ciphertext_out.append(new_letter)
        elif each_letter in alphabetlower:
            index = alphabetlower.index(each_letter)
            caesarshiftalgorithm = (index + shiftstep) % 26  # Enc(x+n)mod26
            crypted_text.append(caesarshiftalgorithm)
            new_letter = alphabetlower[caesarshiftalgorithm]
            ciphertext_out.append(new_letter)

        elif each_letter in space:
            ciphertext_out.append(*space)
    return ciphertext_out


plaintextinput = input("Enter plain text:")
howmanyshift = int(input("How many shifts do you want?:"))
ciphertext = caesar_encrypt(plaintextinput, howmanyshift)
print("Plaintext:", plaintextinput)
print("Ciphertext:", *ciphertext)
