#!/usr/bin/python3


def find_highest_voltage(bank):
    a = bank[0]
    b = bank[1]

    if b > a:
        a, b = b, a

    print("For bank:", bank)
    for i in range(2, len(bank)):
        if bank[i] > a and not i == len(bank) -1:
            a = bank[i]
            b = '0'
        elif bank[i] > b:
            #print(bank[i], ">", b)
            b = bank[i]

    c = a + b
    print("This is the largest joltage:", c)
    return c



def main():
    
    with open("../puzzle-inputs/battery-banks.txt", "r") as f:
        banks = [line.strip() for line in f if line.strip()]
        total = 0


        test = ["5373475263753258336423442254746263332334232217334431337464342726873125223932312363675175435324343745"]

        for bank in banks:
            total = total + int(find_highest_voltage(bank))

        print("Total output joltage:", total)





main()
