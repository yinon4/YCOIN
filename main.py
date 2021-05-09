import blockchain
from hashlib import sha256
YCoin = blockchain.Blockchain()

def hash(string):
    if string == None:
        return None
    return sha256(string.encode("ascii")).hexdigest()

def trans(from_address, to_address, amount):
    return YCoin.addTransaction(blockchain.Transaction(from_address, to_address, amount))

def printChainHistory(chain = YCoin):
    print("\nChain History:\n" + str(chain))

def printChainValidity(chain = YCoin):
    print("Chain Valid!") if chain.isChainValid() else print("Chain Unvalid!")

def mineBlock(address = None):
    YCoin.minePendingTransactions(address)

def printAddressBalance(address):
    print(f"Balance of address {address}: {YCoin.balanceOfAddress(hash(address))}")

def set_balance(address, amount):
    trans(None, address, amount)
    YCoin.minePendingTransactions(None)

if __name__ == '__main__':
    set_balance('A1', 100)
    trans('A1', 'A2', 50)
    trans('A2', 'A3', 50)
    mineBlock('A2')
    mineBlock()

    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')
    printChainValidity()
