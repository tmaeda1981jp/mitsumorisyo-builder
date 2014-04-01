#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
import mock
import contractor
import ConfigParser
import codecs
import os


class TestContractorNormal(unittest.TestCase):

    @mock.patch("contractor.Contractor._getConfigPath")
    def setUp(self, m):
        m.return_value = os.path.join(os.path.dirname(__file__), 'fixtures/contractor.normal.conf')
        self.contractor = contractor.Contractor()

    def test_name(self):
        self.assertEqual(self.contractor.name, u'前田 太郎')

    def test_last_name(self):
        self.assertEqual(self.contractor.last_name, u'前田')

    def test_postal_code(self):
        self.assertEqual(self.contractor.postal_code, '123-1234')

    def test_address1(self):
        self.assertEqual(self.contractor.address1, u'札幌市中央区大通1-2-3-4-5')

    def test_address2(self):
        self.assertEqual(self.contractor.address2, u'xxxマンション1234号室')

    def test_tel(self):
        self.assertEqual(self.contractor.tel, '123-1234-1234')


class TestContractorWhenDataIsEmpty(unittest.TestCase):

    @mock.patch("contractor.Contractor._getConfigPath")
    def setUp(self, m):
        m.return_value = os.path.join(os.path.dirname(__file__), 'fixtures/contractor.empty.conf')
        self.contractor = contractor.Contractor()

    def test_name_return_empty(self):
        self.assertEqual(self.contractor.name, '')

    def test_last_name_return_empty(self):
        self.assertEqual(self.contractor.last_name, '')

    def test_postal_code_return_empty(self):
        self.assertEqual(self.contractor.postal_code, '')

    def test_address1_return_empty(self):
        self.assertEqual(self.contractor.address1, '')

    def test_address2_return_empty(self):
        self.assertEqual(self.contractor.address2, '')

    def test_tel_return_empty(self):
        self.assertEqual(self.contractor.tel, '')


class TestContractorWhenRequiredPropertiesWereNotDefined(unittest.TestCase):

    @mock.patch("contractor.Contractor._getConfigPath")
    def setUp(self, m):
        m.return_value = os.path.join(os.path.dirname(__file__), 'fixtures/contractor.noprop.conf')
        self.contractor = contractor.Contractor()

    def test_name_return_empty(self):
        self.assertEqual(self.contractor.name, '')

    def test_last_name_return_empty(self):
        self.assertEqual(self.contractor.last_name, '')

    def test_postal_code_return_empty(self):
        self.assertEqual(self.contractor.postal_code, '')

    def test_address1_return_empty(self):
        self.assertEqual(self.contractor.address1, '')

    def test_address2_return_empty(self):
        self.assertEqual(self.contractor.address2, '')

    def test_tel_return_empty(self):
        self.assertEqual(self.contractor.tel, '')


if __name__ == '__main__':
    unittest.main()
