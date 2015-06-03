
#!/usr/bin/python
#
# Stuart AH 3-6-15
# simple program to encrypt a string
# usage: encrypt.py unencrypted-password
#

import sys
import base64
from Crypto.Cipher import AES

def main():
    passw = sys.argv[1]
    encrypt_val(passw)

def encrypt_val(passw):
    SALT="vosvjsdabp0909!!"
    enc_secret = AES.new(SALT[:32])
    paddout = (str(passw) + (AES.block_size - len(str(passw)) % AES.block_size) * "\0")
    secret_squirrel = base64.b64encode(enc_secret.encrypt(paddout))
    print "%s encrypted is %s " % (passw, secret_squirrel)
    return secret_squirrel


if __name__ == '__main__':
    main()
