#!/usr/bin/python3

# First time using pandas!!!
import pandas as pd


def main():

    count = 0

    with open("../puzzle-inputs/homework.txt") as f:
        # if isdigit then store in rows as int, if not keep as string. all while spliting on ' '
        # this is completely unnecessary, but it was fun to write :)
        rows = [[int(x) if x.isdigit() else x for x in row.split()] for row in f if row.split()]

        dataframe = pd.DataFrame(rows)

        for col in dataframe.columns:
            if dataframe.iloc[-1,col] == '+':
                count += dataframe.iloc[:-1,col].sum()
            else:
                count += dataframe.iloc[:-1,col].product()

        print(count)



main()
