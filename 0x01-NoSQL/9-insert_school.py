#!/usr/bin/env python3
"""
File : 9-insert_school.py
Desc : a python file containing a function to inssertion
Author : Kaleab Shiferaw Girma
Date : 11th April, 2023
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    A method to insert a new document to collection
    """
    result = mongo_collection.insert_one(kwargs)
    new_id = result.inserted_id

    return new_id;
