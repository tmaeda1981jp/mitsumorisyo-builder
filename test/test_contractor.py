#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
import os
from company import Company


class TestCompanyNormal(unittest.TestCase):

    def setUp(self):
        self.company = Company(os.path.join(os.path.dirname(__file__), 'fixtures/company.normal.conf'))

    def test_name(self):
        self.assertEqual(self.company.name, u'前田 太郎')

    def test_last_name(self):
        self.assertEqual(self.company.last_name, u'前田')

    def test_postal_code(self):
        self.assertEqual(self.company.postal_code, '123-1234')

    def test_address1(self):
        self.assertEqual(self.company.address1, u'札幌市中央区大通1-2-3-4-5')

    def test_address2(self):
        self.assertEqual(self.company.address2, u'xxxマンション1234号室')

    def test_tel(self):
        self.assertEqual(self.company.tel, '123-1234-1234')


class TestCompanyWhenDataIsEmpty(unittest.TestCase):

    def setUp(self):
        self.company = Company(os.path.join(os.path.dirname(__file__), 'fixtures/company.empty.conf'))

    def test_name_return_empty(self):
        self.assertEqual(self.company.name, '')

    def test_last_name_return_empty(self):
        self.assertEqual(self.company.last_name, '')

    def test_postal_code_return_empty(self):
        self.assertEqual(self.company.postal_code, '')

    def test_address1_return_empty(self):
        self.assertEqual(self.company.address1, '')

    def test_address2_return_empty(self):
        self.assertEqual(self.company.address2, '')

    def test_tel_return_empty(self):
        self.assertEqual(self.company.tel, '')


class TestCompanyWhenRequiredPropertiesWereNotDefined(unittest.TestCase):

    def setUp(self):
        self.company = Company(os.path.join(os.path.dirname(__file__), 'fixtures/company.noprop.conf'))

    def test_name_return_empty(self):
        self.assertEqual(self.company.name, '')

    def test_last_name_return_empty(self):
        self.assertEqual(self.company.last_name, '')

    def test_postal_code_return_empty(self):
        self.assertEqual(self.company.postal_code, '')

    def test_address1_return_empty(self):
        self.assertEqual(self.company.address1, '')

    def test_address2_return_empty(self):
        self.assertEqual(self.company.address2, '')

    def test_tel_return_empty(self):
        self.assertEqual(self.company.tel, '')


if __name__ == '__main__':
    unittest.main()
