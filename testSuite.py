#!/usr/bin/env python
# encoding: utf-8

import json
import csv

def main():
    write_input()
    write_output()

def write_input():
    inputfile = csv.writer(open("test.csv","wb"))
    inputfile.writerow(["test", "test2", "test3"])

def write_output():
    with open('out.json', 'w') as outfile:
        json.dump([{'test1':1, 'test2':2}], outfile)

if __name__ == '__main__':
    main()
