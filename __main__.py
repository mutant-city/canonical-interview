# python internal
import argparse
import os
import re
import sys

# add python modules to import path
dir = re.sub(r'[^/]+(?=/$|$)', '', os.path.realpath(__file__)) + "python_modules"
sys.path.append(dir)

# 3rd party
from python_modules import yaml

# local
import main
from HotCache import HotCache

config_file_path = f'{os.path.dirname(__file__)}/config.yaml'

# Parse
parser = argparse.ArgumentParser(description='Files per Package Count')
parser.add_argument('architecture',
                    help='Input the architecture type.'
                    )
args = parser.parse_args()

# Get config data into dict
with open(config_file_path) as file:
    config_data = file.read()
params = yaml.safe_load(config_data)

# Fetch and extract file
gzip_path = main.fetch_index_file(params['mirror_url'], args.architecture, params['output_location'])
file_path = main.extract_gzip(gzip_path)

# Parse and build dict, insertion and fetch from dict(hash table) is O(1)
program_files = {}
hot_cache = HotCache(params['number_of_items'])

# iterate through file line by line and populate a dict with program => [files...] and populate the hot cache
with open(file_path, errors="surrogateescape") as input_file:
    line_count = 0
    for entry in input_file:
        line_count += 1
        data = re.split(r'\s+', entry)  # split the line
        file = data[0]
        programs = data[1].split(',')  # split the programs in case there's multiple
        print(f"Processing line: {line_count}", end="\r")
        for program in programs:
            if program not in program_files:
                program_files[program] = []
            # Note: all of the dictionary calls are O(1)
            program_files[program].append(file) # note a dict is used, so no duplicates
            # the hot cache is constantly updated with every iteration
            # graphing this would be interesting because some entries would last for a while
            # then be overthrown at some point, some would pop in and out of the cache, etc.
            hot_cache.add(program, len(program_files[program]))


# output final results
num = 1
for item in hot_cache.to_ordered_list():
    print(f"{num}. {item[0]} {item[1]}")
    num += 1
