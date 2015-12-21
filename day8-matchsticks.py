#!/usr/bin/env python3

import re
FILE='day8-input.txt'

with open(FILE, 'r') as puzzle_input:
    code_length = 0
    string_length = 0
    for line in puzzle_input:
        clean_line = line.strip()
        code_length += len(clean_line)
        string_line = clean_line.strip('"')
        string_line = re.sub(r'\\x[0-9a-f]{2}', 'r', string_line)
        string_line = re.sub(r'\\[\\"]', 'r', string_line)
        string_length += len(string_line)
    print(code_length - string_length)

with open(FILE, 'r') as puzzle_input:
    code_length = 0
    string_length = 0
    for line in puzzle_input:
        clean_line = line.strip()
        code_length += len(clean_line)
        string_line = re.sub(r'\\', r'\\\\', clean_line)
        string_line = re.sub(r'"', '\\"', string_line)
        string_line = '"{}"'.format(string_line)
        string_length += len(string_line)
    print(string_length - code_length)
