import blockchain as bc
YCoin = bc.Blockchain(difficulty = 3, mining_reward = 100)

def pay(from_address, to_address, amount, chain = YCoin):
    private_from_address = bc.hash(from_address)
    public_to_address = bc.hash(bc.hash(to_address))
    return chain.addTransaction(bc.Transaction(private_from_address, public_to_address, amount))

def printChainHistory(chain = YCoin):
    print("\nChain History:\n" + str(chain))

def printChainValidity(chain = YCoin):
    print("Chain Valid!") if chain.chain_validity() else print("Chain Unvalid!")

def mineBlock(to_address = None, chain = YCoin):
    public_to_address = bc.hash(bc.hash(to_address))
    chain.minePendingTransactions(public_to_address)

def printAddressBalance(address, chain = YCoin):
    private_address = bc.hash(address)
    print(f"Balance of {address} = ${chain.balance_of_address(private_address)}")

def setBalance(address, amount):
    pay(None, address, amount)
    mineBlock()

if __name__ == '__main__':
    setBalance('A1', 10)
    pay('A1', 'A2', 3)
    mineBlock('A2')
    pay('A2', 'A3', 6)
    mineBlock()

    printAddressBalance('A1')
    printAddressBalance('A2')
    printAddressBalance('A3')
    printAddressBalance(None)
    printChainValidity()

#   private is hash of name (FOR TESTING PURPOSES ONLY)
#   from is private,    name hashed once
#   to is public,       name hashed twice
