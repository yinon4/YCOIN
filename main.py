import blockchain
from hashlib import sha256

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

    YCoin.minePendingTransactions('A2')
    YCoin.minePendingTransactions(None)

    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')


    print("Chain Valid") if YCoin.isChainValid() else print("Chain Unvalid")
    print("\nChain History:\n" + str(YCoin))
