#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from company import Company
from quotation import Quotation
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='quotation-sheet-builder')
    parser.add_argument('-c', '--client', required=True)
    parser.add_argument('-m', '--month', type=int)
    args = parser.parse_args()
    print(args)

    try:
        contractor = Company('./contractor.yaml')
        client = Company('./client/%s/client.yaml' % args.client)
        quotation = Quotation('./client/%s/%s.yaml' %
                              (args.client, args.month))
    except IOError as message:
        print message
        exit(1)

    print unicode(contractor)
    print unicode(client)
    print unicode(quotation)

#    QuotationSheetBuilder(contractor, client, quotation).build()
