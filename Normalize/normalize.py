import csv
import numpy as np

def normalize(data):
    min_value = min(data)
    max_value = max(data)
    return [(value - min_value) / (max_value - min_value) for value in data]

def read_csv(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        data = {header: [] for header in headers}
        
        for row in csv_reader:
            for header, value in zip(headers, row):
                data[header].append(float(value))
                
    return data

def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        headers = list(data.keys())
        csv_writer.writerow(headers)
        
        num_rows = len(data[headers[0]])
        for row_index in range(num_rows):
            csv_writer.writerow([data[header][row_index] for header in headers])

if __name__ == "__main__":
    input_file = "values.csv"
    output_file = "normalized_values.csv"
    
    data = read_csv(input_file)
    normalized_data = {header: normalize(values) for header, values in data.items()}
    
    write_csv(output_file, normalized_data)
