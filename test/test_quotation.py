#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import unittest
import os
from quotation import Quotation


class TestQuotationNormal(unittest.TestCase):

    def setUp(self):
        self.quotation = Quotation(
            os.path.join(os.path.dirname(__file__),
                         'fixtures/quotation.normal.yaml'))

    def test_title(self):
        self.assertEqual(self.quotation.title, u'2014年4月分御見積')

    def test_time_for_payment(self):
        self.assertEqual(self.quotation.time_for_payment, u'2014年5月')

    def test_payment_terms(self):
        self.assertEqual(self.quotation.payment_terms, u'20日締翌月末')

    def test_quotation_expiration_date(self):
        self.assertEqual(self.quotation.quote_expiration_date, u'30日')

    def test_estimate_condition(self):
        self.assertEqual(
            self.quotation.estimate_conditions,
            u'仕様追加発生の場合は別途御見積り')

    def test_items(self):
        self.assertEqual(len(self.quotation.items), 3)
        self.assertEqual(self.quotation.items[0]['item'], u'アイテム１')
        self.assertEqual(self.quotation.items[1]['item'], u'アイテム２')
        self.assertEqual(self.quotation.items[2]['item'], u'アイテム３')

    def test_get_total_amount_without_tax(self):
        self.assertEqual(
            self.quotation.get_total_amount_without_tax(),
            100000 + (2 * 250000) + (3 * 500000))

    def test_get_total_amount_with_tax(self):
        self.assertEqual(
            self.quotation.get_total_amount_with_tax(),
            int((100000 + (2 * 250000) + (3 * 500000)) * 1.08)) # TODO read from setting

    def test_get_consumption_tax(self):
        self.assertEqual(
            self.quotation.get_consumption_tax(),
            int((100000 + (2 * 250000) + (3 * 500000)) * 0.08)) # TODO read from setting

    def test_get_withholding_tax(self):
        self.assertEqual(
            self.quotation.get_withholding_tax(),
            int((100000 + (2 * 250000) + (3 * 500000)) * 0.1021))


if __name__ == '__main__':
    unittest.main()
