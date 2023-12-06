import random as rand
import pandas as pd

#Fix the randomness
rand.seed(1234)

def load_data(input_file):
    data = pd.read_csv(input_file, header=None)
    return data

def split_data(input_file, output_file_1, output_file_2, ratio_split=0.2):
    with open(input_file, 'r') as file:
        data_lines = file.readlines()

    total_lines = len(data_lines)
    split_index = int(total_lines * (1 - ratio_split))

    rand.shuffle(data_lines)

    set_1 = data_lines[:split_index]
    set_2 = data_lines[split_index:]

    with open(output_file_1, 'w') as file_1:
        file_1.writelines(set_1)

    with open(output_file_2, 'w') as file_2:
        file_2.writelines(set_2)

    return None
