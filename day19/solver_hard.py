import re
import time

from functools import cache

MINING_ROUNDS = 32

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

def simulate_blueprint(blueprint):

    max_ore = max([blueprint["clay"]["ore"], blueprint["obsidian"]["ore"], blueprint["geode"]["ore"]])
    max_clay = blueprint["obsidian"]["clay"]
    max_obsidian = blueprint["geode"]["obsidian"]

    @cache
    def simulate(remaining_rounds, ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r):

        if remaining_rounds < 7 and obsidian_r == 0 or remaining_rounds < 5 and geode_r == 0:
            return 0

        if remaining_rounds == 0:
            return geode
        remaining_rounds -= 1

        # 1. Check which robots can be built.
        to_build = []

        if ore_r < max_ore and ore >= blueprint["ore"]["ore"] and remaining_rounds > MINING_ROUNDS / 2 - 9:
            to_build.append("O")
        if clay_r < max_clay and ore >= blueprint["clay"]["ore"] and remaining_rounds > MINING_ROUNDS / 2 - 9:
            to_build.append("C")
        if obsidian_r < max_obsidian and ore >= blueprint["obsidian"]["ore"] and clay >= blueprint["obsidian"]["clay"]:
            to_build.append("B")
        if ore >= blueprint["geode"]["ore"] and obsidian >= blueprint["geode"]["obsidian"]:
            to_build.append("G")

        # 2. Collect ore from already built robots.
        ore += ore_r
        clay += clay_r
        obsidian += obsidian_r
        geode += geode_r

        # 3. Build the robots and continue.
        # Continue without building anything.
        max_geode = 0
        if not (ore > max_ore and clay > max_clay and obsidian > max_obsidian):
            max_geode = simulate(remaining_rounds=remaining_rounds, ore=ore, clay=clay, obsidian=obsidian, geode=geode, ore_r=ore_r, clay_r=clay_r, obsidian_r=obsidian_r, geode_r=geode_r)

        if "G" in to_build:
            tmp = simulate(remaining_rounds=remaining_rounds, ore=ore-blueprint["geode"]["ore"], clay=clay, obsidian=obsidian-blueprint["geode"]["obsidian"], geode=geode, ore_r=ore_r, clay_r=clay_r, obsidian_r=obsidian_r, geode_r=geode_r + 1)
            max_geode = tmp if tmp > max_geode else max_geode

        else:

            for robot in to_build:
                tmp = 0
                if robot == "O":
                    tmp = simulate(remaining_rounds=remaining_rounds, ore=ore-blueprint["ore"]["ore"], clay=clay, obsidian=obsidian, geode=geode, ore_r=ore_r + 1, clay_r=clay_r, obsidian_r=obsidian_r, geode_r=geode_r)
                elif robot == "C":
                    tmp = simulate(remaining_rounds=remaining_rounds, ore=ore-blueprint["clay"]["ore"], clay=clay, obsidian=obsidian, geode=geode, ore_r=ore_r, clay_r=clay_r + 1, obsidian_r=obsidian_r, geode_r=geode_r)
                elif robot == "B":
                    tmp = simulate(remaining_rounds=remaining_rounds, ore=ore-blueprint["obsidian"]["ore"], clay=clay-blueprint["obsidian"]["clay"], obsidian=obsidian, geode=geode, ore_r=ore_r, clay_r=clay_r, obsidian_r=obsidian_r + 1, geode_r=geode_r)
                elif robot == "G":
                    tmp = simulate(remaining_rounds=remaining_rounds, ore=ore-blueprint["geode"]["ore"], clay=clay, obsidian=obsidian-blueprint["geode"]["obsidian"], geode=geode, ore_r=ore_r, clay_r=clay_r, obsidian_r=obsidian_r, geode_r=geode_r + 1)

                max_geode = tmp if tmp > max_geode else max_geode

        # 4. Return the max geode achieved.
        return max_geode
        
    max_geode = simulate(remaining_rounds=MINING_ROUNDS, ore=0, clay=0, obsidian=0, geode=0, ore_r=1, clay_r=0, obsidian_r=0, geode_r=0)

    simulate.cache_clear()
    return max_geode

start = time.time()

scores = []

for blueprint in blueprints:
    if blueprint["id"] > 3:
        continue

    b_start = time.time()
    print(f'Processing blueprint N{blueprint["id"]}.')
    scores.append(simulate_blueprint(blueprint=blueprint))
    b_end = time.time()
    print(f'Blueprint N{blueprint["id"]} took {(b_end - b_start):.2f}s.  In total {(b_end - start):.2f}s. Score: {scores[-1]}')


print(scores)
print(scores[0] * scores[1] * scores[2])