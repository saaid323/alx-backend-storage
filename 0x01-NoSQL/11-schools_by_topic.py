#!/usr/bin/env python3
'''returns the list of school having a specific topic:'''


def schools_by_topic(mongo_collection, topic):
    '''function that returns the list of school having a specific topic'''
    document = mongo_collection.find({'topics': topic})
    return document
