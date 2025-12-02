#!/usr/bin/python3


def id_checker(num, first, second, length):

    if second > length:
        print("invalid:", num)
        return True

    if num[first] == num[second]:
        return id_checker(num, first +1, second +1, length)
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
                if int(len(num)) % 2 == 1:
                    continue
                half_len = len(num)//2
                if id_checker(num, 0, half_len, len(num)-1):
                    total += int(num)

        print(total)



main()
