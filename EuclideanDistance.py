
import csv
from collections import Counter
from typing import List, Tuple
from math import sqrt


def read_data_from_csv(filename: str, label_column: str) -> List[Tuple[str, List[float]]]:
    data = []

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Read header row
        header = next(reader)
        label_index = header.index(label_column)

        for row in reader:
            label = row[label_index]
            features = [float(value) for i, value in enumerate(row) if i != label_index]
            data.append((label, features))

    return data


def euclidean_distance(a: List[float], b: List[float]) -> float:
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn(k: int, data: List[Tuple[str, List[float]]], target_features: List[float]) -> str:
    sorted_data = sorted(data, key=lambda x: euclidean_distance(x[1], target_features))
    nearest_neighbors = sorted_data[:k]
    category_count = Counter([category for category, _ in nearest_neighbors])

    return category_count.most_common(1)[0][0]


def main():
    filename = input("Enter the CSV filename containing the data: ")
    label_column = input("Enter the name of the column for classification: ")
    k = int(input("Enter the value of k: "))
    target_height = float(input("Enter the numper to calculate distance for: "))

    data = read_data_from_csv(filename, label_column)
    result = knn(k, data, [target_height])

    print(f"\n {target_height} is classified as: {result}")


if __name__ == "__main__":
    main()
