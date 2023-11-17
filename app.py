import csv
import yaml

# Open the CSV file and read the contents
path='C:/Users/Smiwi1502186/Desktop/csv_to_yml/Catalog_v2.csv'
with open(path, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Create an empty list to store the data
    data = []
    
    # Iterate over the rows of the CSV file and append each row to the data list
    for row in csv_reader:
        print(row)
        data.append(row)
# Open the YAML file and write the data to it
with open('yaml_file.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)