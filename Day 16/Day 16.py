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


def get_total_pressure(valves, distances, best_path, minutes_limit=30):
    minutes = 0
    current_pressure = 0
    total_pressure = 0

    for i in range(0, len(best_path) - 1):
        v_from = best_path[i]
        v_to = best_path[i + 1]
        if (v_from+v_to) not in distances:
            continue

        distance = distances[v_from+v_to]
        #if distance > 6:
        #    break

        if minutes + distance + 1 > minutes_limit:
            break

        minutes += distance + 1  # +1 minute to open a valve

        total_pressure += (distance + 1) * current_pressure
        current_pressure += valves[v_to].flow_rate

        #print(v_from, v_to, "Distance: ", distance, " Current presure: ", current_pressure, "  Total pressure: ", total_pressure)

    if minutes < minutes_limit:
        total_pressure += (minutes_limit - minutes) * current_pressure

    return total_pressure


def get_the_maximum_pressure(valves, distances, path_beginning=None, path_len=None, flow_rate_to_ignore=0):
    processed_path = []
    start_time = time.time()
    valves_with_flow_to_sort = []
    for v in valves:
        if valves[v].flow_rate > flow_rate_to_ignore:
            valves_with_flow_to_sort.append([distances["AA"+v], v])

    valves_with_flow_to_sort.sort(reverse=False)

    valves_with_flow = []
    for v in valves_with_flow_to_sort:
        valves_with_flow.append(v[1])

    #valves_with_flow.remove("IZ")

    best_pressure = 0


    if path_beginning is not None:
        valves_with_flow = set(valves_with_flow).difference(set(path_beginning))

    if path_len is None or len(valves_with_flow) < 6:
        path_len = len(valves_with_flow)

    all_paths = itertools.permutations(valves_with_flow, path_len)



    for best_path in all_paths:
        a = list(best_path)
        #a.insert(0, 'IZ')
        if path_beginning is not None:
            a = path_beginning + a
        if a[0] != 'AA':
            a.insert(0, 'AA')
        best_path = a

        res = get_total_pressure(valves, distances, best_path)
        if res > best_pressure:
            best_pressure = res
            #print(best_path,  res)
            #print("--- %s seconds ---" % (time.time() - start_time))
        processed_path.append([res, best_path])
    return best_pressure, processed_path

def get_the_maximum_pressure2(valves, distances, my_paths=None, flow_rate_to_ignore=0):
    start_time = time.time()
    valves_with_flow = []
    for v in valves:
        if valves[v].flow_rate > flow_rate_to_ignore:
            valves_with_flow.append(v)

    best_pressure = 0

    path_len = len(valves_with_flow)
    if my_paths is None:
        my_paths = itertools.permutations(valves_with_flow, path_len)

    half_len = path_len // 2
    if half_len < 3:
        half_len = 6

    for my_path in my_paths:
        a = list(my_path)[:half_len]
        a.insert(0, 'AA')
        el_paths = itertools.permutations(list(my_path)[half_len:], half_len)
        my_path = a

        res_my = get_total_pressure(valves, distances, my_path, minutes_limit=26)

        for el_path in el_paths:
            a = list(el_path)
            a.insert(0, 'AA')
            el_path = a

            res_el = get_total_pressure(valves, distances, el_path, minutes_limit=26)
            res = res_my + res_el
            if res > best_pressure:
                best_pressure = res
                print(my_path, el_path,  res)
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
    file_name = "Day16-Input-p2.txt"
    valves = parse_file(file_name)
    part_one = 0
    part_two = 0

    distances = calculate_all_distances(valves)

    _, processed_paths = get_the_maximum_pressure(valves, distances, path_len=4)
    processed_paths.sort(reverse=True)
    processed_paths = processed_paths[:100]

    for p_p in processed_paths:
        pressure, processed_paths = get_the_maximum_pressure(valves, distances, path_beginning=p_p[1], path_len=4)
        if pressure > part_one:
            print(pressure)
            print("--- %s seconds ---" % (time.time() - start_time))
            part_one = pressure



    #part_two = get_the_maximum_pressure2(valves, distances, flow_rate_to_ignore=4)

    print("--- %s seconds ---" % ( time.time() - start_time))
    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1641
# Part Two:

# Answers P2:
# Part One: 1584
# Part Two:
