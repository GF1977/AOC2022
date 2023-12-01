import os
import sys
import random
import pandas as pd


shapes = [[(0,0),(0,1),(0,2),(0,3)],0]    
room = []

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data

def main(arguments):
    file_name = "Day 17\Day17-input-d.txt"
    data_input = parse_file(file_name)

    print(data_input)
    stonefall(gas_direction=data_input,rocks_number=10)


def stonefall(gas_direction, rocks_number):
    while (rocks_number>0):
        print(rocks_number)
        rocks_number-=1
    print(shapes[0])
    test_fill_the_room(10)

def test_fill_the_room(rows):
    res = []
    while(rows>0):
        row = ""
        rows-=1
        for i in range(7):
            if (random.randint(0,100)>50):
                c = '#'
            else:
                c = '.'
            row+=c
        res.insert(0, row)
        print(row)

    print('-------')
    for r in res:
        print(r)
    return res

    
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))