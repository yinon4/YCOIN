import blockchain as bc
YCoin = bc.Blockchain()

def hash(string):
    return bc.hash(string)

def trans(from_address, to_address, amount):
    return YCoin.addTransaction(bc.Transaction(hash(from_address), hash(hash(to_address)), amount))

def printChainHistory():
    print("\nChain History:\n" + str(YCoin))

def printChainValidity():
    print("Chain Valid!") if YCoin.isChainValid() else print("Chain Unvalid!")

def mineBlock(address = None):
    YCoin.minePendingTransactions(hash(hash(address)))

def printAddressBalance(address):
    print(f"Balance {address} = ${YCoin.balanceOfAddress(hash(address))}")

def set_balance(address, amount):
    trans(None, address, amount)
    YCoin.minePendingTransactions(None)

if __name__ == '__main__':
    set_balance('A1', 100)
    trans('A1', 'A2', 50)
    trans('A2', 'A3', 50)
    mineBlock('A2')
    mineBlock('A1')
    mineBlock()

    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')
    printChainValidity()


#   private is hash of name (FOR TESTING PURPOSES NOT CORE)
#   from is private,    name hashed once
#   to is public,       name hashed twice
