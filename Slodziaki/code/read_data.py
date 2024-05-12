import csv
import sys
import pandas

# each sequence needs to be one element in the returned list
def read_seqs(path):
    dict = {}
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        prev_row_name = ""
        current_sequence = []
        for row in reader:
            if prev_row_name == row[0]:
                current_sequence.append(row[1])
            else:
                dict[prev_row_name] = current_sequence
                current_sequence = [row[1]]
                prev_row_name = row[0]
        dict[prev_row_name] = current_sequence

    return dict

def read_scenes(path):
    dict = {}
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        object_name =""
        curr_scenes= []
        for row in reader:
            if object_name == row[0]:
                curr_scenes.append(row[2])
            else:
                dict[object_name] = curr_scenes
                curr_scenes = [row[2]]
                object_name = row[0]

        dict[object_name] = curr_scenes

    return dict

def read_object_seqs(path):
    data = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = [list(row) for row in reader]

    return data

def create_frame():
    sequence_path = "/home/agentolek/AI/Bootcamp-mini-hackathon-2024/dane/zadanie_2/znaki-sekwencje-20160604.csv"
    sequence_dict = read_seqs(sequence_path)

    scenes_path = "/home/agentolek/AI/Bootcamp-mini-hackathon-2024/dane/zadanie_2/obiekty-sceny-20160604.csv"
    object_scenes = read_scenes(scenes_path)

    object_sequences_path = "/home/agentolek/AI/Bootcamp-mini-hackathon-2024/dane/zadanie_2/obiekty-sekwencje-20160604.csv"
    object_sequences = read_object_seqs(object_sequences_path)

    ultimate_data = []
    for elem in object_sequences:
        list_elem = elem
        list_elem.append(sequence_dict.get(elem[1])) # get by sequence name
        list_elem.append(object_scenes.get(elem[0])) # get by object name
        ultimate_data.append(list_elem)
        
    my_frame = pandas.DataFrame(ultimate_data, columns=("object_name", "seq_name", "num_of_sequences", "sequence_len", "cycle", "sequence_values", "scenes"))

    return my_frame

if __name__ == "__main__":
    create_frame()