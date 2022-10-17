#What is a blockchain?
#A blockchain comprises of several blocks that are joined to each other
#The best part is that if one block chain is disturbed then the others will be invalid
#Now first we will create the block class
import hashlib
from os import stat
import time

class Block: 
    def __init__(self, index, proof_no, prev_hash, data, timestamp = None):
       self.index = index  #self referes to the instance of the block classs, making it possible to access the methods and attrcibutes associated with the class.
       #index is used to track the position of the block within the blockchain
       self.proof_no = proof_no  #this is the number which is created during the creation of a new block
       self.prev_hash = prev_hash #this referes to the hash of previous block within the chain
       self.data = data #this contains the data of all the transactions 
       self.timestamp = timestamp #this is used to place a timestamp for the transactions

    @property
    def calculate_hash(self):

        #this method will generate the hash of the block
        block_of_string  = "{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)
        #we have used the sha 256 module and it is imported into the project to assist in obtaining the hashes of every block.
        return hashlib.sha256(block_of_string.encode()).hexdigest()



#The main purpose of blockchain is to connect or chain all the blockchains together so thus we are going to create a new blockchain class


class BlockChain:
    def __init__(self) -> None:
        self.chain = [] #this variable will keep all the block
        self.present_data = [] #this variable will be storing all the completed transactions in the block
        self.construct_genesis() #this will be constructing the initial block

    def construct_genesis(self):
        self.construct_block(proof_no = 1, prev_hash = 1)
#setting both the values as 1 because why not lol

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index = len(self.chain),
            #index represents the lenght of the blockchain
            proof_no = proof_no,
            prev_hash = prev_hash,
            #caller method passed
            data = self.present_data)
            #it resets the transaction list on the node.
            #Basically, everytime transactions happens it resests the list and it goes on.

        self.present_data = []

        self.chain.append(block)
        #this joins the newly constructed blocks to the chain
        return block
        #lastly we are returning the block

    
        @staticmethod
        #now we will check the validity. Just a simple method which uses if else and then return true or false.
        def check_validity(block, prev_block):
            if prev_block.index + 1 != block.index:
                return False

            elif prev_block.calculate_hash != block.prev_hash:
                return False
        
            elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
                return False

            elif block.timestamp <= prev_block.timestamp:
                return False

            return True
            

        def new_data(self, sender, recipient, quantity):
            self.present_data.append({
                'sender' : sender,
                'recipient' : recipient,
                'quantity' : quantity
            })
            return True

    #Adding proof of work. Proof of work is a concept that prevents the blockchain from abuse.

        @staticmethod
        def proof_of_work(lat_proof):
             '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
        proof_no = 1
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

            return proof_no


        @staticmethod
        def verifying_proof(last_proof, proof):
            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "000"


        @property
        def last_block(self):
            return self.chain[-1]