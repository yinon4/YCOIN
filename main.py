import blockchain
from hashlib import sha256

def set_balance(address, amount):
    YCoin.addTransaction(blockchain.Transaction(None, address, amount))
    YCoin.minePendingTransactions(None)

if __name__ == '__main__':
    YCoin = blockchain.Blockchain()
    set_balance("1", 100)
    YCoin.addTransaction(blockchain.Transaction("1", "2", 50))
    YCoin.addTransaction(blockchain.Transaction("2", "3", 50))

    YCoin.minePendingTransactions("2")
    YCoin.minePendingTransactions(None)

    print("Balance of address: " + str(YCoin.getBalanceOfAddress("1")))
    print("Balance of address: " + str(YCoin.getBalanceOfAddress("2")))
    print("Balance of address: " + str(YCoin.getBalanceOfAddress("3")))


    print("Chain Valid") if YCoin.isChainValid() else print("Chain Unvalid")
    print("\nChain History:\n" + str(YCoin))
