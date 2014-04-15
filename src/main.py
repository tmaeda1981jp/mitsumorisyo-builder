#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from company import Company
from quotation import Quotation
from quotation_sheet_builder import QuotationSheetBuilder
from default_quotation_sheet_template import DefaultQuotationSheetTemplate
import argparse
import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG,
                        format='\033[91m[%(levelname)s]\033[0m %(message)s')

    parser = argparse.ArgumentParser(description='quotation-sheet-builder')
    parser.add_argument('-c', '--client', required=True)
    parser.add_argument('-m', '--month', type=int)
    args = parser.parse_args()

    try:
        contractor = Company('./contractor.yaml')
        client = Company('./client/%s/client.yaml' % args.client)
        quotation = Quotation('./client/%s/%s.yaml' %
                              (args.client, args.month))
    except IOError as message:
        exit(logging.error(message))

    file_path = '_build/%s_%s.pdf' % (args.client, args.month)
    template = DefaultQuotationSheetTemplate(file_path)
    QuotationSheetBuilder(template).build(contractor, client, quotation)
