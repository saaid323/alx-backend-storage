#!/usr/bin/env python3
''' inserts a new document in a collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
    '''function that inserts a new document in a collection based on kwargs'''
    dic = {}
    for k, v in kwargs.items():
        dic[k] = v
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
