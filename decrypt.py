#!/usr/bin/python
#
# Stuart AH 3-6-15
# simple program to decrypt a string - using output from our encrypt.py program
# usage: decrypt.py encrypted-password
#

import sys
import base64
from Crypto.Cipher import AES

def main():
    encpassw = sys.argv[1]
    decrypt_val(encpassw)

def decrypt_val(encpassw):
    SALT="vosvjsdabp0909!!"
    dec_secret = AES.new(SALT[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(encpassw))
    clear_val = raw_decrypted.rstrip("\0")
    print "%s decrypted is %s " % (encpassw, clear_val)
    return clear_val


if __name__ == '__main__':
    main()
