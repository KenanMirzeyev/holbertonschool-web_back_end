#!/usr/bin/env python3
""" a Python function
"""


def insert_school(mongo_collection, **kwargs):
    """ mongo_collection
    """
    document_id = mongo_collection.insert(kwargs)
    return document_id
