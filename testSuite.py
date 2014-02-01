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

itemlist = [EMPTY_ITEM, SINGLE_CHAR_ITEM, MANY_CHAR_ITEM, COVER_QUOTE_ITEM, ELSE_QUOTE_ITEM]

def main():
    create_directories()
    create_test_cases()
    write_output()
    run_test()

def write_input(lines, case_number):
    inputfile = open("TestFiles/TestCase" + case_number,"w")
    for line in lines:
        inputfile.write(line + "\n")

def write_output():
    with open('out.json', 'w') as outfile:
        json.dump([{'test1':1, 'test2':2}], outfile)

def run_test():
    for i in range(20):
        os.system("python csv2json <TestFiles/TestCase" + str(i) + ".csv> ActualOutput/output" + str(i) + ".json")

def create_directories():
    create_directory("TestFiles")
    create_directory("ActualOutput")

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def create_test_cases():
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
    test_case7()
    test_case8()
    test_case9()
    test_case10()
    test_case11()
    test_case12()
    test_case13()
    test_case14()
    test_case15()
    test_case16()
    test_case17()
    test_case18()
    test_case19()
    test_case20()    

##Test Cases
def test_case1():
    lines = insert_csv_lines(line_combo1(), None)
    write_input(lines, "1.csv")

def test_case2():
    lines = insert_csv_lines(line_combo2(), None)
    write_input(lines, "2.csv")

def test_case3():
    lines = insert_csv_lines(line_combo3(), None)
    write_input(lines, "3.csv")

def test_case4():
    lines = insert_csv_lines(line_combo4(), None)
    write_input(lines, "4.csv")
    
def test_case5():
    lines = insert_csv_lines(line_combo5(), None)
    write_input(lines, "5.csv")

def test_case6():
    lines = insert_csv_lines(line_combo6(), None)
    write_input(lines, "6.csv")

def test_case7():
    lines = insert_csv_lines(line_combo7(), None)
    write_input(lines, "7.csv")

def test_case8():
    lines = insert_csv_lines(line_combo8(), None)
    write_input(lines, "8.csv")

def test_case9():
    lines = insert_csv_lines(line_combo2(), line_combo3())
    write_input(lines, "9.csv")

def test_case10():
    lines = insert_csv_lines(line_combo4(), line_combo5())
    write_input(lines, "10.csv")

def test_case11():
    lines = insert_csv_lines(line_combo6(), line_combo7())
    write_input(lines, "11.csv")

def test_case12():
    lines = insert_csv_lines(line_combo7(), line_combo8())
    write_input(lines, "12.csv")

def test_case13():
    lines = insert_csv_lines(line_combo6(), line_combo2())
    write_input(lines, "13.csv")

def test_case14():
    lines = insert_csv_lines(line_combo7(), line_combo3())
    write_input(lines, "14.csv")

def test_case15():
    lines = insert_csv_lines(line_combo8(), line_combo4())
    write_input(lines, "15.csv")

def test_case16():
    lines = insert_csv_lines(line_combo7(), line_combo5())
    write_input(lines, "16.csv")

def test_case17():
    lines = insert_csv_lines(line_combo2(), line_combo6())
    write_input(lines, "17.csv")

def test_case18():
    lines = insert_csv_lines(line_combo3(), line_combo7())
    write_input(lines, "18.csv")

def test_case19():
    lines = insert_csv_lines(line_combo4(), line_combo8())
    write_input(lines, "19.csv")

def test_case20():
    lines = insert_csv_lines(line_combo5(), line_combo7())
    write_input(lines, "20.csv")

def insert_csv_lines(line1, line2):
    lines = []
    if(line1 != None):
        lines.append(format_csv_line(line1)) 
    if(line2 != None):
        lines.append(format_csv_line(line2))
    return lines

def format_csv_line(items):
    return ','.join(items)

##Line combination
def line_combo1():
    return generate_line(None, None)

def line_combo2():
    return generate_line(1, None)

def line_combo3():
    return generate_line(2, None)

def line_combo4():
    return generate_line(3, None)

def line_combo5():
    return generate_line(4, None)

def line_combo6():
    return generate_line(0,1)

def line_combo7():
    return generate_line(2,3)

def line_combo8():
    return generate_line(2,4)

def generate_line(item1, item2):
    line = []
    if(item1 != None):
        line.append(itemlist[item1])
    if(item2 != None):
        line.append(itemlist[item2])
    return line

if __name__ == '__main__':
    main()
