#!/usr/bin/env python3
""" Python function
"""


def schools_by_topic(mongo_collection, topic):
    """ mongo_collection
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
