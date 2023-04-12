#!/usr/bin/env python3
'''
File: exercise.py
Description: a file initializing a cache class
Author: Kaleab Shiferaw Girma
'''
import uuid
import redis

class Cache():
    '''
    Cache class
    '''
    def __init__(self):
        '''
        initializer method
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
