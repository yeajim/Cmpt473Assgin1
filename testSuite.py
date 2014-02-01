#!/usr/bin/env python
# encoding: utf-8

import json
import csv
import os

## presetted input constants
EMPTY_ITEM = ''
SINGLE_CHAR_ITEM = 's'
MANY_CHAR_ITEM = 'many char'
COVER_QUOTE_ITEM = '"cover quote"'
ELSE_QUOTE_ITEM = 'else"quote'

def main():
    write_input()
    write_output()
    run_test()

def write_input():
    inputfile = csv.writer(open("test.csv","wb"), quotechar=None)
    inputfile.writerow([COVER_QUOTE_ITEM])
    inputfile.writerow(["test", "test2", "test3"])

def write_output():
    with open('out.json', 'w') as outfile:
        json.dump([{'test1':1, 'test2':2}], outfile)

def run_test():
    os.system("python csv2json <test.csv> testout.json")

##Item combination
def line_combo1():
    line = []
    return line

def line_combo2():
    return generate_line(SINGLE_CHAR_ITEM)

def line_combo3():
    return generate_line(MANY_CHAR_ITEM)

def line_combo4():
    return generate_line(COVER_QUOTE_ITEM)

def line_combo5():
    return generate_line(ELSE_QUOTE_ITEM)

def line_combo6():
    return generate_line_with_2items(EMPTY_ITEM, SINGLE_CHAR_ITEM)

def line_combo7():
    return generate_line_with_2items(MANY_CHAR_ITEM, COVER_QUOTE_ITEM)

def line_combo8():
    return generate_line_with_2items(MANY_CHAR_ITEM, ELSE_QUOTE_ITEM)

def generate_line(item):
    line = []
    line.append(item)
    return line

def generate_line_with_2items(item1, item2):
    line = []
    line.append(item1)
    line.append(item2)
    return line

if __name__ == '__main__':
    main()
