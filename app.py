import argparse


known_starting_plaintext = 'THM{'
known_ending_plaintext = '}'

def derive_key_parts(hex_encoded_input, known_plaintext, starting_index):
    xor_encrypted_bytes = bytes.fromhex(hex_encoded_input)
    derived_key = ""
    for i in range(len(known_plaintext)):
        derived_key += chr(xor_encrypted_bytes[starting_index + i] ^ ord(known_plaintext[i]))
    return derived_key

def xor_reverse(hex_encoded_input, key):
    xor_encrypted_bytes = bytes.fromhex(hex_encoded_input)
    decrypted_message = ""
    for i in range(len(xor_encrypted_bytes)):
        decrypted_message += chr(xor_encrypted_bytes[i] ^ ord(key[i % len(key)]))
    return decrypted_message

def main():
    parser = argparse.ArgumentParser(description='W1seGuy THM XOR Decryption')
    parser.add_argument('hex_encoded_input', type=str, help='Hex encoded string to decrypt')
    parser.add_argument('key_length', type=int, help='Length of the encryption key')

    args = parser.parse_args()
    hex_encoded_input = args.hex_encoded_input
    key_length = args.key_length

    derived_key_start = derive_key_parts(hex_encoded_input, known_starting_plaintext, 0)
    derived_key_end = derive_key_parts(hex_encoded_input, known_ending_plaintext, len(hex_encoded_input) // 2 - 1)
    full_xor_key = (derived_key_start + derived_key_end)[0:key_length]
    decrypted_message = xor_reverse(hex_encoded_input, full_xor_key)
    
    print("Derived start of the key:", derived_key_start)
    print("Derived end of the key:", derived_key_end)
    print("Fully derived key:", full_xor_key)
    print("Decrypted message:", decrypted_message)

if __name__ == '__main__':
    main()
