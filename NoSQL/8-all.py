#!/usr/bin/env python3
"""
a listing all py code
"""


def list_all(mongo_collection):
    """
    listall
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
