#!/usr/bin/env python
# encoding: utf-8

import json
import csv
import os

NUM_TEST_CASES_FOR_CONVERSION = 20

## Presetted Input Constants
EMPTY_ITEM = ''
SINGLE_CHAR_ITEM = 's'
MANY_CHAR_ITEM = 'many char'
COVER_QUOTE_ITEM = '"cover quote"'
ELSE_QUOTE_ITEM = 'else"quote'

itemlist = [EMPTY_ITEM, SINGLE_CHAR_ITEM, MANY_CHAR_ITEM, COVER_QUOTE_ITEM, ELSE_QUOTE_ITEM]

def main():
    create_directories()
    create_test_cases()
    run_test()
    compare_outputs()
    run_filename_tests()

def run_test():
    for i in range(1, NUM_TEST_CASES_FOR_CONVERSION + 1):
        os.system("python csv2json <TestFiles/TestCase" + str(i) + ".csv> TestOutput/Files/output" + str(i) + ".json")

def compare_outputs():
    result = open("TestResult/TestResult.txt","w")
    for i in range(1,NUM_TEST_CASES_FOR_CONVERSION + 1):
        expected_output_file = open("ExpectedOutput/output" + str(i) + ".json", "r")
        actual_output_file = open("TestOutput/Files/output" + str(i) + ".json", "r")
        expected_output = json.load(expected_output_file)
        actual_output = json.load(actual_output_file)
        if(expected_output == actual_output):
            result.write("Test Case" + str(i) + " : " + "Pass\n")
        else:
            result.write("Test Case" + str(i) + " : " + "Fail\n")
    result.close()
    
def create_directories():
    create_directory("TestFiles")
    create_directory("TestOutput/Files")
    create_directory("ExpectedOutput")
    create_directory("TestResult")

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


##Write Testcase CSV Input Files
def write_input(lines, case_number):
    inputfile = open("TestFiles/TestCase" + str(case_number) + ".csv","w")
    for line in lines:
        inputfile.write(line + "\n")

def insert_csv_lines(line1, line2):
    lines = []
    if(line1 != None):
        lines.append(format_csv_line(line1)) 
    if(line2 != None):
        lines.append(format_csv_line(line2))
    return lines
        
def format_csv_line(items):
    return ','.join(items)


##Write Expected JSON File Output
def write_output(lines, case_number):
    outfile = open("ExpectedOutput/output" + str(case_number) + ".json","w")
    for line in lines:
        if(line == None or line == ''):
            outfile.write("[" + line + "]")
        else:
            outfile.write("[{" + line + "}]")
            
def insert_json_lines(line1, line2):
    lines = []
    if(line1 != None):
        if(line2 != None):
            lines.append(format_json_line(line1, line2))
        else:
            lines.append('')
    return lines

def format_json_line(line1, line2):
    lines = []
    for i in range(max(len(line1), len(line2))):
        try:
            string_format = '"' + str(format_json_item(line1[i])) + '": "' + str(format_json_item(line2[i])) + '"'
        except:
            #formatting null fieldname or record
            if(len(line1) == max(len(line1), len(line2))):
                string_format = '"' + str(format_json_item(line1[i])) + '": null'
            else:
               string_format = '"null":"' + str(format_json_item(line2[i])) + '"' 
        lines.append(string_format)
    return ','.join(lines)

def remove_first_cover_quote(item):
    if(item != None and len(item) > 2):
        if(item.startswith('"') and item.endswith('"')):
            return item[1:len(item)-1]
    return item


## Generating Filename Tests
def format_json_item(item):
    item = remove_first_cover_quote(item)
    if(item != None):
        item = item.replace('"', '\\"')
    return item

def run_filename_tests():
    outputs = []
    outputs.append(test_case21())
    outputs.append(test_case22())
    outputs.append(test_case23())
    outputs.append(test_case24())
    write_filename_test_output(outputs)

def write_filename_test_output(outputs):
    result = open("TestResult/FilenameTestResult.txt","w")
    for output in outputs:
        result.write(output)
    
