#!/usr/bin/env python
# -*- encoding:utf8 -*-
"""
    Parser Module
    =============
    This module is charged to manipulate CSV Files, to import them, or to write them on file.
"""
import csv


class Importer:
    def __init__(self, filename, delimiter=',', quotechar='"', encoding='utf-8'):
        self.filename = filename
        self.quotechar = quotechar
        self.delimiter = delimiter
        self.encoding = encoding
        self.data, self.header = self.hydrate()

    def hydrate(self):
        with open(self.filename, 'r', encoding=self.encoding) as f:
            reader = csv.DictReader(f, delimiter=self.delimiter, quotechar=self.quotechar)
            data = []
            for row in reader:
                data.append(row)
        return data, reader.fieldnames

    def get_header(self):
        return self.header


class Exporter:
    pass