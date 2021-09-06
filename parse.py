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
    return f"ID: {splitted[0]}\nValue: {splitted[1]}\nDescription: {splitted[2]}"

print(parse_and_str_header("% MyID1 1.25424 My first text description"))
