import math

def entropy(p, q):
    if p == 0 or q == 0:
        return 0
    return -p * math.log2(p) - q * math.log2(q)

def information_gain(e_s, pairs):
    weighted_avg_entropy = sum(p * e for p, e in pairs)
    return e_s - weighted_avg_entropy

def get_attribute_info():
    yes_samples = int(input("Enter the number of YES samples: "))
    no_samples = int(input("Enter the number of NO samples: "))
    return yes_samples, no_samples

def calculate_entropy(yes_samples, no_samples):
    total_samples = yes_samples + no_samples
    return entropy(yes_samples / total_samples, no_samples / total_samples)

def main():
    num_attributes = int(input("Enter the number of attributes: "))

    # Get target attribute YES and NO samples
    target_yes_samples = int(input("Enter the number of YES samples for the target attribute: "))
    target_no_samples = int(input("Enter the number of NO samples for the target attribute: "))
    e_s = calculate_entropy(target_yes_samples, target_no_samples)

    for i in range(num_attributes):
        print(f"\nAttribute {i + 1}")
        attribute_name = input("Enter the name of the attribute: ")

        num_values = int(input(f"Enter the number of values for {attribute_name}: "))
        value_pairs = []

        for j in range(num_values):
            print(f"\nValue {j + 1}")
            value_name = input("Enter the name of the value: ")

            yes_samples, no_samples = get_attribute_info()
            e_value = calculate_entropy(yes_samples, no_samples)
            weight = (yes_samples + no_samples) / (target_yes_samples + target_no_samples)

            value_pairs.append((weight, e_value))

            print(f"Entropy({attribute_name} = {value_name}) = {e_value:.4f}")

        gain = information_gain(e_s, value_pairs)
        print(f"Information Gain for {attribute_name}: {gain:.4f}")

if __name__ == "__main__":
    main()
