from functools import lru_cache

TIME_LIMIT = 30

class Valve:

    def __init__(self, name, pressure):
        
        self.name = name
        self.links: list[Link] = []
        self.pressure = pressure

    def __str__(self):
        tmp = f"{self.name}"
        for link in self.links:
            tmp = f"{tmp}\n->  {link.length} {link.b.name}"

        return tmp

class Link:

    def __init__(self, a:Valve, b:Valve, length:int):

        self.a = a
        self.b = b 
        self.length = length

def decode_opened_valves(opened_valves: str):
    opened_valves = opened_valves.split(",")
    if opened_valves[0] == "":
        return []
    return opened_valves

def encode_opened_valves(opened_valves: list[str]):
    values = sorted(opened_valves)
    return ",".join(values)

def optimize_valves(valves):

    def purge_valve(v: Valve):

        for l in v.links:
            for k in v.links:

                if l.b != k.b:
                    l.b.links.append(Link(l.b, k.b, l.length + k.length))

        for l in v.links:
            for k in l.b.links:
                if k.b == v:
                    l.b.links.remove(k)
        v.links = []

    for v_name in valves:
        v:Valve = valves[v_name]

        # Purge valve if pressure is 0.
        if v.pressure == 0:
            purge_valve(v)

def get_openable_valves_count(valves):

    openable = []

    to_visit = ["AA"]
    visited = ["AA"]

    while to_visit != []:

        valve = valves[to_visit.pop(0)]
        if valve.pressure > 0 and valve not in openable:
            openable.append(valve.name)

        for link in valve.links:
            if link.b.name not in visited:
                to_visit.append(link.b.name)
                visited.append(link.b.name)

    return len(openable)

@lru_cache(maxsize=None)
def go_explore(valve: str, valve_elephant: str, remaining_turns: int, opened_valves: str, score: int):

    opened_valves_list = decode_opened_valves(opened_valves=opened_valves)

    if remaining_turns == 0:
        return score

    remaining_turns -= 1
    # print(f"[{valve}, {valve_elephant}], {remaining_turns}, {opened_valves}, {score}")

    if len(opened_valves_list) == max_open:
        t_score = score
        for v in opened_valves_list:
            t_score += valves[v].pressure * remaining_turns
        return t_score

    # Add score from opened valves.
    for v in opened_valves_list:
        score += valves[v].pressure

    best_score = 0

    person_options = []
    elephant_options = []

    if valve not in opened_valves_list and valves[valve].pressure > 0:
        person_options.append("open")

    if valve_elephant not in opened_valves_list and valves[valve_elephant].pressure > 0:
        elephant_options.append("open")


    for l in valves[valve].links:
        person_options.append(l.b.name)

    for l in valves[valve_elephant].links:
        elephant_options.append(l.b.name)

    best_score = 0
    for p_o in person_options:
        for e_o in elephant_options:

            if p_o == "open" and e_o == "open" and valve_elephant == valve:
                continue
            # if p_o != "open" and p_o == e_o:
            #     continue

            a = [i for i in opened_valves_list]

            if p_o == "open":
                a.append(valve)
                p_o = valve
            if e_o == "open" and valve_elephant not in a:
                a.append(valve_elephant)
                e_o = valve_elephant
            elif e_o == "open":
                e_o = valve_elephant

            tmp = go_explore(valve=p_o, valve_elephant=e_o, remaining_turns=remaining_turns, opened_valves=encode_opened_valves(a), score=score)
            if tmp > best_score:
                best_score = tmp

    return best_score


# Load the file
# input_file = open('day16/input_1.txt', 'r')
input_file = open('day16/input_short.txt', 'r')
lines = input_file.readlines()

valves = {}
tunnels_tmp = []
flow_A = 0

for line in lines:

    line = line.strip()
    parts = line.split()

    name = parts[1]
    flow = int(parts[4][5:-1])
    tunnels = list(map(lambda n: n.split(",")[0], parts[9:]))

    for tunnel in tunnels:
        tunnels_tmp.append({"a": name, "b": tunnel})

    if name == "AA":
        flow_A = flow
        flow = 1
    
    valve = Valve(name=name, pressure=flow)
    valves[name] = valve

for tunnel in tunnels_tmp:
    vlv = valves[tunnel["a"]]
    vlv.links.append(Link(a=vlv, b=valves[tunnel["b"]], length=1))
# optimize_valves(valves=valves)

valves["AA"].pressure = flow_A

max_open = get_openable_valves_count(valves=valves)


score = go_explore(valve="AA", valve_elephant="AA", remaining_turns=11, opened_valves="", score=0)
print(score)

#idx    rnd     total   measured
# 1     0       0       0
# 2     0       0       0
# 3     20      20      0
# 4     41      61      33
# 5     41      102     66
# 6     41      143     104
# 7     41      184
# 8     76      260
# 9     76      346
# 10    78      424
# 11    78      495     490
# 12    81      573     569
# 13    81      654
# 14     .
#
# 20    81      1221    1201
#
#