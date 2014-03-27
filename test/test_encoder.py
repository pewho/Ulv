#!/usr/bin/env python
# -*- encoding:utf8 -*-
import pytest
from ulv.encoder import Encoder


class TestEncoder:
    #noinspection PyUnresolvedReferences
    @pytest.fixture
    def encoder_default(self):
        return Encoder('utf8')

    def test_encode_data_str(self, encoder_default):
        return_data = encoder_default.encode_data('test')
        assert isinstance(return_data, bytes)

    def test_encode_data_mapping(self, encoder_default):
        return_data = encoder_default.encode_data({'test': 'plop', 'test1': 'plup'})
        for key, value in return_data.items():
            assert isinstance(key, bytes)
            assert isinstance(value, bytes)

    def test_encode_already_encoding(self, encoder_default):
        data_unicode = '@àé~&&'
        assert isinstance(data_unicode, str)
        data_latin1 = data_unicode.encode('latin_1')
        assert isinstance(data_latin1, bytes)
        assert data_latin1 == encoder_default.encode_data(data_latin1)

    def test_encode_data_iterable(self, encoder_default):
        return_data = encoder_default.encode_data(['test', 'test'])
        for val in return_data:
            assert isinstance(val, bytes)

    def test_decode_data_utf8(self, encoder_default):
        data_unicode = '@àé~&&'
        assert isinstance(data_unicode, str)
        data_utf8 = data_unicode.encode('utf8')
        assert isinstance(data_utf8, bytes)
        return_data = encoder_default.decode_data(data_utf8)
        assert return_data == data_unicode

    def test_decode_invalid_encoding(self, encoder_default):
        data_unicode = '@àé~&&'
        assert isinstance(data_unicode, str)
        data_latin1 = data_unicode.encode('latin_1')
        assert isinstance(data_latin1, bytes)
        with pytest.raises(UnicodeDecodeError):
            encoder_default.decode_data(data_latin1)

    def test_decode_data_iterable(self, encoder_default):
        return_data = encoder_default.decode_data(['test'.encode('utf8'), 'test2'.encode('utf8')])
        for val in return_data:
            assert isinstance(val, str)

    def test_decode_data_dict(self, encoder_default):
        return_data = encoder_default.decode_data(
            {'test'.encode('utf8'): 'plop'.encode('utf8'),
             'test2'.encode('utf8'): 'plup'.encode('utf8')}
        )
        for key, val in return_data.items():
            assert isinstance(key, str)
            assert isinstance(val, str)

    def test_decode_other_type(self, encoder_default):
        val = encoder_default.decode_data(1)
        assert isinstance(val, int)
        val = encoder_default.decode_data([3, 4.0])
        assert isinstance(val[0], int)
        assert isinstance(val[1], float)

    def test_encode_other_type(self, encoder_default):
        return_data = encoder_default.encode_data(2)
        assert isinstance(return_data, int)
        return_data = encoder_default.encode_data([3, 408.5])
        assert isinstance(return_data[0], int)
        assert isinstance(return_data[1], float)

    def test_empty_iterable(self, encoder_default):
        assert isinstance(encoder_default.decode_data([]), list)
        assert isinstance(encoder_default.encode_data([]), list)

    def test_empty_map(self, encoder_default):
        assert isinstance(encoder_default.decode_data({}), dict)
        assert isinstance(encoder_default.decode_data({}), dict)

    def test_recusrsive_empty_collections(self, encoder_default):
        val_enc = {'test'.encode('utf8'): []}
        val = {'test': []}
        assert val == encoder_default.decode_data(val_enc)
        assert val_enc == encoder_default.encode_data(val)