#!/usr/bin/python3


def find_highest_voltage(bank):
    total = ""
    start = 0

    while len(total) < 12:
        remaining = 12 - len(total)
        end = len(bank) - remaining

        highest = '-1'
        # This is the last position that I searched
        last_position = start

        for i in range(start, end + 1):
            if bank[i] > highest:
                highest = bank[i]
                last_position = i
                # early exit if we find a 9, can't be higher than this
                if highest == '9':
                    break

        total += str(highest)
        start = last_position + 1


    print("for bank:", bank)
    print("largest joltage:", total)
    return total



def main():
    
    with open("../puzzle-inputs/battery-banks.txt", "r") as f:
        banks = [line.strip() for line in f if line.strip()]
        total = 0

        test = ["5373475263753258336423442254746263332334232217334431337464342726873125223932312363675175435324343745"]

        for bank in banks:
            total += int(find_highest_voltage(bank))

        print("Total output joltage:", total)


main()
