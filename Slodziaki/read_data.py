import csv
import sys
import numpy as np

# each sequence needs to be one element in the returned list
def read_csv(path):
    data = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        prev_row_name = ""
        current_sequence = []
        for row in reader:
            if prev_row_name == row[0]:
                current_sequence.append(row[1])
            else:
                data.append(current_sequence)
                current_sequence = [row[1]] 
                prev_row_name = row[0]
    return data[2:]


def main(args):
    og_data = []
    og_path = "/home/agentolek/AI/Bootcamp-mini-hackathon-2024/dane/zadanie_1/znaki-sekwencje-20160604-original.csv"
    og_data = read_csv(og_path)

    print(og_data[0])

if __name__ == "__main__":
    main(sys.argv)