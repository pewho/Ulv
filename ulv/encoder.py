#!/usr/bin/env python
#-*- encoding:utf8 -*-

"""
    Encoder Class
    =============
    Charge to Encode / Decode user input to / from unicode
"""
import collections


class Encoder:

    def __init__(self, encoding='utf8'):
        self.encoding = encoding

    def encode_data(self, data):
        if isinstance(data, str):
            return data.encode(self.encoding)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.encode_data, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.encode_data, data))
        else:
            return data

    def decode_data(self, data):
        if isinstance(data, bytes):
            return data.decode(self.encoding)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.decode_data, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.decode_data, data))
        else:
            return data

