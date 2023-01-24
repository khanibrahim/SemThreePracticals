#Write a program to implement Decision Tree and Random Forest with Prediction, Test Score and Confusion Matrix

# Decision tree
importpandasaspd
fromsklearn,.model_selectionimporttrain_test_split
fromsklearn.treeimportDecisionTreeClassifier

fromsklearn.metricsimportconfusion_
matrix, accuracy
score,
classification_report

import warnings

warnings.filterwarnings('ignore')

# Read Datasets

defread_datasets():

datasets = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-
databases / balance - scale / balance - scale.data
",

» header = None)



print(£"Dataset Length : {len (datasets) }")
print(£"Dataset Shape: {datasets.shape}")
print(f"Datasets : {datasets.head()}")
returndatasets

# Spliting Datasets into train and test

defsplitdataset(datasets):

X = datasets.values[:, 1:5]

Y

0

datasets.values[:, 0]

X
train, X
test, y
train, y
test = train
test_split(x, Y, test_size= |
random_state = 100)

a

# print (€"x train: (Xx train}\n x test: {x _test}\n y trail
y_test: {y_test}
")

: {y_train)\n

returnX_train, X_test, y_train, y
test

deftrain_using_gini(x_train, y
train):



clf_gini = DecisionTreeClassifier(criterion
                                  , min_samples_leaf=5)

gini
', random _state=100,

clf_gini.fit(x_train, y
train)
returnelf_gini
deftrain_using_entropy(x_train, y
train):

clf_entropy = DecisionTreeClassifier(criterion='entropy',

                                     random_state=100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(x_train, y
train)

returnclf_entropy

defprediction(x_test, clf_object):

y_pred = clf_object.predict(x_test)

print(£"Predicted values: {y_pred}")

returny_pred

defcal_accuracy(y_test, y_pred):

print(£"Confusion Metrix :{confusion_matrix(y_test, y_pred)}"
print(f"Accuracy: {accuracy _score(y test, y_pred) * 100}")
print(£"Report: {classification_report (y_test, y_pred)}"
defmain():

datasets = read_datasets()

X_train, X_test, y
train, y_test = splitdataset(datasets)
clf_gini = train_using_gini(x_train, y_train)

clf_entropy = train_using_entropy(x_train, y
train)

print("Results using Gini Index

y_pred_gini = prediction(x_test, clf_gini)
cal_accuracy(y
test, y_pred_gini)

print("Results using Entropy Index: "

y_pred_entropy = prediction(x_test, clf_entropy)

cal_accuracy(y_test, y_pred_entropy

if__name
main__
":

main()
