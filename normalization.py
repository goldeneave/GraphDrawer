# the code snippet is used to refine each origin csv file
# delete redundant value(.json.xz) and sort them by date

import csv
import os

def sort_csv_files(folder_path, output_folder_path):
    # Loop over all the CSV files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            # Path to the input CSV file
            input_path = os.path.join(folder_path, file_name)

            # Path to the output CSV file
            output_path = os.path.join(output_folder_path, file_name[:-4] + "_sorted.csv")

            # Define the header row
            header = ["Date Time", "Like Count", "Comment Count"]

            # Open the input CSV file for reading
            with open(input_path, "r") as input_file:
                reader = csv.reader(input_file)

                # Create a list to store the rows from the input CSV file
                rows = []

                # Loop through each row in the input CSV file
                for row in reader:
                    # Remove the "_UTC.json.xz" from the second column
                    row[1] = row[1].replace("_UTC.json.xz", "")

                    # Add the row to the list of rows
                    rows.append(row)

                # Sort the rows by the value in the second column
                rows.sort(key=lambda x: x[1])

                # Remove the first column from each row
                rows = [row[1:] for row in rows]

            # Open the output CSV file for writing
            with open(output_path, "w", newline="") as output_file:
                writer = csv.writer(output_file)

                # Write the header row to the output CSV file
                writer.writerow(header)

                # Write the sorted rows to the output CSV file
                writer.writerows(rows)

folder_path = "ImageFeatureExtract/result/EngNum"
output_folder_path = "scatterDrawer/csv"
sort_csv_files(folder_path, output_folder_path)
