import itertools
import time


class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to
        self.is_closed = True


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


def get_distance(valves, from_valve_name, to_valve_name, steps=0):
    to_go = []
    if steps == 0:
        to_go.append(from_valve_name)
    else:
        to_go = from_valve_name

    steps += 1
    to_go_new = []
    for v in to_go:
        for valve_to_go_name in valves[v].lead_to:
            if valve_to_go_name == to_valve_name:
                return steps
            if valves[valve_to_go_name].is_closed:
                to_go_new.append(valve_to_go_name)
    result = get_distance(valves, to_go_new, to_valve_name, steps)
    return result


def unvisit_valves(valves):
    for v in valves:
        valves[v].is_closed = True


def get_total_pressure(valves, distances, best_path):
    minutes = 0
    current_pressure = 0
    total_pressure = 0
    opened_valves = []

    for i in range(0, len(best_path) - 1):
        v_from = best_path[i]
        v_to = best_path[i + 1]
        distance = distances[v_from+v_to]

        # if distance > 10:
        #     break

        if minutes + distance + 1 > 30:
            break

        minutes += distance + 1  # +1 minute to open a valve
        opened_valves.append(v_to)

        total_pressure += (distance + 1) * current_pressure
        current_pressure += valves[v_to].flow_rate

        #print(v_from, v_to, "Distance: ", distance, " Current presure: ", current_pressure, "  Total pressure: ", total_pressure)

    if minutes < 30:
        total_pressure += (30 - minutes) * current_pressure

    #print("Total pressure: ", total_pressure)
    return total_pressure, opened_valves


def get_the_maximum_pressure(valves, distances,  flow_rate_to_ignore=0, path_len=6):
    start_time = time.time()
    valves_with_flow = []
    for v in valves:
        if valves[v].flow_rate > flow_rate_to_ignore:
            valves_with_flow.append(v)

    best_pressure = 0

    all_paths = itertools.permutations(valves_with_flow, path_len)

    for best_path in all_paths:
        a = list(best_path)
        a.insert(0, 'AA')
        best_path = a

        res, o_v = get_total_pressure(valves, distances, best_path)
        if res > best_pressure:
            best_pressure = res
            print(best_path, o_v, res)
            print("--- %s seconds ---" % (time.time() - start_time))
    return best_pressure


def calculate_all_distances(valves):
    result = {}
    for v1 in valves:
        for v2 in valves:
            if v1 != v2 and valves[v1].flow_rate > 0 and valves[v2].flow_rate > 0 or v1 == 'AA':
                result[v1 + v2] = get_distance(valves, v1, v2)
                unvisit_valves(valves)
    return result

def main():
    start_time = time.time()
    file_name = "Day16-Input-d.txt"
    valves = parse_file(file_name)

    distances = calculate_all_distances(valves)
    part_one = get_the_maximum_pressure(valves, distances)

    part_two = 1

    print("--- %s seconds ---" % ( time.time() - start_time))
    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1641
# Part Two:
