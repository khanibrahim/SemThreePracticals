#A. Implement the different Distance methods (Euclidean, Manhattan Distance, Minkowski Distance) withPrediction, Test Score and Confusion Matrix.

frommathimportsqrt
fromsklearn.metricsimportconfusion_matrix, classification_report
defeuclidian_distance(a, b):
returnsqrt(sum((e1 - e2) ** 2fore1, e2inzip(a, b)))
defmanhattan_distance(a, b):
returnsum(abs(e1 - e2) fore1, e2inzip(a, b))
defminkowski_distance(a, b, p):
returnsum(abs(e1 - e2) ** pfore1, e2inzip(a, b)) ** (1 / p)
actual = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
predicted = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
dist1 = euclidian_distance(actual, predicted)
dist2 = manhattan_distance(actual, predicted)
dist3 = minkowski_distance(actual, predicted, 1)
print(f"Euclidian_dist: {dist1}\nManhattan_dist: {dist2}\nMinkowski_dist
with value 1: {dist3}")
dist4 = minkowski_distance(actual, predicted, 2)
print(f"Minkowski_dist with value 2: {dist4}\n")
matrix = confusion_matrix(actual, predicted, labels=[1, 0])
print("Confusion_matrix: \n", matrix)
tp, fn, fp, tn = confusion_matrix(actual, predicted, labels=[1,
0]).reshape(-1)
print("Outcome values: \n", tp, fn, fp, tn)
matrix = classification_report(actual, predicted, labels=[1, 0])
print("Classification_report: \n", matrix)
