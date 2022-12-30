import itertools
import time


class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    valves = {}

    for line in data:
        tmp = line.split("; ")
        valve_name = tmp[0].split(" ")[1]
        flow_rate = int(tmp[0].split("=")[1])
        tmp_lead_to = tmp[1].split(" ")
        lead_to = []
        for i in range(4, len(tmp_lead_to)):
            lead_to.append(tmp_lead_to[i].replace(",", ""))

        valve = Valve(valve_name, flow_rate, lead_to)
        valves[valve_name] = valve

    return valves


def get_distance(valves, valve_a, valve_b, steps=0):
    # To get the shortest path from valve A to valve B
    to_go = []
    if steps == 0:
        to_go.append(valve_a)
    else:
        to_go = valve_a

    steps += 1
    to_go_new = []
    for v in to_go:
        for valve_to_go_name in valves[v].lead_to:
            if valve_to_go_name == valve_b:
                return steps
            to_go_new.append(valve_to_go_name)
    distance = get_distance(valves, to_go_new, valve_b, steps)

    return distance



def breadth_first_search(valves, distances, current_valve, available_valves, rest_minutes, path=[], current_pressure=0,
                         total_pressure=0, best_pressure=0):
    for v in available_valves:
        if v not in path and v != "AA":
            exec_time = (distances[current_valve + v] + 1)  # +1 minute to open valve

            if exec_time <= rest_minutes:
                saved_m = rest_minutes
                saved_c = current_pressure
                saved_t = total_pressure

                rest_minutes -= exec_time
                total_pressure += exec_time * current_pressure
                current_pressure += valves[v].flow_rate

                path.append(v)
                tmp_pressure = breadth_first_search(valves, distances, v, available_valves, rest_minutes, path,
                                                    current_pressure, total_pressure, best_pressure)
                if tmp_pressure > best_pressure:
                    best_pressure = tmp_pressure

                path.remove(v)

                current_pressure = saved_c
                total_pressure = saved_t
                rest_minutes = saved_m


    if rest_minutes > 0:
        total_pressure += rest_minutes * current_pressure

    if total_pressure > best_pressure:
        best_pressure = total_pressure

    return best_pressure


def get_valves_with_flow(valves):
    valves_with_flow = []
    for v in valves:
        if valves[v].flow_rate > 0:
            valves_with_flow.append(v)

    return valves_with_flow


def calculate_all_distances(valves):
    result = {}
    for v1 in valves:
        for v2 in valves:
            if v1 != v2 and \
                    valves[v1].flow_rate > 0 and \
                    valves[v2].flow_rate > 0 or \
                    (v1 == 'AA' and valves[v2].flow_rate > 0):
                result[v1 + v2] = get_distance(valves, v1, v2)

    return result


def main():
    start_time = time.time()
    file_name = "Day16-input-p.txt"
    valves = parse_file(file_name)
    part_one = 0
    part_two = 0

    distances = calculate_all_distances(valves)
    valves_with_flow = get_valves_with_flow(valves)
    my_path = valves_with_flow

    print("--- %s seconds ---" % (time.time() - start_time))
    best_res = breadth_first_search(valves, distances, "AA", my_path, 30)
    print(best_res)
    print("--- %s seconds ---" % (time.time() - start_time))


    #return

    all_my_paths = itertools.permutations(valves_with_flow, 7)
    best_res = 0

    # for 7 it will be  =  15!/(15-7)! = 32,432,400
    a = 0
    for my_path in all_my_paths:
        a += 1
        if a % 10000 == 0:
            print("Count: %i           %s seconds" % (a, time.time() - start_time))

        el_path = set(valves_with_flow).difference(set(my_path))
        res_my = breadth_first_search(valves, distances, "AA", my_path, 26)
        res_el = breadth_first_search(valves, distances, "AA", el_path, 26)
        if (res_my + res_el) > best_res:
            print(my_path, el_path, "Res = ", res_my, res_el, res_my + res_el)
            best_res = res_my + res_el

    print("--- %s seconds ---" % (time.time() - start_time))
    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1641
# Part Two: 2261

# Answers P2:
# Part One: 1584
# Part Two: 2052
