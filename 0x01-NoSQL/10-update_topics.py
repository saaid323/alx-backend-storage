#!/usr/bin/env python3
'''changes all topics of a school document based on the name'''


def update_topics(mongo_collection, name, topics):
    documents = mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})
