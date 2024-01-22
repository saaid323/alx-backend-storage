#!/usr/bin/env python3
''' '''
from pymongo import MongoClient


if __name__ == "__main__":
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["logs"]
    mycol = mydb["nginx"]
    print(mycol.find_one())
    print(mycol.count_documents({}))
