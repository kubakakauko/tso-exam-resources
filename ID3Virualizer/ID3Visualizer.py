import pandas as pd
import numpy as np
from collections import Counter

def entropy(y):
    n_labels = len(y)
    if n_labels <= 1:
        return 0
    counts = np.bincount(y)
    probs = counts / n_labels
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

def information_gain(parent_entropy, left_child, right_child):
    num_left = len(left_child)
    num_right = len(right_child)
    total = num_left + num_right
    return parent_entropy - (num_left / total) * entropy(left_child) - (num_right / total) * entropy(right_child)

def id3_algorithm(data, target_attribute, attributes, parent=None):
    unique_labels = np.unique(data[target_attribute])
    if len(unique_labels) == 1:
        return unique_labels[0]
    if not attributes:
        return Counter(data[target_attribute]).most_common(1)[0][0]
    parent_entropy = entropy(data[target_attribute])
    info_gains = []
    for attribute in attributes:
        left_child = data[data[attribute] == 0][target_attribute]
        right_child = data[data[attribute] == 1][target_attribute]
        info_gains.append(information_gain(parent_entropy, left_child, right_child))
    best_attribute = attributes[np.argmax(info_gains)]
    tree = {best_attribute: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attribute]
    for value in np.unique(data[best_attribute]):
        subset = data[data[best_attribute] == value]
        tree[best_attribute][value] = id3_algorithm(subset, target_attribute, remaining_attributes)
    return tree

# Define the dataset
data = {'A': [0, 1, 0, 0],
        'B': [0, 1, 0, 1],
        'C': [1, 1, 0, 0],
        'Y': [0, 1, 1, 0]}

# Convert dataset into pandas dataframe
df = pd.DataFrame(data)

# Define the target attribute and remaining attributes
target_attribute = 'Y'
attributes = [col for col in df.columns if col != target_attribute]

# Run ID3 algorithm on the dataset
tree = id3_algorithm(df, target_attribute, attributes)
print(tree)
