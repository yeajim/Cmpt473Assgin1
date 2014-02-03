#!/usr/bin/env python
# encoding: utf-8

## Cmpt 473 Assignment 1 Test Suite
## Yeaji Moon - 301097918
## Rei Li

import json
import csv
import os

## Presetted Input Constants
EMPTY_ITEM = ''
SINGLE_CHAR_ITEM = 's'
MANY_CHAR_ITEM = 'many char'
COVER_QUOTE_ITEM = '"cover quote"'
ELSE_QUOTE_ITEM = 'else"quote'
NUM_TEST_CASES_FOR_CONVERSION = 48

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
    test_case21()
    test_case22()
    test_case23()
    test_case24()
    test_case25()
    test_case26()
    test_case27()
    test_case28()
    test_case29()
    test_case30()
    test_case31()
    test_case32()
    test_case33()
    test_case34()
    test_case35()
    test_case36()
    test_case37()
    test_case38()
    test_case39()
    test_case40()
    test_case41()
    test_case42()
    test_case43()
    test_case44()
    test_case45()
    test_case46()
    test_case47()
    test_case48()


##Write Testcase CSV Input Files
def write_input(lines, case_number):
    inputfile = open("TestFiles/TestCase" + str(case_number) + ".csv","w")
    for line in lines:
        inputfile.write(line + "\n")

def insert_csv_lines(line1, line2, line3=None):
    lines = []
    if(line1 != None):
        lines.append(format_csv_line(line1)) 
    if(line2 != None):
        lines.append(format_csv_line(line2))
    if(line3 != None):
        lines.append(format_csv_line(line3))
    return lines
        
def format_csv_line(items):
    return ','.join(items)


##Write Expected JSON File Output
def write_output(lines, case_number):
    outfile = open("ExpectedOutput/output" + str(case_number) + ".json","w")
    result = ','.join(lines)
    result = '[' + result + ']'
    outfile.write(result)
            
def insert_json_lines(line1, line2, line3=None):
    lines = []
    max_length = calculate_max_length(line1, line2, line3)
    if(line1 != None):
        if(line2 != None):
            lines.append(format_json_line(line1, line2, max_length))
        if(line3 != None):
            lines.append(format_json_line(line1, line3, max_length))
    return lines

def calculate_max_length(line1, line2, line3):
    if(line2 == None):
        if(line3 == None):
            return len(line1)
        else:
            return max(len(line1), len(line3))
    elif(line3 == None):
        return max(len(line1), len(line2))
    else:
        return max(len(line1), len(line2), len(line3))

def format_json_line(line1, line2, max_length):
    lines = []
    for i in range(max_length):
        try:
            string_format = '"' + str(format_json_item(line1[i])) + '": "' + str(format_json_item(line2[i])) + '"'
        except:
            #formatting null fieldname or record
            if(len(line1) == max_length):
                string_format = '"' + str(format_json_item(line1[i])) + '": null'
            else:
               string_format = '"null":"' + str(format_json_item(line2[i])) + '"' 
        lines.append(string_format)
    result = ','.join(lines)
    if(result != None and result != '' and result != '\n'):
        result = '{' + str(result) + '}'
    return result

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
    outputs.append(test_case49())
    outputs.append(test_case50())
    outputs.append(test_case51())
    outputs.append(test_case52())
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
    create_test_files(1, line_combo1(), None)

def test_case2():
    create_test_files(2, line_combo2(), None)

def test_case3():
    create_test_files(3, line_combo3(), None)

def test_case4():
    create_test_files(4, line_combo4(), None)
    
def test_case5():
    create_test_files(5, line_combo5(), None)

def test_case6():
    create_test_files(6, line_combo6(), None)

def test_case7():
    create_test_files(7, line_combo7(), None)

def test_case8():
    create_test_files(8, line_combo8(), None)

def test_case9():
    create_test_files(9, line_combo1(), line_combo1())

def test_case10():
    create_test_files(10, line_combo2(), line_combo2(), line_combo4())

def test_case11():
    create_test_files(11, line_combo2(), line_combo3(), line_combo5())

def test_case12():
    create_test_files(12, line_combo3(), line_combo2(), line_combo4())

def test_case13():
    create_test_files(13, line_combo3(), line_combo3(), line_combo5())

def test_case14():
    create_test_files(14, line_combo4(), line_combo2(), line_combo4())

