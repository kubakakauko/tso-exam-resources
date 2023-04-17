import pandas as pd
import numpy as np
import math

def entropy(y):
    unique_labels, label_counts = np.unique(y, return_counts=True)
    probabilities = label_counts / len(y)
    entropy_value = -np.sum([p * np.log2(p) if p > 0 else 0 for p in probabilities])
    return entropy_value

def weighted_entropy(data, feature, target):
    unique_feature_values, feature_counts = np.unique(data[feature], return_counts=True)
    entropy_sum = 0
    total_samples = len(data)
    
    for value, count in zip(unique_feature_values, feature_counts):
        data_subset = data[data[feature] == value]
        y_subset = data_subset[target]
        subset_entropy = entropy(y_subset)
        print(f'  Entropy({feature}={value}): {subset_entropy}')
        
        weight = count / total_samples
        entropy_sum += weight * subset_entropy
        
    return entropy_sum

def id3_algorithm(data, target):
    print("\nCalculating dataset entropy:")
    dataset_entropy = entropy(data[target])
    print(f'Entropy(Y): {dataset_entropy}')

    print("\nCalculating information gain for each feature:")
    features = [col for col in data.columns if col != target]

    max_info_gain = -math.inf
    best_feature = None

    for feature in features:
        print(f'\nFeature: {feature}')
        feature_entropy = weighted_entropy(data, feature, target)
        info_gain = dataset_entropy - feature_entropy
        print(f'Information Gain({feature}): {info_gain}')

        if info_gain > max_info_gain:
            max_info_gain = info_gain
            best_feature = feature

    print(f'\nBest feature: {best_feature}')
    return best_feature

# Load CSV file
filename = "ID3V_CSV.csv"
data = pd.read_csv(filename, dtype={'A': 'bool', 'B': 'bool', 'C': 'bool', 'Y': 'bool'}, true_values=['T'], false_values=['F'])

# Set the target column name
target = "Y"

# Run the ID3 algorithm
best_feature = id3_algorithm(data, target)
