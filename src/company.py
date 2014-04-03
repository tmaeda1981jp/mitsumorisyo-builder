#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class Company:

    def __init__(self, configPath):
        import codecs
        import ConfigParser
        properties = {'name': '',
                      'postal_code': '',
                      'address1': '',
                      'address2': '',
                      'tel': ''}
        conf = ConfigParser.SafeConfigParser(properties)
        conf.readfp(codecs.open(configPath, 'r', 'utf8'))

        for prop in properties.keys():
            self.__dict__[prop] = conf.get('company', prop)

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
    def addres1(self):
        return self.address1

    @property
    def address2(self):
        return self.address2

    @property
    def tel(self):
        return self.tel
