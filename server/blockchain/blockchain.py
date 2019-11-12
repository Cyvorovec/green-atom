    
import json
import hashlib


# Инфа в блоке
class Block:
    def __init__(self, index, timestamp, data, previousHash=' '):
        self.index = id
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        return hashlib.sha256(str(self.index) + self.previousHash + self.timestamp + json.dumps(self.data)).hexdigest()

    def printBlock(self):
        print ("Block #") + str(self.index)
        print ("Account: ") + str(self.data["account"])
        print ("Amount: ") + str(self.data["amount"])
        print ("Block Hash: ") + str(self.hash)
        print ("Block Previous Hash: ") + str(self.previousHash)
        print ("---------------")


# Блоки блок чейна
class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "10/01/2017", "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range (1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True

    def printBlockChain(self):
        for i in range(1, len(self.chain)):
            self.chain[i].printBlock()


def main():
    annaCoin = BlockChain()
    annaCoin.addBlock(Block(1, "10/10/2017", {"Name": "Anna","testimony": 25,"action": "to pay"}))
    annaCoin.addBlock(Block(2, "11/01/2017", {"Name": "Epifancev","testimony": 10,"action": "to pay"}))
    annaCoin.addBlock(Block(3, "12/01/2017", {"Name": "Katie","testimony": 20,"action": "to pay"}))
    annaCoin.addBlock(Block(4, "12/07/2017", {"Name": "Pahom","testimony": 4,"action": "to pay"}))
    annaCoin.printBlockChain()


if __name__ == '__main__':
    main()