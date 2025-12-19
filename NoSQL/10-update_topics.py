#!/usr/bin/env python3
""" a Python function
"""


def update_topics(mongo_collection, name, topics):
    """ mongo_collection
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
