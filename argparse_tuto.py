#!/usr/bin/python

import argparse
import sys

def set_policy(args):
    print args.set_policy


#  create the top-level parser
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

# create ranger parser
ranger_parser = subparser.add_parser('ranger')
ranger_parser.add_argument('-set_policy', type=str, required=True, choices=['nifi', 'hive'],
                           help="set ranger policy for Nifi's hdfs access and hive", nargs=1)
ranger_parser.set_defaults(func=set_policy)

def run(args):
    return parser.parse_args(args)


#args = parser.parse_args('ranger -set_policy coucou!'.split())
#args.func(args)

if __name__ == '__main__':
    run(sys.argv)


