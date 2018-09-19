#!/usr/bin/env python

from lib import generate
from python_terraform import *

import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate, plan and apply terraform scripts in templates.')
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='Valid subcommands:',
                                       dest='generate')
    subparsers.add_parser('generate', help='Generate Terraform scripts for the files listed in templates/.')
    parser.add_argument('--plan', '-p', metavar='<TEMPLATE_NAME>', help='Plan given Terraform script.')
    parser.add_argument('--apply', '-a', metavar='<TEMPLATE_NAME>', help='Apply given Terraform script.')
    args = parser.parse_args()

    tf = Terraform(working_dir='output/')
    tf.init()

    if args.generate:
        generate.templates()
    elif args.plan:
        print(tf.plan(no_color=IsFlagged, refresh=False, capture_output=True))
    elif args.apply:
        print("APPLY")
    else:
        print("OUTRO")


if __name__ == '__main__':
    main()
