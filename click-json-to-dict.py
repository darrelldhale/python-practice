#!/usr/bin/env python3.7

import click
import json
import pprint

pp = pprint.PrettyPrinter()

@click.command
@click.argument('file')
def convert (file):
    with open(file, 'r') as output_file:
        json_file = json.load(output_file)
        pp.pprint(json_file)
