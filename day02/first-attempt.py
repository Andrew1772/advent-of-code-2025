#!/usr/bin/python3

def invalid_id_finder(first, last, string):

    if last - first <= 0:
        print("invalid id:", string)
        return True

    if string[first] == string[last]:
        invalid_id_finder(first + 1, last - 1, string)
    else:
        return False


def main():

    with open("product-ids.txt", "r") as f:
        ugly_ids = f.read().strip()

        ids = ugly_ids.split(",")
        print("ids:", ids)
        
        total = 0

        for rang in ids:
            first, last = rang.split("-")
            print("range", first, "-", last)

            for num in range(int(first), int(last)):
                num = str(num)
                if invalid_id_finder(0, len(num)-1, num):
                    total += int(num)

        print("total:", total)


main()

