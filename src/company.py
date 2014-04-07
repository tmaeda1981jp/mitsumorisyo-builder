#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import yaml


class Company:

    def __init__(self, yaml_path):
        import codecs
        data = yaml.load(codecs.open(yaml_path, 'r', 'utf8'))
        for key in ['name', 'postal_code', 'address1', 'address2', 'tel']:
            if key in data:
                prop = data[key]
                self.__dict__[key] = prop if prop is not None else ''
            else:
                self.__dict__[key] = ''


    @property
    def name(self):
        return self.name

    @property
    def last_name(self):
        return self.name.split(' ')[0]

    @property
    def postal_code(self):
        return self.postal_code

    @property
    def address1(self):
        return self.address1

    @property
    def address2(self):
        return self.address2

    @property
    def tel(self):
        return self.tel

if __name__ == '__main__':
    Company('../contractor.yaml')
