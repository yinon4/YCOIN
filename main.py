import blockchain
YCoin = blockchain.Blockchain()

def trans(from_address, to_address, amount):
    return YCoin.addTransaction(blockchain.Transaction(blockchain.hash(from_address), blockchain.hash(to_address), amount))

def printChainHistory():
    print("\nChain History:\n" + str(YCoin))

def printChainValidity(chain):
    print("Chain Valid!") if chain.isChainValid() else print("Chain Unvalid!")

def mineBlock(address = None):
    YCoin.minePendingTransactions(blockchain.hash(address))

def printAddressBalance(address):
    print(f"Balance {address} = ${YCoin.balanceOfAddress(blockchain.hash(address))}")

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
    printChainValidity(YCoin)
    printChainHistory()


#   private is hash of name (FOR TESTING PURPOSES NOT CORE)
#   from is private,    hashed once
#   to is public,       hashed twice
#   in main.py send hashed once
#   in bc.py hash as necessary
