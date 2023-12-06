import random as rand
import pandas as pd

#Fix the randomness
seed = 1234
rand.seed(seed)

import pandas as pd
import random

def load_data(input_file):
    data = pd.read_csv(input_file, header=None)
    return data

def split_data(input_file, output_file_1, output_file_2, ratio_split=0.2):
    df = pd.read_csv(input_file)

    # Remove columns: date, country (Since every data is collected inside USA)
    df = df.drop(columns=["date", "country"])

    # 1. Filter noisy data (house with prices == 0.0)
    df = df[df["price"] > 100]
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    total_rows = len(df)
    split_index = int(total_rows * (1 - ratio_split))

    set_1 = df.iloc[:split_index, :]
    set_2 = df.iloc[split_index:, :]

    set_1.to_csv(output_file_1, index=False, header = True)
    set_2.to_csv(output_file_2, index=False, header = True)
    return None