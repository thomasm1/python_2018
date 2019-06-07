# Support Vector Regression
## y = mx + b
## Solution: min(1/2)||w||^2
## Constraints: yi-wxi-b <= epsilon
##            : wxi + b-yi <= epsilon

import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

a = np.arange(0, 5, 0.1)
b = np.sin(a)
plt.plot(a, b)

dates = []
prices = []


#plt.switch_backend('newbackend')  

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_len = SVR(kernel= 'linear', C=1e3, gamma='auto')
    svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2, gamma='auto')
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma='auto')
    
    svr_len.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_len.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_len.predict(x)[0], svr_poly.predict(x)[0]

get_data('AAPL.csv')

predicted_price = predict_prices(dates, prices, 29)

print(predicted_price) 
    
