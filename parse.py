#!/usr/bin/env python3
import argparse


def parse_args():    
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('files', action='store', nargs='+', help='input files')
    my_parser.add_argument('-w','--wrap', action='store', type=int, help='wrap size')
    my_parser.add_argument('-o','--output', action='store', type=str, help='name of the output file')
    return my_parser.parse_args()
   

def parse_and_str_header(header_line):
    splitted = [x.strip() for x in header_line.split(' ', 3)][1:]
    return f"ID: {splitted[0]}\nValue: {round(float(splitted[1]),1)}\nDescription: {splitted[2]}"
    
   
def print_file(in_file):
    reader = open(in_file, 'r')
    length = 0
    print(parse_and_str_header(reader.readline()))
    while (line := reader.readline()) != '':
        if line.startswith('%'):
            print(f"Sequence length: {length}\n")
            print(parse_and_str_header(line))
            length = - len(line)
        length = length + len(line) if not line == '\n' else length
    print(f"Sequence length: {length}")
            

parsed_args = parse_args()
for in_file in parsed_args.files:
    if len(parsed_args.files) > 1:
        print(in_file)
    print_file(in_file)
    
    
