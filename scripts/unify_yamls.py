# -*- coding: utf-8 -*-

import click
import logging
import yaml
import os
import sys

from commons import load_yaml_in_memory, write_yaml_on_fs, LEVEL


def get_original_env(application):
    old_env_vars = None
    if 'environment' in application:
        old_env_vars = application['environment']
    return old_env_vars


@click.command()
@click.option('--source', help='Composer source file', prompt=True)
@click.option('--destination', help='Composer destination path')
def include_extensions(source, destination):
    logging.debug('source: {}; destination: {}'.format(source, destination))

    services_yaml = load_yaml_in_memory(source)
    apps_yaml = services_yaml['services']

    for app_name in apps_yaml.keys():
        if 'extends' not in apps_yaml[app_name]:
            logging.debug('skipped {} no extends present'.format(app_name))
            continue

        # Save state of original yaml env_variables
        old_env_vars = get_original_env(apps_yaml[app_name])

        # Retrieve file name from original yaml and load extension in memory
        path_from_extends = apps_yaml[app_name]['extends']['file']
        path_of_extension = os.path.join(os.path.dirname(source), path_from_extends)

        yaml_of_extension = load_yaml_in_memory(path_of_extension)['services']

        # Put the original env_variables in the current yaml
        if old_env_vars:
            yaml_of_extension[app_name]['environment'].update(old_env_vars)

        if len(yaml_of_extension.values()) != 1:
            raise Exception("Unexpected error: lenght of yaml_of_extension.values()")

        # Build new yaml
        apps_yaml[app_name] = yaml_of_extension.values()[0]

    new_yaml = yaml.dump(services_yaml, default_flow_style=False)
    write_yaml_on_fs(destination, new_yaml)


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)
    logging.info('START')
    include_extensions()
    logging.info('END')
