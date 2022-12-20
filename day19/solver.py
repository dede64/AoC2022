import re
import time

from functools import cache

MINING_ROUNDS = 24

# Load the file
input_file = open('day19/input_1.txt', 'r')
# input_file = open('day19/input_short.txt', 'r')
lines = input_file.readlines()

blueprints = []

for line in lines:

    # Apply match regex on the line.
    data = list(map(int, re.match("Blueprint ([\d]+): Each ore robot costs ([\d]+) ore. Each clay robot costs ([\d]+) ore. Each obsidian robot costs ([\d]+) ore and ([\d]+) clay. Each geode robot costs ([\d]+) ore and ([\d]+) obsidian.", line.strip()).groups()))

    blueprints.append({
        "id": data[0],
        "ore": {
            "ore": data[1]
        },
        "clay": {
            "ore": data[2]
        },
        "obsidian": {
            "ore": data[3],
            "clay": data[4]
        },
        "geode": {
            "ore": data[5],
            "obsidian": data[6]
        }
    })

def sort_robots(robots: str):

    r = []

    for ch in robots:
        r.append(ch)
    r = sorted(r)
    return "".join(r)

def simulate_blueprint(blueprint):

    @cache
    def simulate(robots: str, remaining_rounds, ore, clay, obsidian, geode):

        if remaining_rounds == 0:
            return geode
        remaining_rounds -= 1

        # 1. Check which robots can be built.
        to_build = []

        if ore >= blueprint["ore"]["ore"] and remaining_rounds > MINING_ROUNDS / 2 - 8:
            to_build.append("O")
        if ore >= blueprint["clay"]["ore"] and remaining_rounds > MINING_ROUNDS / 2 - 8:
            to_build.append("C")
        if ore >= blueprint["obsidian"]["ore"] and clay >= blueprint["obsidian"]["clay"]:
            to_build.append("B")
        if ore >= blueprint["geode"]["ore"] and obsidian >= blueprint["geode"]["obsidian"]:
            to_build.append("G")

        # 2. Collect ore from already built robots.
        for robot in robots:
            if robot == "O":
                ore += 1
            elif robot == "C":
                clay += 1
            elif robot == "B":
                obsidian += 1
            elif robot == "G":
                geode += 1

        # 3. Build the robots and continue.
        # Continue without building anything.
        max_geode = 0
        if "G" not in to_build:
            max_geode = simulate(robots=robots, remaining_rounds=remaining_rounds, ore=ore, clay=clay, obsidian=obsidian, geode=geode)

        for robot in to_build:
            tmp = 0
            if robot == "O":
                tmp = simulate(robots=sort_robots(f"{robots}O"), remaining_rounds=remaining_rounds, ore=ore-blueprint["ore"]["ore"], clay=clay, obsidian=obsidian, geode=geode)
            elif robot == "C":
                tmp = simulate(robots=sort_robots(f"{robots}C"), remaining_rounds=remaining_rounds, ore=ore-blueprint["clay"]["ore"], clay=clay, obsidian=obsidian, geode=geode)
            elif robot == "B":
                tmp = simulate(robots=sort_robots(f"{robots}B"), remaining_rounds=remaining_rounds, ore=ore-blueprint["obsidian"]["ore"], clay=clay-blueprint["obsidian"]["clay"], obsidian=obsidian, geode=geode)
            elif robot == "G":
                tmp = simulate(robots=sort_robots(f"{robots}G"), remaining_rounds=remaining_rounds, ore=ore-blueprint["geode"]["ore"], clay=clay, obsidian=obsidian-blueprint["geode"]["obsidian"], geode=geode)

            max_geode = tmp if tmp > max_geode else max_geode
        # 4. Return the max geode achieved.
        return max_geode
        
    max_geode = simulate(robots="O", remaining_rounds=MINING_ROUNDS, ore=0, clay=0, obsidian=0, geode=0)

    simulate.cache_clear()
    return blueprint["id"] * max_geode


score = 0

start = time.time()
for blueprint in blueprints:
    b_start = time.time()
    print(f'Processing blueprint N{blueprint["id"]}.')
    tmp = simulate_blueprint(blueprint=blueprint)
    score += tmp
    b_end = time.time()
    print(f'Blueprint N{blueprint["id"]} took {(b_end - b_start):.2f}s.  In total {(b_end - start):.2f}s. Score: {tmp}')


print(score)