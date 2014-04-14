#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class QuotationSheetBuilder:

    def __init__(self, template):
        self.template = template

    def build(self, contractor, client, quotation):
        self.template\
            .draw()\
            .set_contractor(contractor)\
            .set_client(client)\
            .set_quotation(quotation)\
            .save()
