#!/usr/bin/python3

import itertools

# returns a list of true/false, after button is pressed
def press_button(jolt, button):

    for i in range(len(jolt)):
        if i in button:
            jolt[i] += 1

    return jolt


# looks at one line, returns lowest button presses
def pressing_some_buttons(line):

    end = len(line) - 1

    #break line into parts, lights is a list of true/false. buttons is a list of lists of ints
    lights = [light == '#' for light in line[0].strip("[]")]
    temp_buttons = []

    for button in range(1, end):
      temp_buttons.append(line[button])

    buttons = [list(map(int, string.strip("()").split(","))) for string in temp_buttons]

    # Using this in part 2, will come back to later
    jolts = [int(jolt) for jolt in line[end].strip("{}").split(",")]

    # now we have the parts we want

    times_pressed = 0
    best = 9999

    for length in range(1, 100):
        for collection_of_buttons in itertools.product(buttons, repeat=length):

            current_jolt = [0 for i in range(len(jolts))]
            times_pressed = 0

            for button in collection_of_buttons:
                current_jolt = press_button(current_jolt, button)
                times_pressed += 1
            print(current_jolt)
            if current_jolt == jolts:
                if best > times_pressed:
                    best = times_pressed
                    break


    return best

def main():

    lines = []

    with open("../puzzle-inputs/indicator-lights-test.txt") as f:
        raw_lines = [ line.strip() for line in f if line.strip() ]

        for raw_line in range(len(raw_lines)): 
            lines.append((raw_lines[raw_line].split()))

    total = 0
    total = pressing_some_buttons(lines[0])
    #for line in lines:
    #    print(line)
    #    total = total + pressing_some_buttons(line)

    print(total)

main()
