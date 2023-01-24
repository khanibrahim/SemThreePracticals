# Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis
# based on a givenset of training data samples. Read the training data from a .CSV file.

import csv
num_attributes = 6
dataset = []
with open(r"Dataset.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
for row in reader:
    dataset.append(row)
print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)
for j in range(0, num_attributes):
    hypothesis[j] = dataset[1][j]
print("\n Find S: Finding a Maximally Specific Hypothesis")
for i in range(1, len(dataset)):
    if dataset[i][num_attributes] == 'Yes':
        for j in range(0, num_attributes):
            if dataset[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = dataset[i][j]
print("For Training instance no:{0} the hypothesis is ".format(i), hypothesis)
print("\n The Maximally Specific Hypothesis for a given training examples:\n")
print(hypothesis)