def test_case15():
    create_test_files(15, line_combo4(), line_combo3(), line_combo5())

def test_case16():
    create_test_files(16, line_combo5(), line_combo2(), line_combo4())

def test_case17():
    create_test_files(17, line_combo5(), line_combo3(), line_combo5())

def test_case18():
    create_test_files(18, line_combo6(), line_combo6(), line_combo7())

def test_case19():
    create_test_files(19, line_combo6(), line_combo7(), line_combo8())

def test_case20():
    create_test_files(20, line_combo7(), line_combo6(), line_combo7())

def test_case21():
    create_test_files(21, line_combo7(), line_combo7(), line_combo8())

def test_case22():
    create_test_files(22, line_combo8(), line_combo6(), line_combo7())

def test_case23():
    create_test_files(23, line_combo8(), line_combo7(), line_combo8())

def test_case24():
    create_test_files(24, line_combo1(), line_combo2(), line_combo4())

def test_case25():
    create_test_files(25, line_combo1(), line_combo3(), line_combo5())

def test_case26():
    create_test_files(26, line_combo1(), line_combo6(), line_combo7())

def test_case27():
    create_test_files(27, line_combo1(), line_combo7(), line_combo8())

def test_case28():
    create_test_files(28, line_combo2(), line_combo6(), line_combo7())

def test_case29():
    create_test_files(29, line_combo2(), line_combo7(), line_combo8())

def test_case30():
    create_test_files(30, line_combo3(), line_combo6(), line_combo7())

def test_case31():
    create_test_files(31, line_combo3(), line_combo7(), line_combo8())

def test_case32():
    create_test_files(32, line_combo4(), line_combo6(), line_combo7())

def test_case33():
    create_test_files(33, line_combo4(), line_combo7(), line_combo8())

def test_case34():
    create_test_files(34, line_combo5(), line_combo6(), line_combo7())

def test_case35():
    create_test_files(35, line_combo5(), line_combo7(), line_combo8())

def test_case36():
    create_test_files(36, line_combo2(), line_combo1())

def test_case37():
    create_test_files(37, line_combo3(), line_combo1())

def test_case38():
    create_test_files(38, line_combo4(), line_combo1())

def test_case39():
    create_test_files(39, line_combo5(), line_combo1())

def test_case40():
    create_test_files(40, line_combo6(), line_combo1(), line_combo2())

def test_case41():
    create_test_files(41, line_combo6(), line_combo3(), line_combo4())

def test_case42():
    create_test_files(42, line_combo6(), line_combo5(), line_combo1())

def test_case43():
    create_test_files(43, line_combo7(), line_combo1(), line_combo2())

def test_case44():
    create_test_files(44, line_combo7(), line_combo3(), line_combo4())

def test_case45():
    create_test_files(45, line_combo7(), line_combo5(), line_combo1())

def test_case46():
    create_test_files(46, line_combo8(), line_combo1(), line_combo2())

def test_case47():
    create_test_files(47, line_combo8(), line_combo3(), line_combo4())

def test_case48():
    create_test_files(48, line_combo8(), line_combo5(), line_combo1())

def create_test_files(case_number, line1, line2, line3=None):
    lines = insert_csv_lines(line1, line2, line3)
    write_input(lines, case_number)
    json_lines = insert_json_lines(line1, line2, line3)
    write_output(json_lines, case_number)


## Filename Test Cases
def test_case49():
    status = run_filename_test_command("NotExist", "NotExist")
    return filename_error_compare(49, 1, status)

def test_case50():
    status = run_filename_test_command(None, "NotExist")
    return filename_error_compare(50, 1, status)

def test_case51():
    create_csv_for_filename_test()
    create_json_for_filename_test()
    status = run_filename_test_command("Exist", "Exist")    
    filename_override_output_compare(51)
    return filename_error_compare(51, 0, status)

def test_case52():
    create_csv_for_filename_test()
    status = run_filename_test_command("Exist", None)
    return filename_error_compare(52, 1, status)

    
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

def generate_line(item1, item2, item3=None):
    line = []
    if(item1 != None):
        line.append(itemlist[item1])
    if(item2 != None):
        line.append(itemlist[item2])
    if(item3 != None):
        line.append(itemlist[item3])
    return line

if __name__ == '__main__':
    main()
