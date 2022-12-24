import copy
import ctypes.wintypes
from multiprocessing import Process, Value
import time


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    coordinates = []
    for line in data:
        tmp = line.split(": ")
        s_x = int(tmp[0].split(", ")[0].split("=")[1])
        s_y = int(tmp[0].split(", ")[1].split("=")[1])
        b_x = int(tmp[1].split(", ")[0].split("=")[1])
        b_y = int(tmp[1].split(", ")[1].split("=")[1])
        coordinates.append([XY(s_x, s_y), XY(b_x, b_y)])

    return coordinates


def get_start_end(crd_sensor, crd_beacon, r_y):
    # for a given coordinates return the X coordinates (start, end) on a line where Y = r_y
    # to simplify the math, lets made calculation moving Sensor to [0,0] and adjust beacon and r_y accordingly
    b_x = abs(crd_beacon.x - crd_sensor.x)
    b_y = abs(crd_beacon.y - crd_sensor.y)
    r_y = abs(r_y - crd_sensor.y)

    end_r_x = b_x + (b_y - r_y)
    start_r_x = -end_r_x

    # if r_y doesn't cross the sensor coverage, there is no result
    if end_r_x < start_r_x:
        return None

    # it is important to preserve the initial X,Y of a sensor to locate them on the coverage map correctly
    return [start_r_x + crd_sensor.x, end_r_x + crd_sensor.x]


def is_overlapped(a, b):
    # checking if a range A is overlapped or connected with range B

    # for cases where the coordinates are connected [1, 100] & [101,299] or [-5,-2][-1,22]
    if abs(a[0] - b[1]) == 1 or abs(a[1] - b[0]) == 1:
        return True

    if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
        return True


def get_ranges(data_input, y_coordinate):
    # return the set of ranges which don't overlap or connect each other
    # converting the raw coordinates into a set of coverage ranges for a given Y coordinate
    ranges = []
    result = []
    for crd in data_input:
        new_range = get_start_end(crd_sensor=crd[0], crd_beacon=crd[1], r_y=y_coordinate)
        if new_range is not None:
            ranges.append(new_range)

    ranges.sort()

    range_a = ranges[0]

    for i in range(0, len(ranges)):
        range_b = copy.copy(ranges[i])
        if is_overlapped(range_a, range_b):
            range_b[0] = range_a[0]
            range_b[1] = max(range_a[1], range_b[1])

        else:
            result.append(range_a)
        range_a = range_b

    result.append(range_a)
    return result


def get_whole_range(coverage_line):
    # return the distance between the most left and most right ranges
    # [1,100] [200,300] [300,304]  = > the range is  [1,304], the distance is 304 - 1 = 303
    start = coverage_line[0][0]
    end = coverage_line[0][1]

    for a in coverage_line:
        if a[1] > end:
            end = a[1]

    return end - start


def get_coverage_distance(ranges):
    # return the total distance of the all ranges
    res = 0
    for a_range in ranges:
        res += abs(a_range[0] - a_range[1])

    return res


def scan_the_range(data_input, start, end, result):
    for line_number in range(start, end):
        res = get_ranges(data_input, line_number)
        # condition of success is - there are only two ranges with single gap
        # Example:  [0,1000] [1002,2222]  => Gap is [1001,1001]
        if len(res) == 2 and abs(res[0][1] - res[1][0]) == 2:
            result.value = (res[0][1] + 1) * 4000000 + line_number
            break


def main():
    file_name = "Day15-Input-p.txt"
    data_input = parse_file(file_name)
    line_number = 2000000

    res = get_ranges(data_input, line_number)
    part_one = get_coverage_distance(res)

    part_two = 0

    lst_processes = []
    start_time = time.time()
    result = Value(ctypes.c_int64, 0)
    for i in range(0, 20):
        start = i * 200000
        end = (i + 1) * 200000
        obj_process = Process(target=scan_the_range, args=(data_input, start, end, result,))
        lst_processes.append(obj_process)
        obj_process.start()

    for obj_process in lst_processes:
        obj_process.join()
        if result.value > 0:
            part_two = result.value
            break

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)
    print("--- Execution time: %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

# Answers:
# Part One: 5144286
# Part Two: 10229191267339
