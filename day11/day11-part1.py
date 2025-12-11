#!/usr/bin/python3

count = 0


def timelines(devices, steps):

    next_step = []
    global count


    if "out" in steps:
        del steps["out"]
        if steps == []:
            return

    # turns a list of list into a single list [[1, 2], [1, 2, 3,]] => [1, 2, 1, 2, 3]
    for sub_list in steps:
        if isinstance(sub_list, list):
            next_step.extend(sub_list)
        else:
            next_step.append(sub_list)

    if "you" in devices:
        start = devices["you"]
        del devices["you"]

        next_step = [ val for val in start ]
        timelines(devices, next_step)

    next_next_steps = []

    if next_step:
        for val in next_step:
            if val == "out":
                count += 1 
                print(count)
                continue

            if val in devices:
                next_next_steps.append(devices[val])

    timelines(devices, next_next_steps)



def main():

    devices = {}

    with open("../puzzle-inputs/day11.txt") as f:
        for line in f:
            line = line.strip()

            key, values = line.split(":")
            key = key.strip()

            list_of_values = values.strip().split()
            devices[key] = list_of_values

    timelines(devices, [])
    print(count)

main()
