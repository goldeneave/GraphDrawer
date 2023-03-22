import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def line_drawer(csv_file, column_num, time_interval=None):
    data = pd.read_csv(csv_file)

    for i, row in data.iterrows():
        try:
            data.at[i, 'Date Time'] = datetime.strptime(row['Date Time'], '%Y-%m-%d_%H-%M-%S')
        except ValueError:
            continue

    if time_interval:
        grouped_data = data.groupby(pd.Grouper(key='Date Time', freq=f'{time_interval}D')).mean().reset_index()
    else:
        grouped_data = data.groupby('Date Time').mean().reset_index()

    if column_num == 1:
        column_name = 'Comment Count'
        y_data = grouped_data['Comment Count']
        print(y_data)

    elif column_num == 2:
        column_name = 'Like Count'
        y_data = grouped_data['Like Count']
        print(y_data)

    else:
        raise ValueError('Invalid column number')

    plt.plot(grouped_data['Date Time'], y_data)
    plt.xlabel('Time')
    plt.xticks(rotation=60)
    plt.ylabel(column_name)
    plt.show()

csv_path = "new/aldo_shoes_EngNum_sorted.csv"
line_drawer(csv_path, 1, time_interval=30)