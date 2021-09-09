# TBFSBS parser

A parser of the TBFSBS format. For assignment details please click [here](https://gist.github.com/prihoda/d3fef922c29874b700a953a801e82692). 

## Download:
```bash
git@github.com:lavakin/TBFSBS_parsing.git
```
## Dependencies:
At least python 3.8 required

## Usage:
### Parsing an input file:

```bash
./parse.py MySequences1.txt MySequences2.txt > Parsed_seqs.txt
```
### Writer with configurable line wrap:

```bash
./parse.py MySequences1.txt MySequences2.txt --output MyOutput.txt --wrap 80
```

You may also use shortened flags:
```bash
./parse.py MySequences1.txt MySequences2.txt -o MyOutput.txt -w 80
```
