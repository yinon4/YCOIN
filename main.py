import blockchain as bc
YCoin = bc.Blockchain(difficulty = 3, mining_reward = 100)

def pay(from_address, to_address, amount, chain = YCoin):
    private_from_address = bc.hash(from_address)
    public_to_address = bc.hash(bc.hash(to_address))
    return chain.addTransaction(bc.Transaction(private_from_address, public_to_address, amount))

def printChainHistory(chain = YCoin):
    print("\nChain History:\n" + str(chain))

def printChainValidity(chain = YCoin):
    print("Chain Valid!") if chain.isChainValid() else print("Chain Unvalid!")

def mineBlock(address = None, chain = YCoin):
    public_address = bc.hash(bc.hash(address))
    chain.minePendingTransactions(public_address)

def printAddressBalance(address, chain = YCoin):
    private_address = bc.hash(address)
    print(f"Balance of {address} = ${chain.balanceOfAddress(private_address)}")

def set_balance(address, amount, chain = YCoin):
    pay(None, address, amount)
    chain.minePendingTransactions(None)

if __name__ == '__main__':
    set_balance('A1', 10)
    pay('A1', 'A2', 3)
    mineBlock('A2')
    pay('A2', 'A3', 6)
    mineBlock()

    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')
    printChainValidity()

#   private is hash of name (FOR TESTING PURPOSES NOT CORE)
#   from is private,    name hashed once
#   to is public,       name hashed twice