def filename_error_compare(case_number, expected_status, actual_status):
    if(expected_status == actual_status):
        result = "Test Case " + str(case_number) +" (Expected Status=" + str(expected_status) + " , Actual Status:" + str(actual_status) + "): Pass\n"
    else:
        result = "Test Case " + str(case_number) +" (Expected Status=" + str(expected_status) + " , Actual Status:" + str(actual_status) + "): Fail\n"
    return result


## Generating Filename Tests: Existing input file & output file overriding test
def create_csv_for_filename_test():
    result = open("TestFiles/Exist.csv","w")
    result.write('exist\n')
    result.write('file')
    result.close()

def create_json_for_filename_test():
    result = open("ExpectedOutput/Exist.json","wb")
    json.dump([{"initial":"file"}], result)
    expected_result = open("TestOutput/Files/Exist.json","w")
    expected_result.write('[{"exist":"file"}]')
    result.close()
    expected_result.close()

def filename_override_output_compare(case_number):
    result = open("TestResult/TestResult.txt","a")
    expected_output_file = open("ExpectedOutput/Exist.json", "r")
    actual_output_file = open("TestOutput/Files/Exist.json", "r")
    expected_output = json.load(expected_output_file)
    actual_output = json.load(actual_output_file)
    if(expected_output == actual_output):
        result.write("Test Case" + str(case_number) + " : " + "Pass\n")
    else:
        result.write("Test Case" + str(case_number) + " : " + "Fail\n")

def run_filename_test_command(input_name, output_name):
    if(input_name == None):
        command = "python csv2json ExpectedOutput/" + str(output_name) + ".json"
    elif(output_name == None):
        command = "python csv2json <TestFiles/" + str(input_name) + ".csv>"
    else:
        command = "python csv2json <TestFiles/" + str(input_name) + ".csv> ExpectedOutput/Exist.json"
    status = os.system(command)
    return status


##Test Cases
def test_case1():
    create_test_files(line_combo1(), None, 1)

def test_case2():
    create_test_files(line_combo2(), None, 2)

def test_case3():
    create_test_files(line_combo3(), None, 3)

def test_case4():
    create_test_files(line_combo4(), None, 4)
    
def test_case5():
    create_test_files(line_combo5(), None, 5)

def test_case6():
    create_test_files(line_combo6(), None, 6)

def test_case7():
    create_test_files(line_combo7(), None, 7)

def test_case8():
    create_test_files(line_combo8(), None, 8)
    
def test_case9():
    create_test_files(line_combo2(), line_combo3(), 9)

def test_case10():
    create_test_files(line_combo4(), line_combo5(), 10)

def test_case11():
    create_test_files(line_combo6(), line_combo7(), 11)

def test_case12():
    create_test_files(line_combo7(), line_combo8(), 12)

def test_case13():
    create_test_files(line_combo6(), line_combo2(), 13)

def test_case14():
    create_test_files(line_combo7(), line_combo3(), 14)

def test_case15():
    create_test_files(line_combo8(), line_combo4(), 15)

def test_case16():
    create_test_files(line_combo7(), line_combo5(), 16)

def test_case17():
    create_test_files(line_combo2(), line_combo6(), 17)

def test_case18():
    create_test_files(line_combo3(), line_combo7(), 18)

def test_case19():
    create_test_files(line_combo4(), line_combo8(), 19)

def test_case20():
    create_test_files(line_combo5(), line_combo7(), 20)


## Filename Test Cases
def test_case21():
    status = run_filename_test_command("NotExist", "NotExist")
    return filename_error_compare(21, 1, status)

def test_case22():
    status = run_filename_test_command(None, "NotExist")
    return filename_error_compare(22, 1, status)

def test_case23():
    create_csv_for_filename_test()
    create_json_for_filename_test()
    status = run_filename_test_command("Exist", "Exist")    
    filename_override_output_compare(23)
    return filename_error_compare(23, 0, status)

def test_case24():
    create_csv_for_filename_test()
    status = run_filename_test_command("Exist", None)
    return filename_error_compare(24, 1, status)

def create_test_files(line1, line2, case_number):
    lines = insert_csv_lines(line1, line2)
    write_input(lines, case_number)
    json_lines = insert_json_lines(line1, line2)
    write_output(json_lines, case_number)

    
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
