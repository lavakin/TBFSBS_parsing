#!/usr/bin/env python3.8
import argparse


def parse_args():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('files', action='store', nargs='+', help='input files')
    my_parser.add_argument('-w', '--wrap', nargs='?', action='store', type=int, default=54, help='wrap size')
    my_parser.add_argument('-o', '--output', nargs='?', action='store', type=str,
                           help='name of the output file')
    return my_parser.parse_args()


class Parser:

    def parse_and_str_header(header_line):
        splitted = [x.strip() for x in header_line.split(None, 3)][1:] # split by (' ')^+
        return f"ID: {splitted[0]}\nValue: {round(float(splitted[1]),1)}\nDescription: {splitted[2]}"


    def get_length(reader):
        length = 0
        while (line := reader.readline()) != '' and not line.startswith('%'):
            length += len(line.strip())
        return length, line  # returns also the last line read as it may be a header


    def print_file(in_file):
        if len(parsed_args.files) > 1:
            print(in_file)
        with open(in_file, 'r') as reader:
            last_line = reader.readline()
            while not last_line.startswith('%'):  # handling blank lines
                last_line = reader.readline()
            while last_line != '':  #eof
                header = Parser.parse_and_str_header(last_line) # parse header
                length, last_line = Parser.get_length(reader)
                print(f"{header}\nSequence length: {length}\n")


class Writer:

    def get_remainder(sequence, writer):
        for _ in range(len(sequence)//parsed_args.wrap):  # number of full lines
            writer.write(sequence[:parsed_args.wrap]+'\n')   # write full line
            sequence = sequence[parsed_args.wrap:]  # remove the line from the processed sequence
        return sequence


    def write_file(in_file, out_file):
        reader = open(in_file, 'r')
        writer = open(out_file, 'a')
        if len(parsed_args.files) > 1:
            writer.write(in_file + '\n')
        remainder = ""
        line = reader.readline()
        while line != "":  #eof
            if line.startswith('%'):
                writer.write(line)  # print header
            else:
                remainder = Writer.get_remainder(remainder + line.strip(), writer)  # subseq < wrap
            if (line := reader.readline()) == '' or line.startswith('%') and remainder != "":
                writer.write(remainder +'\n')
                remainder = ""
        writer.close()
        reader.close()


if __name__ == '__main__':
    parsed_args = parse_args()
    if parsed_args.output is not None:
        open(parsed_args.output, 'w').close()
        for in_file in parsed_args.files:
            Writer.write_file(in_file, parsed_args.output)
    else:
        for in_file in parsed_args.files:
            Parser.print_file(in_file)
