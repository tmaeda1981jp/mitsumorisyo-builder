#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from yaml_loader import YamlLoader


class Company:

    def __init__(self, yaml_path):
        properties = ['name', 'postal_code', 'address1', 'address2', 'tel']
        for key, value in YamlLoader.load(yaml_path, properties).items():
            self.__dict__[key] = value

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

    def __unicode__(self):
        return u"[%s|%s|%s|%s|%s]" % (self.name, self.postal_code,
                                      self.address1, self.address2, self.tel)

if __name__ == '__main__':
    Company('../contractor.yaml')
