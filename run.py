#!/usr/bin/env python

from terrascript import *
from templates import *

import sys
import yaml


def get_config():
    """Load Config YAML file."""
    with open('config.yml') as f:
        configuration = yaml.load(f)

    return configuration


def main():
    environment = 'test'
    cfg = get_config() 
    env = cfg['environments'][environment]

    cluster, sg_alb, sg_cluster, launch_config = ecs_cluster.ecs_cluster(cfg['cluster_name'], env['instance_type'], env['ami_id'] , env['min_instance'], env['max_instance'])
    print(dump())


if __name__ == '__main__':
    main()
