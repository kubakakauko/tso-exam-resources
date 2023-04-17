import pandas as pd

def naive_bayes_classifier(data, test_sample):
    target = data.columns[-1]
    target_classes = data[target].unique()

    priors = {}
    for t_class in target_classes:
        priors[t_class] = len(data[data[target] == t_class]) / len(data)

    conditional_probs = {}
    for t_class in target_classes:
        class_data = data[data[target] == t_class]
        class_probs = {}
        for feature, value in test_sample.items():
            class_probs[feature] = len(class_data[class_data[feature] == value]) / len(class_data)
        conditional_probs[t_class] = class_probs

    posterior_probs = {}
    for t_class, class_probs in conditional_probs.items():
        posterior_prob = priors[t_class]
        for feature_prob in class_probs.values():
            posterior_prob *= feature_prob
        posterior_probs[t_class] = posterior_prob

    print("Priors:", priors)
    print("Conditional Probabilities:", conditional_probs)
    print("Posterior Probabilities:", posterior_probs)

    prediction = max(posterior_probs, key=posterior_probs.get)
    return prediction


if __name__ == "__main__":
    # Read dataset from CSV file
    dataset = pd.read_csv("dataset.csv")

    # Test sample
    test_sample = {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "High", "Wind": "Weak"}

    prediction = naive_bayes_classifier(dataset, test_sample)
    print("Prediction for the test sample:", prediction)
