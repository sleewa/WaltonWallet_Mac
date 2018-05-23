from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import getpass

from web3.auto import w3

from eth_account import Account
from PyQt5.QtWidgets import *



def Generate_Key(password1, password2):
    if password1 == password2:
        pass1 = password1
        pass2 = password2
        if len(pass1) < 6:
            print('less than 6')
            return 1
        else:
            acct = Account.create(password1)
            return acct
    else:
        print('wrong')
        return 1


def Import_secret(passphrase1, passphrase2, secret):
    if passphrase1 == passphrase2:
        print(passphrase1, secret)
    else:
        print('wrong')


def Import_Ketstore(passphrase, filename):
    if filename.len == 0:
        print('no file')
    else:
        print('keystore', passphrase)


def Import_mnemonic(passphrase1, passphrase2, mnemonicwords):
    if passphrase1 == passphrase2:
        print(passphrase1)
        print(mnemonicwords)
    else:
        print('wrong')


