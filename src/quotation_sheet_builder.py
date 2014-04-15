#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import logging


class QuotationSheetBuilder:

    def __init__(self, template):
        self.template = template

    def build(self, contractor, client, quotation):
        try:
            self.template\
                .draw()\
                .set_contractor(contractor)\
                .set_client(client)\
                .set_quotation(quotation)\
                .save()

        except Exception as message:
            exit(logging.error(message))
