alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(alphabet,range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)),alphabet))

def encrypt_vigenre(message,key):
    encrypted_vigenre = ''

    split_message = [message[i:i + len(key)] for i in range(0,len(message),len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet) 
            encrypted_vigenre += index_to_letter[number]
            i+=1
    
    return encrypted_vigenre

def decrypt_vigenre(cipher,key):
    decrypted_vigenre = ''

    split_cipher = [cipher[i:i +len(key)] for i in range(0,len(cipher), len(key))]

    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted_vigenre += index_to_letter[number]
            i+=1

    return decrypted_vigenre

#================================================================================================

def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

#================================================================================================


def create_playfair_matrix(key): 
    key = key.upper().replace('J', 'I')
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed_text = ""
    
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i+1 < len(text) and text[i] == text[i+1]:
            processed_text += 'X'
        elif i+1 < len(text):
            processed_text += text[i+1]
            i += 1
        i += 1
    
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    
    return processed_text

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = preprocess_text(plaintext)
    encrypt_playfair = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            encrypt_playfair += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            encrypt_playfair += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            encrypt_playfair += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return encrypt_playfair

#================================================================================================

def encrypt_rot13(pt):
    encptl = list(pt)
    for i in range(len(pt)):
        n = ord(pt[i])
        if n >= 78:
            n += 13
            n = n - 90 + 64
            ch = chr(n)
            encptl[i] = ch
        else:
            n += 13
            ch = chr(n)
            encptl[i] = ch
    return "".join(encptl)

def decrypt_rot13(encpt):
    decptl = list(encpt)
    for i in range(len(encpt)):
        n = ord(encpt[i])
        if n <= 77:
            n -= 13
            n = 91 - (65 - n)
            ch = chr(n)
            decptl[i] = ch
        else:
            n -= 13
            ch = chr(n)
            decptl[i] = ch
    return "".join(decptl)

#================================================================================================

def gcd(a, b):
    """Menghitung Greatest Common Divisor (GCD) dari a dan b"""
    a = int(float(a))
    b = int(float(b))
    while b != 0:
        a, b = b, a % b
    return a

def encrypt_affine(text, a, b):
    """Melakukan enkripsi Affine Cipher pada teks"""
    a  = int(float(a))
    b = int(float(b))
    if gcd(a, 26) != 1:
        raise ValueError("a dan 26 harus coprime untuk affine cipher bekerja dengan benar.")
    
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                encrypted_char = (a * x + b) % 26
                result += chr(encrypted_char + ord('A'))
            else:
                x = ord(char) - ord('a')
                encrypted_char = (a * x + b) % 26
                result += chr(encrypted_char + ord('a'))
        else:
            result += char
    return result
