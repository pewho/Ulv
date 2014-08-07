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
    def __init__(self, filename, header, delimiter=',', quotechar='"', encoding='utf-8'):
        self.filename = filename
        self.header = header
        self.quotechar = quotechar
        self.delimiter = delimiter
        self.encoding = encoding
        self.quoteStrategy = csv.QUOTE_ALL if self.quotechar != '' else csv.QUOTE_NONE
        with open(self.filename, 'w') as fwrite:
            writer = csv.DictWriter(fwrite, self.header,
                                    delimiter=self.delimiter,
                                    quotechar=self.quotechar,
                                    quoting=self.quoteStrategy)
            writer.writeheader()

    def write_row(self, row):
        with open(self.filename, 'a') as fwrite:
            writer = csv.DictWriter(fwrite,
                                    self.header,
                                    delimiter=self.delimiter,
                                    quotechar=self.quotechar,
                                    quoting=self.quoteStrategy)
            writer.writerow(row)

    def write_rows(self, rows):
        with open(self.filename, 'a') as fwrite:
            writer = csv.DictWriter(fwrite,
                                    self.header,
                                    delimiter=self.delimiter,
                                    quotechar=self.quotechar,
                                    quoting=self.quoteStrategy)
            writer.writerows(rows)