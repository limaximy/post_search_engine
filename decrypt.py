from base64 import b64decode
import hashlib
from Cryptodome.Cipher import AES

def decrypt(enc_dict:list, password:str)->bytes:
    cipher_text = b64decode(enc_dict[0])
    salt = b64decode(enc_dict[1])
    nonce = b64decode(enc_dict[2])
    tag = b64decode(enc_dict[3])

    # Генерируем приватный ключ из пароля и соли
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    decrypted:bytes = cipher.decrypt_and_verify(cipher_text, tag)
    return decrypted


def open_file(file_name:str)->list:
    f = open(file_name, 'r')
    a = []
    s = ''
    while s := f.readline():
        s = s[:-1]
        a.append(s)
    f.close()
    return a


def decrypt_file(token_file_name:str, password:str, is_print:bool)->bytes:
    d:bytes = decrypt(open_file(token_file_name), password)
    if is_print:
        print(str(d)[2:-1])
    return d



if __name__ == "__main__":
    decrypt_file("vk_token.myaw", input(), True)