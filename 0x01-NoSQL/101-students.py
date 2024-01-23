#!/usr/bin/env python3
'''returns all students sorted by average score'''


def top_students(mongo_collection):
    '''function that returns all students sorted by average score'''
    documents = mongo_collection.aggregate([{'$group': {'_id': '$_id', 'name': {'$first':'$name'}, 'averageScore': {'$avg': {"$avg": '$topics.score'}}}}, {'$sort': {'averageScore': -1}}])
    return documents
