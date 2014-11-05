#!/usr/bin/env python
# -*- encoding:utf8 -*-
"""
    Encoder Class
    =============
    Charge to Encode / Decode user input to / from unicode
"""
import collections


class Encoder:
    """
        Encode to / Decode from a specific encoding <> Unicode.

        :Example:
        >>> enc = Encoder('latin_1')
        >>> val = 'test'
        >>> type(val)
        <class 'str'>
        >>> val_encoded = enc.encode_data(val)
        >>> type(val_encoded)
        <class 'bytes'>
        >>> print(val_encoded)
        b'test'
        >>> unicode_val = enc.decode_data(val_encoded)
        <class 'str'>
        >>> print(unicode_val)
        test
    """
    def __init__(self, encoding='utf8'):
        """
            :param encoding: encoding used for convertion
        """
        self.encoding = encoding

    def encode_data(self, data):
        """
            Encode from unicode to a byteString.

            This convert an unicode string to bytes string,
            or recursively unicode string on iterable / dict
            to the selected encoding. Other type is conserved.

            :param data: the string to convert, or an iterable, or a dict
        """
        if isinstance(data, str):
            return data.encode(self.encoding)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.encode_data, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.encode_data, data))
        else:
            return data

    def decode_data(self, data):
        """
        Decode from a byteString to unicode.

        This convert a byte string to unicode,
        or recursively bytes string on iterable / dict
        from the selected encoding. Other type is conserved.

        :param data: the string to convert, or an iterable, or a dict
        """
        if isinstance(data, bytes):
            return data.decode(self.encoding)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.decode_data, data.items()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.decode_data, data))
        else:
            return data
