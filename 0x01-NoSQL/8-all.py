#!/usr/bin/env python3
"""
file: 8-all.py
Description: a python file containing a method
Author: Kaleab Shiferaw Girma
Date: 11th April, 2023
"""


def list_all(mongo_collection):
    """
    A method to list all documents of a collection
    """
    mylist = []
    for i in mongo_collection.find():
        mylist.append(i)
    return mylist
