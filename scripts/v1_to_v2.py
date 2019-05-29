# -*- coding: utf-8 -*-

import click
import logging
import yaml
import sys

from commons import load_yaml_in_memory, write_yaml_on_fs, LEVEL


def modify_volumes(volume_list):
    new_volume_list = []
    for volume in volume_list:
        if not volume.startswith('./'):
            volume = './' + volume
        new_volume_list.append(volume)
    return new_volume_list


@click.command()
@click.option('--source', help='Composer source file', prompt=True)
@click.option('--destination', help='Composer destination path')
def from_v1_to_v2(source, destination):
    logging.debug('source: {}; destination: {}'.format(source, destination))

    apps_yaml = load_yaml_in_memory(source)

    # edit volume if not starts with ./
    for app_name, app_body in apps_yaml.items():
        for prop, values in app_body.items():
            if prop == 'volumes':
                apps_yaml[app_name][prop] = modify_volumes(values)

    # Workaround because: http://pyyaml.org/ticket/29
    new_yaml = "version: '2'\n" + yaml.dump({'services': apps_yaml}, default_flow_style=False)

    write_yaml_on_fs(destination, new_yaml)


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)
    logging.info('START')
    from_v1_to_v2()
    logging.info('END')
