
import pandas as pd
import math

def entropy(data, target_col):
    value_counts = data[target_col].value_counts()
    total = len(data)
    ent = 0
    for count in value_counts:
        p = count / total
        ent -= p * math.log2(p)
    return ent

def information_gain(data, attribute, target_col):
    unique_values = data[attribute].unique()
    total = len(data)
    ent = entropy(data, target_col)
    weighted_entropy = 0
    
    for value in unique_values:
        subset = data[data[attribute] == value]
        subset_entropy = entropy(subset, target_col)
        weighted_entropy += len(subset) / total * subset_entropy

    return ent - weighted_entropy

def main():
    # Read the dataset from user input
    data = pd.read_csv('tennis.csv')
    target_col = 'Play Tennis'
    attributes = list(data.columns)
    attributes.remove(target_col)

    # Calculate Information Gain for each attribute
    info_gains = {attribute: information_gain(data, attribute, target_col) for attribute in attributes}

    # Print the Information Gain for each attribute
    for attribute, info_gain in info_gains.items():
        print(f"{attribute}: {info_gain:.4f}")

if __name__ == "__main__":
    main()
