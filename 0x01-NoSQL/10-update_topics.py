#!/usr/bin/env python3
'''changes all topics of a school document based on the name'''


def update_topics(mongo_collection, name, topics):
    '''function that changes all topics of a school document based on the name'''
    documents = mongo_collection.update({'name': name},
            {'$set': {'topics': topics}})
