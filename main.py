import blockchain
from hashlib import sha256

def printChainHistory(chain):
    print("\nChain History:\n" + str(chain))

def printChainValidity(chain):
    print("Chain Valid!") if chain.isChainValid() else print(f"Chain Unvalid!")

def mineBlock(address = None):
    YCoin.minePendingTransactions(address)

def printAddressBalance(address):
    print(f"Balance of address {address}: {YCoin.getBalanceOfAddress(address)}")

def set_balance(address, amount):
    YCoin.addTransaction(blockchain.Transaction(None, address, amount))
    YCoin.minePendingTransactions(None)

if __name__ == '__main__':
    YCoin = blockchain.Blockchain()
    set_balance('A1', 100)
    YCoin.addTransaction(blockchain.Transaction('A1', 'A2', 50))
    YCoin.addTransaction(blockchain.Transaction('A2', 'A3', 50))

    mineBlock('A2')
    mineBlock()
    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')

    printChainValidity(YCoin)
    printChainHistory(YCoin)
