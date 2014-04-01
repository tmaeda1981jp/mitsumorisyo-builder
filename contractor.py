#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class Contractor:

    def __init__(self):
        conf = self._getConfig()

        for prop in ['name', 'postal_code', 'address1', 'address2', 'tel']:
            try:
                self.__dict__[prop] = conf.get('contractor', prop)
            except:
                self.__dict__[prop] = ''

    def _getConfig(self):
        import codecs
        import ConfigParser

        conf = ConfigParser.SafeConfigParser()
        conf.readfp(codecs.open('./contractor.conf', 'r', 'utf8'))
        return conf

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
