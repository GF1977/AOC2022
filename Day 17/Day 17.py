import os
import sys

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data

def main(arguments):
    file_name = "Day 17\Day17-input-p.txt"
    data_input = parse_file(file_name)
    

    print(arguments)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))