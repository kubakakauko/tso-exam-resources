import csv
from collections import Counter
from typing import List, Tuple
from math import sqrt


def read_data_from_csv(filename: str, label_column: str, distance_column: str) -> List[Tuple[str, float]]:
    data = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Read header row
        header = next(reader)
        label_index = header.index(label_column)
        distance_index = header.index(distance_column)

        for row in reader:
            label = row[label_index]
            feature = float(row[distance_index])
            data.append((label, feature))

    return data


def euclidean_distance(a: float, b: float) -> float:
    return sqrt((a - b) ** 2)


def knn(k: int, data: List[Tuple[str, float]], target_value: float) -> str:
    sorted_data = sorted(data, key=lambda x: euclidean_distance(x[1], target_value))
    nearest_neighbors = sorted_data[:k]
    category_count = Counter([category for category, _ in nearest_neighbors])

    # Handle ties
    if len(category_count) > 1 and category_count.most_common(2)[0][1] == category_count.most_common(2)[1][1]:
        return nearest_neighbors[0][0]
    else:
        return category_count.most_common(1)[0][0]


def print_distance_table(data: List[Tuple[str, float]], target_value: float):
    print("\nEuclidean Distance Table:")
    print("Label\tDistance")
    for label, feature in data:
        distance = euclidean_distance(feature, target_value)
        print(f"{label}\t{distance:.2f}")


def main():
    filename = input("Enter the CSV filename containing the data: ")
    label_column = input("Enter the name of the column for classification: ")
    distance_column = input("Enter the name of the column to calculate distance for: ")
    k = int(input("Enter the value of k: "))
    target_value = float(input("Enter the number to calculate distance for: "))

    data = read_data_from_csv(filename, label_column, distance_column)
    print_distance_table(data, target_value)
    result = knn(k, data, target_value)

    print(f"\n {distance_column} of {target_value} is classified as: {result}")


if __name__ == "__main__":
    main()
