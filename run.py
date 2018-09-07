#!/usr/bin/env python

from lib import generate

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

    if args.generate:
        generate.templates()
    elif args.plan:
        print("PLAN")
    elif args.apply:
        print("APPLY")
    else:
        print("OUTRO")


if __name__ == '__main__':
    main()
