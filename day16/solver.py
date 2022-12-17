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

@lru_cache(maxsize=1000000000)
def go_explore(valve: str, remaining_turns: int, opened_valves: str, score: int, jump_length: int):

    opened_valves_list = decode_opened_valves(opened_valves=opened_valves)

    # Add score from opened valves.
    for v in opened_valves_list:
        score += valves[v].pressure * jump_length

    remaining_turns -= jump_length
    # print(f"{valve}, {remaining_turns}, {opened_valves}, {score}, {jump_length}")

    if remaining_turns == 0:
        return score

    best_score = 0
    did_continue = False

    if valve not in opened_valves_list and valves[valve].pressure > 0:
        # print(f"opening {valve}")

        tmp_score = score
        for v in opened_valves_list:
            tmp_score += valves[v].pressure

        # opened_valves_list.append(valve)
        a = [i for i in opened_valves_list]
        a.append(valve)

        best_score = go_explore(valve=valve, remaining_turns=remaining_turns - 1, opened_valves=encode_opened_valves(a), score=tmp_score, jump_length=0)
        did_continue = True
    
    # Go to other valves.

    for l in valves[valve].links:

        if l.length > remaining_turns:
            continue

        tmp = go_explore(valve=l.b.name, remaining_turns=remaining_turns, opened_valves=encode_opened_valves(opened_valves_list), score=score, jump_length=l.length)
        did_continue = True
        if tmp > best_score:
            best_score = tmp

    if not did_continue:
        for v in opened_valves_list:
            score += valves[v].pressure * remaining_turns
        return score

    return best_score


# Load the file
input_file = open('day16/input_1.txt', 'r')
# input_file = open('day16/input_short.txt', 'r')
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

# for v in valves:
#     print(valves[v])

# print("------")
optimize_valves(valves=valves)

valves["AA"].pressure = flow_A

# for v in valves:
#     print(valves[v])


score = go_explore(valve="AA", remaining_turns=30, opened_valves="", score=0, jump_length=0)
print(score)