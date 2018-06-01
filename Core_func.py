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

from xml.dom import minidom


# 生成XML文件方式
def generateaddressXml():
    doc = minidom.Document()

    # 创建根元素
    rootElement = doc.createElement('ArrayOfAddressEntity')
    rootElement.setAttribute('xmlns:xsd','"http://www.w3.org/2001/XMLSchema"')

    doc.appendChild(rootElement)
    # 为根元素添加10个子元素

    # 打开test.xml文件 准备写入
    f = open('test.xml', 'w')
    # 写入文件
    doc.writexml(f, addindent='  ', newl='\n')
    # 关闭
    f.close()

    return (doc,rootElement)

def addaddressxml(doc,rootElement,accountname,address):
    AddressEntity = doc.createElement('AddressEntity')
    rootElement.appendChild(AddressEntity)
    # 为子元素添加id属性
    # childElement.setAttribute('id', str(pythonId))
    UAddress = doc.createElement('UAddress')
    AddressEntity.appendChild(UAddress)

    GuidNo = doc.createElement('GuidNo')
    AddressEntity.appendChild(GuidNo)

    AccountName = doc.createElement('AccountName')
    AddressEntity.appendChild(AccountName)
    name = doc.createTextNode(accountname)
    AccountName.appendChild(name)

    Address = doc.createElement('Address')
    AddressEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)

    doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open('test.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def editaddressxml(doc,rootElement,accountname,row):
    addrentity = rootElement.getElementsByTagName('AddressEntity')[row]
    nametag = addrentity.getElementsByTagName('AccountName')[0].childNodes[0]
    nametag.nodeValue=accountname

    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)

    f = open('test.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def generatewalletXml():
    doc = minidom.Document()

    rootElement = doc.createElement('ArrayOfWalletBaseEntity')
    rootElement.setAttribute('xmlns:xsd', '"http://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)
    f = open('wa.xml', 'w')
    doc.writexml(f, addindent='  ', newl='\n')
    f.close()

    return (doc, rootElement)

def addwalletxml(doc,rootElement,accountname,address,filename,GMN='false'):
    WalletBaseEntity = doc.createElement('WalletBaseEntity')
    rootElement.appendChild(WalletBaseEntity)
    # 为子元素添加id属性
    Address = doc.createElement('Address')
    WalletBaseEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)
    # childElement.setAttribute('id', str(pythonId))
    UUID = doc.createElement('UUID')
    WalletBaseEntity.appendChild(UUID)

    AccountName = doc.createElement('AccountName')
    WalletBaseEntity.appendChild(AccountName)
    name = doc.createTextNode(accountname)
    AccountName.appendChild(name)

    FileName = doc.createElement('FileName')
    WalletBaseEntity.appendChild(FileName)
    fname = doc.createTextNode(filename)
    FileName.appendChild(fname)

    GMNtag = doc.createElement('GMN')
    WalletBaseEntity.appendChild(GMNtag)
    gmn = doc.createTextNode(GMN)
    GMNtag.appendChild(gmn)

    doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open('wa.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def editwalletxml(doc,rootElement,accountname,row):
    walletentity = rootElement.getElementsByTagName('WalletBaseEntity')[row]
    nametag = walletentity.getElementsByTagName('AccountName')[0].childNodes[0]
    nametag.nodeValue=accountname

    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)

    f = open('wa.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

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
        return (1, 0)
    else:
        return (0, 0)


def Transaction_out(private_key, toaddr, value, gas, gasprice):
    print(private_key)
    acct = Account.privateKeyToAccount(private_key)
    print(acct)
    public_key = acct.address
    print(public_key)
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
    print(transaction)
    #key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
    signed = w3.eth.account.signTransaction(transaction, private_key)
    print(w3.toHex(signed.rawTransaction))
    tx_hash = requests.get(
        "https://waltonchain.net:18950/api/sendRawTransaction/" + w3.toHex(signed.rawTransaction)).json()
    print(tx_hash)

    return (1, tx_hash['tx_hash'])


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

def generatetransXml():
    doc = minidom.Document()

    rootElement = doc.createElement('ArrayOfAddressTransactionsEntity')
    rootElement.setAttribute('xmlns:xsd', '"http://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)
    f = open('trans.xml', 'w')
    doc.writexml(f, addindent='  ', newl='\n')
    f.close()

    return (doc, rootElement)

def addtransaddrxml(doc,rootElement,address,updatetime):
    AddressTransactionsEntity = doc.createElement('AddressTransactionsEntity')
    rootElement.appendChild(AddressTransactionsEntity)

    Address = doc.createElement('Address')
    AddressTransactionsEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)

    UpdateTime = doc.createElement('UpdateTime')
    AddressTransactionsEntity.appendChild(UpdateTime)
    updatet = doc.createTextNode(updatetime)
    UpdateTime.appendChild(updatet)

    TransactionList = doc.createElement('TransactionList')
    AddressTransactionsEntity.appendChild(TransactionList)

    # doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open('trans.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def addtranslistxml\
    (doc,rootElement,address,updatetime,fromaddr,blocknum,
     toaddr,gasprice,blockhash,transacindex,txhash,Gas,Value,utctimestamp,transtype,blocktype):

    foundaddr = 0
    for AddressTransactionsEntity in rootElement.getElementsByTagName('AddressTransactionsEntity'):
        if address == AddressTransactionsEntity.getElementsByTagName('Address')[0].firstChild.data:
            # walletentity = AddressTransactionsEntity.getElementsByTagName('UpdateTime')
            updatet = AddressTransactionsEntity.getElementsByTagName('UpdateTime')[0].firstChild
            updatet.nodeValue=updatetime

            AccountTransactionsEntity = doc.createElement('AccountTransactionsEntity')
            newtrans = AddressTransactionsEntity.getElementsByTagName('TransactionList')[0]
            newtrans.appendChild(AccountTransactionsEntity)

            addressFrom = doc.createElement('addressFrom')
            AccountTransactionsEntity.appendChild(addressFrom)
            faddr = doc.createTextNode(fromaddr)
            addressFrom.appendChild(faddr)

            blockNumber = doc.createElement('blockNumber')
            AccountTransactionsEntity.appendChild(blockNumber)
            blockNo = doc.createTextNode(blocknum)
            blockNumber.appendChild(blockNo)

            gasPrice = doc.createElement('gasPrice')
            AccountTransactionsEntity.appendChild(gasPrice)
            gp = doc.createTextNode(gasprice)
            gasPrice.appendChild(gp)

            blockHash = doc.createElement('blockHash')
            AccountTransactionsEntity.appendChild(blockHash)

            transacIndex = doc.createElement('transacIndex')
            AccountTransactionsEntity.appendChild(transacIndex)
            tranid = doc.createTextNode(transacindex)
            transacIndex.appendChild(tranid)

            tx_hash = doc.createElement('tx_hash')
            AccountTransactionsEntity.appendChild(tx_hash)
            hash = doc.createTextNode(txhash)
            tx_hash.appendChild(hash)

            gas = doc.createElement('gas')
            AccountTransactionsEntity.appendChild(gas)
            GAS = doc.createTextNode(Gas)
            gas.appendChild(GAS)

            addressTo = doc.createElement('addressTo')
            AccountTransactionsEntity.appendChild(addressTo)
            taddr = doc.createTextNode(toaddr)
            addressTo.appendChild(taddr)

            value = doc.createElement('value')
            AccountTransactionsEntity.appendChild(value)
            val = doc.createTextNode(Value)
            value.appendChild(val)

            utc_timestamp = doc.createElement('utc_timestamp')
            AccountTransactionsEntity.appendChild(utc_timestamp)
            utct = doc.createTextNode(utctimestamp)
            utc_timestamp.appendChild(utct)

            transType = doc.createElement('transType')
            AccountTransactionsEntity.appendChild(transType)
            ttype = doc.createTextNode(transtype)
            transType.appendChild(ttype)

            blockType = doc.createElement('blockType')
            AccountTransactionsEntity.appendChild(blockType)
            btype = doc.createTextNode(blocktype)
            blockType.appendChild(btype)

            foundaddr = 1
            break
    if foundaddr == 0:
        addtransaddrxml(doc, rootElement, address, updatetime)
        addtranslistxml \
            (doc, rootElement, address, updatetime, fromaddr, blocknum,
             toaddr, gasprice, blockhash, transacindex, txhash, Gas, Value, utctimestamp, transtype, blocktype)


    # doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open('trans.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def edittransxml(doc,rootElement,address,blocktype,row):
    for AddressTransactionsEntity in rootElement.getElementsByTagName('AddressTransactionsEntity'):
        if address == AddressTransactionsEntity[0].childNodes[0]:
            TransactionList = AddressTransactionsEntity[0].childNodes[2]
            trans = TransactionList.getElementsByTagName('AccountTransactionsEntity')[row]
            typetag = trans.getElementsByTagName('blockType')[0].childNodes[0]
            typetag.nodeValue=blocktype

            xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            doc = minidom.parseString(xmlStr)

            f = open('trans.xml', 'w')
            doc.writexml(f, addindent=' ', newl='\n')
            f.close()

            break

def generatesettingXml():
    doc = minidom.Document()

    rootElement = doc.createElement('MiningEntity')
    rootElement.setAttribute('xmlns:xsd', '"http://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)

    password = doc.createElement('MinerP')
    rootElement.appendChild(password)
    addr = doc.createTextNode(' ')
    password.appendChild(addr)

    minediff = doc.createElement('Difficulty')
    rootElement.appendChild(minediff)
    diff = doc.createTextNode('478705014976')
    minediff.appendChild(diff)

    minereward = doc.createElement('Mining_reward')
    rootElement.appendChild(minereward)
    reward = doc.createTextNode('3')
    minereward.appendChild(reward)

    f = open('setting.xml', 'w')
    doc.writexml(f, addindent='  ', newl='\n')
    f.close()

    return (doc, rootElement)


# print(getTransactionInfo('0x4a0f05cd4d901a50af76f6d8cbf56c2fd8a7fc09dcec49706e240ae068b919f5'))

# print(getTransactionRecord('0xAB828046856F5886a3835C914862E0F5f834Ee7d'))
#Transaction_out('3373c7af355f86b8dc9f02d386bea047da063ed541ed927d149214134012e451', '0xFBf36B7c56258dC3e29769C1a686250B8B002dE3', 2, 200000, 0.000000036)