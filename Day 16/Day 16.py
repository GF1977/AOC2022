import itertools
import time

distances = {}

class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to
        self.is_closed = True
        self.is_visited = False


def walk_the_graf(valves, start_valve):
    max_flow = -1
    best_v = None
    for v in start_valve.lead_to:
        v_to_go = valves[v]
        if v_to_go.flow_rate > max_flow and v_to_go.is_visited == False:
            max_flow = v_to_go.flow_rate
            best_v = v_to_go

    if best_v is None:
        return

    best_v.is_visited = True
    print(best_v.name, best_v.flow_rate)
    walk_the_graf(valves, best_v)


def get_next_valve(valve_from, valves):
    #  returns obj valve which is connected to param:valve_from with the biggest flow rate
    max_flow_rate = 0
    valve = None
    for direction in valve_from.lead_to:
        candidate = valves[direction]
        if candidate.is_closed and candidate.flow_rate > max_flow_rate:
            max_flow_rate = candidate.flow_rate
            valve = candidate

    return valve


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
        valves[v].is_visited = True
        for valve_to_go_name in valves[v].lead_to:
            if valve_to_go_name == to_valve_name:
                return steps
            if not valves[valve_to_go_name].is_visited:
                to_go_new.append(valve_to_go_name)
    result = get_distance(valves, to_go_new, to_valve_name, steps)
    return result


def unvisit_valves(valves):
    for v in valves:
        valves[v].is_visited = False


def get_total_pressure(valves, best_path):
    minutes = 0
    current_pressure = 0
    total_pressure = 0
    opened_valves = []

    for i in range(0, len(best_path) - 1):
        v_from = best_path[i]
        v_to = best_path[i + 1]
        distance = get_distance(valves, v_from, v_to)
        unvisit_valves(valves)
        if distance > 4:
            return 0, []

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


def main():
    start_time = time.time()
    file_name = "Day16-Input-p.txt"
    valves = parse_file(file_name)
    part_one = 0
    part_two = 1


    # for v1 in valves:
    #     for v2 in valves:
    #         if v1 != v2 and valves[v1].flow_rate > 0 and valves[v2].flow_rate > 0:
    #             key = v1 + v2
    #             distances[key] = get_distance(valves, v1, v2)

    valves_with_flow = []
    for v in valves:
        if valves[v].flow_rate > 4:
            #print(v, valves[v].flow_rate)
            valves_with_flow.append(v)

    best_pressure = 0

    # valves_with_flow.remove('YL')
    #valves_with_flow.remove('FF')
    #valves_with_flow.remove('UZ')
    #valves_with_flow.remove('TU')
    #valves_with_flow.remove('QZ')
    valves_with_flow.remove('CU')
    valves_with_flow.remove('IZ')

    print(len(valves_with_flow))
    all_paths = itertools.permutations(valves_with_flow, 8)

    counter = 0
    for best_path in all_paths:
        a = list(best_path)
        # a.insert(0, 'YL')
        #a.insert(0, 'FF')
        #a.insert(0, 'UZ')
        #a.insert(0, 'TU')
        #a.insert(0, 'QZ')
        a.insert(0, 'CU')
        a.insert(0, 'IZ')


        a.insert(0, 'AA')
        best_path = a
        o_v = []
        res = 0

        res, o_v = get_total_pressure(valves, best_path)
        #print(best_path, res)
        if res > best_pressure:
            best_pressure = res
            print(best_path, o_v, res)
            print(" Processed: %i --- %s seconds ---" % (counter, time.time() - start_time))
        counter+=1
    #walk_the_graf(valves, valves['AA'])

    #best_path = ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    best_path = ['AA', 'IZ', 'CU', 'QZ', 'TU', 'UZ', 'FF', 'GG', 'ZL']
                # ['AA', 'IZ', 'CU', 'QZ', 'TU', 'UZ', 'FF', 'GG', 'ZL'] Winner!
                #['AA', 'TU', 'QZ', 'CU', 'IZ', 'PA', 'XF', 'YL', 'JH', 'OI', 'GG', 'ZL', 'UZ', 'TR', 'SZ', 'FF']
    part_two = get_total_pressure(valves, best_path)

    #distance = get_distance(valves, 'HH', 'EE')
    #print(distance)

    print("----------------------------")
    print("Part One:", best_pressure)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1641
# Part Two:
