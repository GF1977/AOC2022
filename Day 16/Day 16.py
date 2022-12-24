class Valve:
    def __init__(self, name, flow_rate, lead_to):
        self.name = name
        self.flow_rate = flow_rate
        self.lead_to = lead_to
        self.is_closed = True

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


def main():
    file_name = "Day16-Input-d.txt"
    valves = parse_file(file_name)
    part_one = 0
    part_two = 1

    valve = valves["AA"]
    minute = 1
    while True:
        print("== Minute %i ==" % minute)
        valve = get_next_valve(valve, valves)
        if valve is None:
            break
        valve.is_closed = False
        print("Valve %s is open, releasing %i pressure." %(valve.name, valve.flow_rate))
        minute += 1



    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: