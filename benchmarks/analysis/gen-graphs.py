import re
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import json

# Ensure the output directory exists
output_dir = 'graphs/matrixMultiply'

def GetColumns(input_text):
    # Split input text into lines
    lines = input_text.strip().split('\n')

    # Extract headers
    headers = re.split(r'\s+', lines[0].strip('#').strip())

    # Initialize a dictionary to store values column-wise
    columns = {header: [] for header in headers}

    # Extract values
    for line in lines[1:]:
        values = list(map(int, re.split(r'\s+', line.strip())))
        for header, value in zip(headers, values):
            columns[header].append(value)
    
    return columns

def strip_zeros(data_dict):
    return {key: {k: v for k, v in value.items() if v != 0} for key, value in data_dict.items()}
def remove_empty_labels(data_dict):
    return {key: value for key, value in data_dict.items() if value}

def generate_grouped_bar_graphs(input_files, labels, grouping, output_dir, output_prefix, colors):
    # Initialize a dictionary to store sums for each column across all files
    group_sums = {}

    # Extract columns and calculate sums for each group
    headers = None
    for group_name, group_indices in grouping.items():
        group_sum = {label: {header: 0 for header in headers} for label in labels} if headers else {}
        for index in group_indices:
            with open(input_files[index], "r") as f:
                columns = GetColumns(f.read())
                # if index == 3:
                #     print(columns)
                if headers is None:
                    headers = list(columns.keys())
                    group_sum = {label: {header: 0 for header in headers} for label in labels}
                label = labels[index]
                for header in headers:
                    # if index == 3:        
                    #     print(label)
                    #     print(header)
                    group_sum[label][header] += sum(columns[header])
        group_sums[group_name] = remove_empty_labels(strip_zeros(group_sum))
        # if index == 3:
            # print(group_sums[group_name])
            # print(group_name)
        
        # group_sums = remove_empty_labels(strip_zeros(group_sums[group_name]))
    return group_sums

def GenerateSumGraphs(data, output_dir):

    # Extracting datasets and metrics
    datasets = list(data.keys())  # ['cheri,regular']
    metrics = list(data['cheri,regular']['cheri'].keys())  # All the metrics

    # Iterate over each metric to create an independent bar chart
    for metric in metrics:
        # Fetch values for 'cheri' and 'regular' configurations for each dataset
        cheri_values = [data[dataset]['cheri'][metric] for dataset in datasets]
        regular_values = [data[dataset]['regular'][metric] for dataset in datasets]
    
        # Plotting configuration
        x = np.arange(len(datasets))  # Label locations
        width = 0.35  # Width of the bars
    
        # Plotting
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, cheri_values, width, label='Cheri')
        rects2 = ax.bar(x + width/2, regular_values, width, label='Regular')
    
        # Labels and title
        ax.set_xlabel('Benchmark Dataset Size')
        ax.set_ylabel(f'Count of {metric}')
        ax.set_title(f'Comparison of Cheri and Regular for {metric}')
        ax.set_xticks(x)
        ax.set_xticklabels(datasets, rotation=45, ha="right")
        ax.legend()
    
        # Layout and save
        fig.tight_layout()
        filename = os.path.join(output_dir, f'matrixMultiply-{metric.replace("/", "_")}.png')
        plt.savefig(filename)
        plt.close(fig)  # Close the figure after saving to avoid display overlap



# Example usage
if __name__ == "__main__":
    input_files = sys.argv[1:-5]  # List of input files
    labels = sys.argv[-5].split(",")  # List of labels
    print(sys.argv[-4])
    grouping = {group.split(":")[0]: list(map(int, group.split(":")[1].split(","))) for group in sys.argv[-4].split(";")}  # Grouping info
    colors = sys.argv[-3].split(",")  # List of colors
    output_dir = sys.argv[-2]  # Output directory
    output_prefix = sys.argv[-1]  # Output file prefix

    group_sums = generate_grouped_bar_graphs(input_files, labels, grouping, output_dir, output_prefix, colors)

    # Make the result directory 
    os.makedirs(output_dir, exist_ok=True)

    # Save dataset 
    # Write the modified data to a new JSON file
    with open('benchmark.json', 'w') as f:
        json.dump(output_dir, f)

    # Generate group sum graphs 
    GenerateSumGraphs(group_sums, "")

