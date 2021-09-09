# TBFSBS parser

A parser of the TBFSBS format. For assignment details please click [link](https://gist.github.com/prihoda/d3fef922c29874b700a953a801e82692 "here"). 

## Download:

## Dependencies:
At least python 3.8 required

## Usage:
### Parsing an input file:

```python
./parse.py MySequences1.txt MySequences2.txt > Parsed_seqs.txt
```
### Writer with configurable line wrap:

```python
./parse.py MySequences1.txt MySequences2.txt --output MyOutput.txt --wrap 80
```

You may also use shortened flags:
```python
./parse.py MySequences1.txt MySequences2.txt -o MyOutput.txt -w 80
```
