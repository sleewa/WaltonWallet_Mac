import getpass
import json
import sys
import time
import requests
from eth_account import Account
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from web3.auto import w3
import datetime

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


def Import_From_Private(secret, password1):
    print("this is imported private key", secret)
    acct = Account.privateKeyToAccount(secret)
    public_key = acct.address
    encrypted = Account.encrypt(secret, password1)
    return (1, public_key, json.dumps(encrypted))


def Import_Keystore(passphrase, filecontent):
    try:
        # content = json.loads(filecontent)
        private_key = w3.toHex(Account.decrypt(filecontent, passphrase))
        public_key = Account.privateKeyToAccount(private_key).address
        encrypted = Account.encrypt(private_key, passphrase)
        return (1, [public_key, private_key], json.dumps(encrypted))
    except Exception as err:
        print(err)
        return (0, 10000)


def Import_mnemonic(passphrase1, passphrase2, mnemonicwords):
    if passphrase1 == passphrase2:
        print(passphrase1)
        print(mnemonicwords)
        
    else:
        return (0, 0)


def Transaction_out(private_key, toaddr, value, gas, gasprice):
    print(private_key)
    acct = Account.privateKeyToAccount(private_key)
    print(acct)
    public_key = acct.address
    nonce = requests.get(
        "https://waltonchain.net:18950/api/getSendTransactionNonce/"+public_key).json()["send_nonce"]
    print(nonce)
    transaction = {
        'to': toaddr,
        'value': int(float(value) * (10 ** 18)),
        'gas': int(gas),
        'gasPrice': int(float(gasprice) * (10 ** 18)),
        'nonce': nonce,
        'chainId': 15
    }
    key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
    signed = w3.eth.account.signTransaction(transaction, private_key)
    return (1, w3.toHex(signed.rawTransaction))


def startCPUMining():
    pass


def stopCPUMining():
    pass


def getAccountBalance(public_key):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getBalance/"+public_key).json()
        return (1, r1['Balance'])
    except Exception as err:
        print(err)
        return (0, err)


def getMiningRecord(public_key):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getMinedBlocksPagination/"+public_key+"/1/12").json()
        return (1, r1['tx_pagination_details'])
    except Exception as err:
        print(err)
        return (0, err)


def getTransactionRecord(public_key):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getAccountTransactionsAllPagination/"+public_key+"/1/12").json()
        return (1, r1['tx_pagination_details'])
    except Exception as err:
        print(err)
        return (0, err)

def getTransactionInfo(hash):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getTransactionInfo/"+hash).json()
        return (1, r1['tx_details'])
    except Exception as err:
        print(err)
        return (0, err)
#api/getAccountTransactionsAllPagination/" + address + "/1/100"


def getTokenMarket():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getMarket/WTC/30").json()
        return (1, r1['token_market'])
    except Exception as err:
        print(err)
        return (0, err)


def getTransactionRecord_day(public_key, interval):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getHistoryBalance/"+public_key+'/'+interval).json()
        return (1, r1['HistoryBalance'])
    except Exception as err:
        print(err)
        return (0, err)


def getCurrentNodesDistribution():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getCurrentNodesDistribution").json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)


def getLatestBlock():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getLatestBlock").json()
        return (1, r1['latest_block'])
    except Exception as err:
        print(err)
        return (0, err)


def getGasPrice():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getGasPrice").json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)


def getHashRate():
    try:
        r1 = requests.post('http://httpbin.org/post', data={
            "jsonrpc": "2.0", "method": "eth_hashrate", "params": [], "id": 2}).json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)
# test for Generate_Two_Key()
# print(Generate_Two_Key("12345", "12345"))
# print(Generate_Two_Key("1234567", "123456"))

# test case
# test_account = (Generate_Three_Key("123456", "123456"))
# print(test_account)
# test_keystore = test_account[1][2]
#
# # test for Import_Keystore
# out = (Import_Keystore("123456", test_keystore))
# print(out)
# test_public_key = out[1][0]
# test_private_key = out[1][1]
# print(Transaction_out(test_private_key, test_public_key, 1, 1, 1))
# print(Import_From_Private('e8671e48e23b728717a43b888612f324ad96177396dcc9a1f3616c6c3c3e6429'))


#ret2 = getTransactionInfo('0x36775097df4ed6429dbe31fc56119a66f8c3dfcfda46792f4982117a90521f0a')
#print(ret2[1])
#print(ret2[1][2]['totol_reward'])
#print(ret2[1][0]['blockNumber'])

#ret3 = getMiningRecord('0x4a49f969507770f31a3e98ff05e75060cfe8e3fd')
#print(ret3[1])
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# datetime.datetime.time()
# timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)) #将utc时间转化为本地时间
# timedeta = datetime.datetime.utcnow()-datetime.datetime.now()
# timetext = timenow.strftime('%Y-%m-%d %H:%M:%S')
# print(datetime.datetime.utcnow())
# print(timetext)
# print(timedeta)


# timenow = datetime.datetime.utcnow()
#
def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
#
# print(utc2local(timenow))
#
# ret = getMiningRecord('0xfbf36b7c56258dc3e29769c1a686250b8b002de3')
# print(ret)