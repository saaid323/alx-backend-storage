#!/usr/bin/env python3
'''script that provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


if __name__ == "__main__":
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["logs"]
    mycol = mydb["nginx"]
    print(mycol.find_one())
    print(mycol.count_documents({}), 'logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in methods:
        result = mycol.count_documents({'method': i})
        print(f'\tmethod {i}: {result}')
    print(mycol.count_documents({'path': '/status'}), 'status check')
    
