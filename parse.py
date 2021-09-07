#!/usr/bin/env python3
import argparse


def parse_args():    
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('files', action='store', nargs='+', help='input files')
    my_parser.add_argument('-w','--wrap', action='store', type=int, default=55, help='wrap size')
    my_parser.add_argument('-o','--output', action='store', type=str, help='name of the output file')
    return my_parser.parse_args()
   

def parse_and_str_header(header_line):
    splitted = [x.strip() for x in header_line.split(None, 3)][1:]
    return f"ID: {splitted[0]}\nValue: {round(float(splitted[1]),1)}\nDescription: {splitted[2]}"
    
   
def print_file(in_file):
    reader = open(in_file, 'r')
    length = 0
    line = reader.readline()
    while line != '':
        if line.startswith('%'):
            print(parse_and_str_header(line))
            length = - len(line.strip())
        length += len(line.strip())
        if (line := reader.readline()) == '' or line.startswith('%'):
            print(f"Sequence length: {length}")


def write_file(in_file, out_file):
    reader = open(in_file, 'r')
    writer = open(out_file, 'w')


parsed_args = parse_args()
print(parsed_args)
for in_file in parsed_args.files:
    if len(parsed_args.files) > 1:
        print(in_file)
    print_file(in_file)
    
    
