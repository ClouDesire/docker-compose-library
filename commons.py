# -*- coding: utf-8 -*-

import logging
import yaml

# CONSTANTS
LEVEL = logging.DEBUG


def load_yaml_in_memory(file_path):
    logging.debug('loading file: {}'.format(file_path))
    with open(file_path, 'r') as f:
        return yaml.load(f)


def write_yaml_on_fs(file_path, content):
    if not file_path:
        print content
        return
    logging.debug('writing file: {}'.format(file_path))
    with open(file_path, 'w') as f:
        f.write(content)
