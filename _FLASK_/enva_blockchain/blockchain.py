'''
Project: Flask Python App
Project ENv: enflask
Date: June 19, 2019
Author: Thomas Maestas
Template Author: https://github.com/dvf/blockchain/blob/master/blockchain.py
'''
import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set() 
        self.new_block(previous_hash='1', proof=100) # genesis block

    def register_node(self, address):
        # add a new node to list of nodes,
        # :param address: eg 'http://192.168.0.5:5000'        
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:  # accepts URL without scheme like '192.169...
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def valid_chain(self, chain):
        # determine if a given blockchain is valid
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n----------\n")
            #check that hash of block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            #check that the Proof of Work is correct
            if not self.valid_proof
        

            


###NOTES::  
    '''
    def new_block(self):   # add new block
        pass

    def new_transaction(self): # add new xaction to list of xactions
        pass

    @staticmethod
    def hash(block):  # hash a block
        pass

    @property
    def last_block(self):  # returns last Block in chain
        pass


    def new_transaction(self, sender, recipient, amount):
            """ Creates new transation to go to next mined Block
            :param sender:<str>
            :param recipient:<str>
            :param amount: <int>
            :return: <int> index of the Block holding xaction """
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
       })

       return self.last_block['index'] + 1
    '''


                        '
    
