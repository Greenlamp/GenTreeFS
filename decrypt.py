import os
import sys
import json
import base64

from Crypto.Cipher import AES  # pip install pycrypto

salt = "tu89geji340t89u2"
passphrase = bytes.fromhex('a7ca9f3366d892c2f0bef417341ca971b69ae9f7bacccffcf43c62d1d7d021f9')

cipher = AES.new(passphrase, AES.MODE_CBC, salt)

'''
Encrypt a json file
'''
def encrypt_save_file(in_json_file, out_save_file):
    if os.path.isfile(in_json_file):
        file_contents = open(in_json_file, "r").read()
        
        encrypted = base64.b64encode(cipher.encrypt(utils.pkcs7_pad_str(file_contents)))
        
        open(out_save_file, "wb").write(encrypted)
    else:
        raise Exception("Input file \"{}\" doesn't exist!".format(in_json_file))


'''
Decrypt a save file
'''
def decrypt_save_file(in_save_file, out_json_file, pretty_json = True):
    if os.path.isfile(in_save_file):
        file_contents = open(in_save_file, "rb").read()
        
        decrypted = cipher.decrypt(base64.b64decode(file_contents))
        decrypted = decrypted.decode('ascii')
        
        # Fix numerous different paddings
        if decrypted[-1] != "}":
            decrypted = decrypted.rstrip(decrypted[-1])
        
        if pretty_json:
            decrypted = json.dumps(json.loads(decrypted), indent=4)
        
        open(out_json_file, "w").write(decrypted)
    else:
        raise Exception("Input file \"{}\" doesn't exist!".format(in_save_file))

class utils(object):
    @staticmethod
    def pkcs7_pad_str(s):
        padding_count = (16 - len(s) % 16)
        return s + (padding_count * chr(padding_count))

if __name__ == "__main__":
    try:
        # Remove first arg
        args = [sys.argv[x] for x in range(1, len(sys.argv))]
        
        if len(args) != 3:
            print("Incorrect arguments count ({} given out of 3)".format(len(args)))
            raise Exception("USAGE: (encrypt/decrypt) (input file) (output file)")
        
        mode = args[0].lower()
        input_file = args[1]
        output_file = args[2]
        
        if mode == "decrypt":
            print("Decrypting \"{}\" to \"{}\"...".format(input_file, output_file))
            decrypt_save_file(input_file, output_file)
        elif mode == "encrypt":
            print("Encrypting \"{}\" to \"{}\"...".format(input_file, output_file))
            encrypt_save_file(input_file, output_file)
        else:
            print("Invalid mode specified.")
            raise Exception("Mode should be either encrypt or decrypt.")
        
        print("Done!")
    except Exception as err:
        print(err)
