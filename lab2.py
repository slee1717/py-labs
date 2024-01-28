table = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encrypt(line, key):
    encrypted_word = ""
    for x in line.upper():
        if x == " ":
            encrypted_word += " "
        else:
            if table.index(x)+key > 25:
                encrypted_word += table[table.index(x)+(key-26)]
            else:
                encrypted_word += table[table.index(x)+key]
    return encrypted_word

def decrypt(line,key):
    decrypted_word = ""
    for x in line.upper():
        if x == " ":
            decrypted_word += " "
        else:
            decrypted_word += table[table.index(x) - key]
    return decrypted_word

print(encrypt("I AM ENCRYPTED",5))
print(decrypt("N FR JSHWDUYJI",5))

