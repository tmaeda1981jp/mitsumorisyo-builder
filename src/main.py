#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from company import Company
from quotation import Quotation

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description='mitsumorisyo builder')
    parser.add_argument('-c', '--client', required=True)
    parser.add_argument('-m', '--month', type=int)
    args = parser.parse_args()
    print(args)

    contractor = Company('./contractor.yaml')
    client = Company('./client/%s/client.yaml' % args.client)
    quotation = Quotation('./client/%s/%s.yaml' % (args.client, args.month))

    print unicode(contractor)
    print unicode(client)
    print unicode(quotation)

#    QuotationSheetBuilder(contractor, client, quotation).build()
