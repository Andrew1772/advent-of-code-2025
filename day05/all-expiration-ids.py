#!/usr/bin/python3

def order_dates(ranges):

    if not ranges:
        return []

    # lambda is used since sorted key wants a function here, so said the internet
    ranges = sorted(ranges, key=lambda x: x[0])

    first_start = ranges[0][0]
    first_end = ranges[0][1]
    merged = [[first_start, first_end]]

    for i in range(1, len(ranges)):
        current_start = ranges[i][0]
        current_end = ranges[i][1]

        last_start = merged[-1][0]
        last_end = merged[-1][1]

        if current_start <= last_end + 1:
            # max is needed because we cannot assume the current_end will always be larger than last_end
            merged[-1][1] = max(last_end, current_end)
        else:
            merged.append([current_start, current_end])

    return merged


def main():

    with open("../puzzle-inputs/expiration-dates.txt", "r") as f:
        lines = [ line.strip() for line in f if line.strip() ]

    dates = []
    total = 0

    for line in lines:
        if "-" in line:
            start, end = line.split("-")
            print("line", line, "start", start, "end", end)
            dates.append((int(start), int(end)))
        else:

            ordered_dates = order_dates(dates)

            for start, end in ordered_dates:
                total += (end - start + 1)
            # need to clean out all the ranges, after getting the largest range
            dates = []

    print(total)


main()
