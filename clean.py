# the code is used to clean redundant row after sort origin data
# save new generated file into a new folder

import os
import pandas as pd


def csvCleaner(input_path, output_path):
    for csv_file in os.listdir(input_path):
        if csv_file.endswith('.csv'):
            csv_input_path = os.path.join(input_path, csv_file)
            csv_output_path = os.path.join(output_path, csv_file)
            print(csv_input_path)

            try:
                df = pd.read_csv(csv_input_path)
            except Exception as e:
                print(f"Error reading file {csv_file}: {e}")
                continue

            if 'Date Time' not in df:
                print(f"Error: 'Date Time' column not found in file {csv_file}")
                continue

            indexes = df[df['Date Time'] == 'File Name'].index

            if len(indexes) == 0:
                print(f"No rows containing 'File Name' found in file {csv_file}")
                df.to_csv(csv_output_path, index=False)
                continue

            last_idx = indexes[0]
            df = df.iloc[:last_idx, :]

            try:
                df.to_csv(csv_output_path, index=False)
            except Exception as e:
                print(f"Error writing file {csv_file}: {e}")
                continue

            print(f"{csv_file} has been cleaned!")



csvCleaner("csv", "new")