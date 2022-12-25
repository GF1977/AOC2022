import itertools
class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to
        self.is_closed = True
        self.is_visited = False

def walk_the_graf(valves, start_valve, previous_valve=None, timer=0):
    if previous_valve == None:
        previous_valve = start_valve


    timer += 1
    if timer >= 30:
        print("Finish")
        return 0
    for valve_to_go_name in start_valve.lead_to:
        valve_to_go = valves[valve_to_go_name]
        if valve_to_go_name != previous_valve.name:
            print("From %s to %s" %(start_valve.name, valve_to_go_name))
            walk_the_graf(valves, valve_to_go, start_valve,timer)


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
            lead_to.append(tmp_lead_to[i].replace(",",""))

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
    result = get_distance(valves,to_go_new,to_valve_name, steps)
    return result






def unvisit_valves(valves):
    for v in valves:
        valves[v].is_visited = False


def get_total_pressure(valves, best_path):
    minutes = 0
    current_pressure = 0
    total_pressure = 0

    for i in range(0, len(best_path) - 1):
        v_from = best_path[i]
        v_to = best_path[i + 1]
        distance = get_distance(valves, v_from, v_to)
        unvisit_valves(valves)

        minutes += distance + 1  # +1 minute to open a valve
        total_pressure += (distance + 1) * current_pressure
        current_pressure += valves[v_to].flow_rate
        #print(v_from, v_to, "Distance: ", distance, " Current presure: ", current_pressure, "  Total pressure: ",
              #total_pressure)
        if minutes > 30:
            break

    if minutes < 30:
        total_pressure += (30 - minutes) * current_pressure

    return total_pressure

def main():
    file_name = "Day16-Input-p.txt"
    valves = parse_file(file_name)
    part_one = 0
    part_two = 1

    valve = valves["AA"]
    minute = 1
    # while True:
    #     print("== Minute %i ==" % minute)
    #     valve = get_next_valve(valve, valves)
    #     if valve is None:
    #         break
    #     valve.is_closed = False
    #     print("Valve %s is open, releasing %i pressure." %(valve.name, valve.flow_rate))
    #     minute += 1

    #walk_the_graf(valves, valve)
    valves_with_flow = []
    for v in valves:
        if valves[v].flow_rate > 0:
            valves_with_flow.append(v)

    all_pathes = itertools.permutations(valves_with_flow, len(valves_with_flow))

    best_pressure = 0
    for best_path in all_pathes:
        a = list(best_path)
        a.insert(0,'AA')
        best_path = a
        res = get_total_pressure(valves, best_path)
        if res > best_pressure:
            best_pressure = res
            print(best_path, res)





    #best_path = ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    #part_one = get_total_pressure(valves, best_path)

    #distance = get_distance(valves, 'HH', 'EE')
    #print(distance)



    print("----------------------------")
    print("Part One:", best_pressure)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: