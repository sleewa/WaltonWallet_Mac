import getpass
import json
import sys

from eth_account import Account
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from web3.auto import w3


"""
failure reason for Generate_Two_Key function
10000: password length less than 6
10001: two passwords do not match
"""


def Generate_Three_Key(password1, password2):
    if password1 == password2:
        pass1 = password1
        pass2 = password2
        if len(pass1) < 6:
            print('less than 6')
            return (0, 10000)
        else:
            acct = Account.create(password1)
            public_key = acct.address
            private_key = acct.privateKey
            encrypted = Account.encrypt(private_key, password1)
            return (1, [public_key, w3.toHex(private_key), json.dumps(encrypted)])
    else:
        print('wrong')
        return (0, 10001)


"""
failure reason for Generate_Key function
"""


def Import_From_Private(secret):
    acct = Account.privateKeyToAccount(secret)
    public_key = acct.address
    return (1, public_key)


def Import_Keystore(passphrase, filecontent):
    try:
        # content = json.loads(filecontent)
        private_key = w3.toHex(Account.decrypt(filecontent, passphrase))
        public_key = Account.privateKeyToAccount(private_key).address
        return (1, [public_key, private_key])
    except Exception as err:
        print(err)
        return (0, 10000)


def Import_mnemonic(passphrase1, passphrase2, mnemonicwords):
    if passphrase1 == passphrase2:
        print(passphrase1)
        print(mnemonicwords)
    else:
        print('wrong')


def Transaction_out(fromaddr, toaddr, value, gas, gasprice):
    print(' ')


# test for Generate_Two_Key()
# print(Generate_Two_Key("12345", "12345"))
# print(Generate_Two_Key("1234567", "123456"))
test_account = (Generate_Three_Key("123456", "123456"))
print(test_account)
test_keystore = test_account[1][2]

# test for Import_Keystore
print(Import_Keystore("123456", test_keystore))
