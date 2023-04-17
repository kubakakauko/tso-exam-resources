# tso-exam-resources

# Information Gain Calculator
Make sure to update the path to your dataset and the name of your target column. After that run the python file.
`python3 IGCalculator.py`

E.G Question 4.a 2020-21 sample input
The input required for this code to compute the Information Gain for the given question is as follows:

    Enter the number of attributes: 2 (Temperature and Humidity)
    Enter the number of YES samples for the target attribute: 9 (Play Tennis: Yes)
    Enter the number of NO samples for the target attribute: 5 (Play Tennis: No)

For the "Temperature" attribute:

    Attribute 1
    Enter the name of the attribute: Temperature
    Enter the number of values for Temperature: 3 (Hot, Mild, Cool)

For each value of the "Temperature" attribute, you'll need to provide the count of YES and NO samples for that value. You should calculate these counts from the dataset provided.

For the "Humidity" attribute:

    Attribute 2
    Enter the name of the attribute: Humidity
    Enter the number of values for Humidity: 2 (High, Normal)

Again, for each value of the "Humidity" attribute, you'll need to provide the count of YES and NO samples for that value. You should calculate these counts from the dataset provided.

Please note that this code only calculates the Information Gain for a given set of input values. You will still need to compute the counts for YES and NO samples of each attribute value from the dataset.


# Euclidean Distance Calculator

Create a CSV file with the given
`
Identifier,Adult/Child,Height (cm)
1,Adult,170.7
2,Child,155.6
3,Child,165.3
3,Adult,175.2
5,Adult,147.3
6,Child,150.2
`

Run the code
`
$ python EuclideanDistance.py
Enter the CSV filename containing the data: 
Enter the value of k: 
Enter the vaplue to find euclideandist for: 
`
