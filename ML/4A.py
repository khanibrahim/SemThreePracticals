#A. For a given set of training data examples stored in a .CSV file implement Least Square Regression algorithm.(Use Univariate dataset)

importpandasaspd
importnumpyasnp
importmatplotlib.pyplotasplt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Lea
# from sklearn.metrics import confusion_matrix, accuracy_score
plt.rcParams['figure.figsize']=(12.0,9.0)
dataset =
pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/di
abetes.csv")
print(dataset.head())
x = dataset.iloc[:,0]
y = dataset.iloc[:,1]
plt.scatter(x, y)
plt.show()
x_mean = np.mean(x)
y_mean = np.mean(y)
num = 0
den = 0
foriinrange(len(x)):
num += (x[i] -x_mean)*(y[i]-y_mean)
den += (x[i] -x_mean)**2
m = num/den
c = y_mean - m*x_mean
print(m,c)
y_pred = m*x +c
plt.scatter(x,y)
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color="red")
plt.show()