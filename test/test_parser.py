#!/usr/bin/env python
# -*- encoding:utf8 -*-
import os

import pytest

from ulv.parser import Importer


class TestImporter:
    @pytest.fixture
    def importer(self):
        return Importer('%s/fixture/test_csv.csv' % os.path.dirname(os.path.realpath(__file__)))

    @pytest.fixture
    def importer_iso(self):
        return Importer('%s/fixture/test_encoding.csv' % os.path.dirname(os.path.realpath(__file__)),
                        encoding='latin_1')

    def test_import_data(self, importer):
        assert 16 == len(importer.data)
        assert {'pw_ccpro__IsoCode_2__c': 'XK',
                'Id': 'a14D00000011g7UIAQ',
                'Name': 'Kosovo',
                'pw_ccpro__IsoCode_3__c': 'XKX'} == importer.data[0]

    def test_get_header(self, importer):
        assert ['Name', 'pw_ccpro__IsoCode_2__c', 'pw_ccpro__IsoCode_3__c', 'Id'] == importer.get_header()

    def test_get_csv_with_other_encoding(self, importer_iso):
        assert {'Name': 'éspèrluette', 'Value': '&'} == importer_iso.data[0]

class TestExporter:
    pass