#!/usr/bin/python3





def main():

    with open("../puzzle-inputs/expiration-dates.txt", "r") as f:
        lines = [ line.strip() for line in f if line.strip() ]

    dates = []
    fresh = 0

    for line in lines:
        if "-" in line:
            start, end = line.split("-")
            print("line", line, "start", start, "end", end)
            dates.append((int(start), int(end)))
        else:
            for start, end in dates:
                if start <= int(line) <= end:
                    fresh +=1 
                    break

    print(fresh)




main()
