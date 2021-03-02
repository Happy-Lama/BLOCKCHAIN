import time
import hashlib

class Block:
    """
        This is the block class for the blocks to be added to the blockchain
    """

    def __init__(self, last_hash):
        self.prevHash = last_hash
        self.timeOpened = time.time()
        self.data = []
        self.closed = False
        self.timeClosed = time.time()#to be adjusted to only when it closes 
        self.hash = hashlib.md5("{}".format(self.data).encode()).hexdigest()#to be adjusted to only hash when it closes
        self.next = None

    def write(self,info):
        # Method to record information in the block while its open
        if self.closed == False:  
            timestamp = time.time()
            data_in = info
            written_data = {
                'timestamp':timestamp,
                'data': data_in
            }
            self.data.insert(written_data)     

    def join(self,next_block):
        # Method that joins current block to the previous block in the block chain after it closes
        #Note has to be adjusted to work properly
        if next_block == None:
            self.next = next_block
        else:
            if next_block.prevHash == self.hash:
                self.next = next_block
            else:
                print("Rejected: Block has been tampered with")

    def __repr__(self):
        return f"""[\n   prevHash: {self.prevHash},\n    timeOpened: {self.timeOpened},\n    data: {self.data},\n    timeClosed: {self.timeClosed},\n    hash: {self.hash},\n    next: {self.next}\n]"""


class BlockChain:
    """
        This is the blockchain class for the whole blockchain system
    """
    def __init__(self):
        self.head = None

    def add(self,block):
        # Adds blocks to the chain after they are closed
        current = block
        current.join(self.head)
        self.head = current

    def search(self, lookup_data):
        # Search for data recorded in the chain
        found = False
        current = self.head
        while current and not found:
            for i in current.data:
                if i["data"] == lookup_data:
                    found = True
            current = current.next
        return current

    def len(self):
        # returns the length of the chain excluding the first block/item in block which is 
        # a None object
        current = self.head
        x = 0
        while current != None:
            x += 1
            current = current.next
        return x

    def __repr__(self):
        out = "["
        while current:
            out += f"{current} ==> "
        return out + "]"
