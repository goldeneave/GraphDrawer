import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def plot_scatter(csv_file, column_num, time_interval=None):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Convert the time format into a standard datetime object
    for i, row in data.iterrows():
        try:
            data.at[i, 'Date Time'] = datetime.strptime(row['Date Time'], '%Y-%m-%d_%H-%M-%S')
        except ValueError:
            continue

    if time_interval:
        # Compute the average value for each time point
        grouped_data = data.groupby(pd.Grouper(key='Date Time', freq=f'{time_interval}D')).mean().reset_index()

        # Set the x-axis label and rotate the ticks
        plt.xlabel(f'Time (every {time_interval} days)')
        plt.xticks(rotation=45)
    else:
        # Compute the average value for each time point without grouping by time interval
        grouped_data = data.groupby('Date Time').mean().reset_index()

        # Set the x-axis label and rotate the ticks
        plt.xlabel('Time')
        plt.xticks(rotation=45)

    # Get the name of the column to use for the y-axis
    if column_num == 1:
        column_name = 'Comment Count'
    elif column_num == 2:
        column_name = 'Like Count'
    else:
        raise ValueError('Invalid column number')

    # Create a scatter plot
    for i in range(len(grouped_data)):
        try:
            plt.scatter(grouped_data.iloc[i]['Date Time'], grouped_data.iloc[i][column_name])
        except ValueError:
            continue

    # Set the y-axis label
    plt.ylabel(column_name)

    print(grouped_data['Comment Count'])
    print(grouped_data['Like Count'])

    # Display the plot
    plt.show()



csv_path = "new/aldo_shoes_EngNum_sorted.csv"
plot_scatter(csv_path, column_num=1, time_interval=30)