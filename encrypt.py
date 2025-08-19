from base64 import b64encode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))

    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def full_encrypt():
    te = str(input("Enter text for encryption: "))
    pw = str(input("Enter password for encryption: "))

    et = encrypt(te, pw)

    fn = str(input("Enter the name of the file: "))
    f = open(fn, 'w')
    cipher_text = et['cipher_text']
    salt = et['salt']
    nonce = et['nonce']
    tag = et['tag']
    f.write(cipher_text +'\n')
    f.write(salt +'\n')
    f.write(nonce +'\n')
    f.write(tag +'\n')
    f.close()


if __name__ == "__main__":
    full_encrypt()