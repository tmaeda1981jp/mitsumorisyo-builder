#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import codecs
import yaml


class YamlLoader:

    @staticmethod
    def load(path, props):

        if not os.path.exists(path):
            raise IOError("%s is not found." % path)

        data = yaml.load(codecs.open(path, 'r', 'utf8'))
        result = {}
        for key in props:
            if key in data:
                prop = data[key]
                result[key] = prop if prop is not None else ''
            else:
                result[key] = ''
        return result
