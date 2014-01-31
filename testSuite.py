#!/usr/bin/env python
# encoding: utf-8

import json
import csv
import os

def main():
    write_input()
    write_output()
    run_test()

def write_input():
    inputfile = csv.writer(open("test.csv","wb"))
    inputfile.writerow(["test", "test2", "test3"])
    inputfile.writerow(["test", "test2", "test3"])

def write_output():
    with open('out.json', 'w') as outfile:
        json.dump([{'test1':1, 'test2':2}], outfile)

def run_test():
    os.system("python csv2json <test.csv> testout.json")

if __name__ == '__main__':
    main()
