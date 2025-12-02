#!/usr/bin/python3


def check_all_same(num, first, length):
    for i in range(0, length-1):
        if num[i] != num[i+1]:
            return False
    return True

def id_checker(num):
    return num in (num + num)[1:-1]


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

                if id_checker(num):
                    total += int(num)

        print(total)



main()
