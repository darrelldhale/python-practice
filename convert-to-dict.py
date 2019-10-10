#!/usr/bin/env python3.7
"""
Command line tool to convert json to python dict.
"""

import argparse
import json
import pprint

pp = pprint.PrettyPrinter()

def convert(file):
    with open(file, 'r') as output_file:
        json_file = json.load(output_file)
        pp.pprint(json_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Json-to-Dict')

    parser.add_argument('convert', choices=['convert'])
    parser.add_argument('file', help='a json file to convert')

    args = parser.parse_args()
    convert(args.file)
