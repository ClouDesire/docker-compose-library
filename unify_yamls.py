# -*- coding: utf-8 -*-

import click
import yaml

def load_yaml_in_memory(file_path):
    # TODO: log debug with what I'm doing here
    with open(file_path, 'r') as f:
        return yaml.load(f)

def get_original_env(application):
    old_env_vars = None
    if 'environment' in application:
        old_env_vars = application['environment']
    return old_env_vars

@click.command()
@click.option('--source', help='Composer source file', prompt=True)
@click.option('--destination', default='~', help='Composer destination path [to implement]')
def include_extensions(source, destination):
    # TODO: log debug with source and destination
    apps_yaml = load_yaml_in_memory(source)

    for app_name in apps_yaml.keys():
        if 'extends' not in apps_yaml[app_name]:
            # TODO: log debug for app_name skipped
            continue

        # Save state of original yaml env_variables
        old_env_vars = get_original_env(apps_yaml[app_name])

        # Retrieve file name from original yaml and load extension in memory
        path_of_extension = apps_yaml[app_name]['extends']['file']
        yaml_of_extension = load_yaml_in_memory(path_of_extension)

        # Put the original env_variables in the current yaml
        if old_env_vars:
            yaml_of_extension[app_name]['environment'].update(old_env_vars)

        if len(yaml_of_extension.values()) != 1:
            raise "Unexpected error: lenght of yaml_of_extension.values()"

        # Build new yaml
        apps_yaml[app_name] = yaml_of_extension.values()[0]

    # TODO: Save new yaml to file system
    print yaml.dump(apps_yaml, default_flow_style=False)

if __name__ == '__main__':
    include_extensions()
