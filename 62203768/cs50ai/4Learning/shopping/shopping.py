import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    # Passes path to file as a string, empty string as newline to handle empty rows, as keyword gives csv resource a name
    with open(filename, newline='') as csv_file:
        # To load the contents of the csv file in dictionary format, use a DictReader object. Pass the csv resource to the constructor and assign the results to a variable called reader.
        reader = csv.DictReader(csv_file)
        # The DictReader object will read the csv resource and map each row to a dictionary.

        # Initiate lists to hold data
        evidence = []
        labels = []

        # Sort months into dictionary
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_number = enumerate(months)
        month = {k: v for v, k in month_number}

        # Loop over data and add to evidence and labels lists
        for row in reader:
            # evidence
            data = []

            data.append(int(row["Administrative"]))
            data.append(float(row["Administrative_Duration"]))
            data.append(int(row["Informational"]))
            data.append(float(row["Informational_Duration"]))
            data.append(int(row["ProductRelated"]))
            data.append(float(row["ProductRelated_Duration"]))
            data.append(float(row["BounceRates"]))
            data.append(float(row["ExitRates"]))
            data.append(float(row["PageValues"]))
            data.append(float(row["SpecialDay"]))
            data.append(int(month[row["Month"]]))
            data.append(int(row["OperatingSystems"]))
            data.append(int(row["Browser"]))
            data.append(int(row["Region"]))
            data.append(int(row["TrafficType"]))
            data.append(int(row["VisitorType"]))        # ????
            data.append(int(row["Weekend"] == "TRUE"))

            evidence.append(data)

            # labels
            if not row["Revenue"]:
                labels.append([0])
            else:
                labels.append([1])

        return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    negative = 0
    true_neg = 0

    for i in range(len(labels)):
        if labels[i] == 0:
            if labels[i] == predictions[i]:
                true_neg += 1
            else:
                negative += 1
        else:
            


if __name__ == "__main__":
    main()
