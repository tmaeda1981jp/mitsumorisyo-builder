#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import setting
from yaml_loader import YamlLoader


class Quotation:

    def __init__(self, yaml_path):
        properties = [
            'title', 'time_for_payment', 'payment_terms',
            'quote_expiration_date', 'estimate_conditions',
            'items']
        for key, value in YamlLoader.load(yaml_path, properties).items():
            self.__dict__[key] = value

    def get_total_amount_without_tax(self):
        """ 税抜き金額を返す
        """
        return sum(map(lambda item: item['price'] * item['quantity'],
                       self.items))

    def get_total_amount_with_tax(self):
        """ 税込金額を返す
        """
        return self.get_total_amount_without_tax() + self.get_consumption_tax()

    def get_consumption_tax(self):
        """ 消費税を返す
        """
        return int(self.get_total_amount_without_tax() * setting.TAX_RATE)

    def get_withholding_tax(self):
        """ 源泉徴収税額を返す
        """
        return int(self.get_total_amount_without_tax()
                   * setting.WITHHOLDING_TAX_RATE)

    @property
    def title(self):
        return self.title

    @property
    def time_for_payment(self):
        return self.time_for_payment

    @property
    def payment_terms(self):
        return self.payment_terms

    @property
    def quote_expiration_date(self):
        return self.quote_expiration_date

    @property
    def estimate_conditions(self):
        return self.estimate_conditions

    @property
    def items(self):
        return self.items

    def __unicode__(self):
        return "[%s]" % self.title

if __name__ == '__main__':
    q = Quotation('./client/company_a/201404.yaml')
    print q.get_total_amount_without_tax()
    print q.get_total_amount_with_tax()
    print q.get_consumption_tax()
