import itertools
import time
import re
import collections


class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to


def parse_file(file_to_process):
    with open(file_to_process, mode="r") as file:
        lines = file.readlines()

    valves = {}

    for line in lines:
        match = re.search(r'Valve\s+(\w+)\s+has flow rate=(\d+);\s+tunnels?\s+leads?\s+to\s+valves?\s+([\w, ]+)', line)
        if match:
            name = match.group(1)
            flow_rate = int(match.group(2))
            lead_to = [v.strip() for v in match.group(3).split(',')]
            valve = Valve(name, flow_rate, lead_to)
            valves[name] = valve

    return valves


def get_distance(valves, valve_a, valve_b):
    # To get the shortest path from valve A to valve B
    visited = set()
    to_go = [(valve_a, 0)]

    while to_go:
        v, steps = to_go.pop(0)
        if v == valve_b:
            return steps

        visited.add(v)
        for next_valve in valves[v].lead_to:
            if next_valve not in visited:
                to_go.append((next_valve, steps + 1))

    return None


def calculate_all_distances(valves):
    result = {}
    for v1 in valves:
        for v2 in valves:
            if v1 != v2 and \
                    (v1 == 'AA' or valves[v1].flow_rate > 0) and valves[v2].flow_rate > 0:
                result[v1 + v2] = get_distance(valves, v1, v2)

    return result


def breadth_first_search(valves, available_valves, distances, rest_minutes):
    current_pressure = 0
    total_pressure = 0
    max_pressure = 0
    max_path = []
    queue = collections.deque([("AA", available_valves, rest_minutes, current_pressure, total_pressure, ["AA"])])

    while queue:
        current_valve, available_valves, rest_minutes, current_pressure, total_pressure, path = queue.popleft()

        for i, v in enumerate(available_valves):
            if v != "AA":
                exec_time = (distances[current_valve + v] + 1)

                if exec_time <= rest_minutes:
                    saved_m = rest_minutes
                    saved_c = current_pressure
                    saved_t = total_pressure

                    rest_minutes -= exec_time
                    total_pressure += exec_time * current_pressure
                    current_pressure += valves[v].flow_rate

                    queue.append((v, list(available_valves)[:i] + list(available_valves)[i + 1:], rest_minutes,
                                  current_pressure, total_pressure, path + [v]))

                    current_pressure = saved_c
                    total_pressure = saved_t
                    rest_minutes = saved_m

        if rest_minutes > 0:
            total_pressure += rest_minutes * current_pressure

        if total_pressure > max_pressure:
            max_pressure = total_pressure
            max_path = path

    return max_pressure, max_path


def get_path_cost(my_path, distances):
    path_cost = 0
    for i in range(0, len(my_path) - 1):
        v1 = my_path[i]
        v2 = my_path[i + 1]
        path_cost += distances[v1 + v2]

    return path_cost


def get_pressure_for_path(valves, path, distances, rest_minutes):
    current_valve = "AA"
    total_pressure = 0
    current_pressure = 0
    for v in path:
        if v == "AA":
            continue
        exec_time = (distances[current_valve + v] + 1)
        if exec_time <= rest_minutes:
            rest_minutes -= exec_time
            total_pressure += exec_time * current_pressure
            current_pressure += valves[v].flow_rate
            current_valve = v
    if rest_minutes > 0:
        total_pressure += rest_minutes * current_pressure

    return total_pressure


def main():
    start_time = time.time()
    file_name = "Day16-Input-p.txt"
    valves = parse_file(file_name)
    distances = calculate_all_distances(valves)

    part_one = 0
    part_two = 0

    valves_with_flow = [key for key, value in valves.items() if value.flow_rate > 0]

    # 30 minutes is hardcoded requirement for this scenario
    best_res, best_path = breadth_first_search(valves, valves_with_flow, distances, rest_minutes=30)
    print(best_res, best_path)
    print("--- %s seconds ---" % (time.time() - start_time))

    cost = get_pressure_for_path(valves, best_path, distances, rest_minutes=30)
    print("Cost for: ", best_path, " = ", cost)


    # Part two

    all_my_paths = itertools.permutations(valves_with_flow, len(valves_with_flow) // 2)
    best_res = 0
    # for 7 it will be  =  15!/(15-7)! = 32,432,400

    for my_path in all_my_paths:

        el_path = list(set(valves_with_flow).difference(set(my_path)))

        # 26 minutes is hardcoded requirement for this scenario
        res_my, best_path_my = breadth_first_search(valves, my_path, distances, rest_minutes=26)

        res_el, best_path_el = breadth_first_search(valves, el_path, distances, rest_minutes=26)
        if (res_my + res_el) > best_res:
            print(best_path_my, best_path_el, "    Res = ", res_my, "+", res_el, "=", res_my + res_el)
            print("--- %s seconds ---" % (time.time() - start_time))
            best_res = res_my + res_el

    print("--- %s seconds ---" % (time.time() - start_time))
    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1641 1.70 seconds
# Part Two: 2261 3.79 seconds

# Answers P2:
# Part One: 1584  1.49 seconds
# Part Two: 2052  5.92 seconds
