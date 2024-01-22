#!/usr/bin/env python3
''' '''


def schools_by_topic(mongo_collection, topic):
    ''' '''
    document = mongo_collection.find({'topics': topic})
    return document
