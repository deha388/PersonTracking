# project is in the localhost
# so database connection is not using for now

import time

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# some_dict={35: [177.2, 178.0, 183.6, 177.2, 182.6], 89: [188.8, 185.8, 181.0, 190.0, 193.0], 92: [196.0, 196.0, 190.6, 191.2, 194.8], 267: [184.0, 177.2, 173.5, 174.6, 182.2]}
some_dict = {35: [183.0, 181.8, 188.0, 179.8, 182.0, 177.0, 185.2, 179.6, 172.0],
             268: [196.6, 181.6, 191.2, 200.2, 201.4, 202.0, 185.2, 201.4, 192.4],
             275: [195.8, 176.0, 176.8, 181.0, 188.8, 186.8, 185.8, 181.6, 181.8],
             277: [184.0, 201.4, 186.4, 182.2, 190.6, 179.0, 194.2, 184.0, 176.8],
             284: [175.0, 175.0, 175.0, 184.75, 175.0, 173.8, 175.0, 173.8, 179.8],
             293: [187.0, 187.0, 186.4, 189.4, 188.2, 196.6, 183.4, 194.2, 179.8],
             326: [183.25, 177.0, 178.0, 185.5, 192.25, 187.0, 190.0, 194.2, 183.25],
             335: [185.8, 175.0, 181.0, 185.2, 179.8, 190.6, 179.8, 186.4, 181.6],
             341: [175.0, 172.0, 174.0, 172.33333333333334, 176.0, 176.5, 172.75, 175.75, 178.0],
             389: [187.0, 179.0, 181.0, 187.6, 193.0, 185.8, 187.0, 187.0, 181.0],
             412: [181.0, 185.8, 181.0, 178.75, 185.5, 190.0, 184.0, 195.0, 185.0],
             417: [186.0, 195.4, 193.6, 183.0, 194.8, 193.0, 191.2, 185.8, 182.5],
             440: [188.8, 185.8, 183.0, 185.8, 192.0, 190.4, 187.4, 197.0, 195.4],
             471: [191.2, 187.0, 185.8, 184.6, 188.8, 197.8, 183.4, 195.4, 195.4],
             483: [192.4, 193.0, 194.71428571428572, 185.8, 185.2, 188.8, 191.8, 190.6, 185.8],
             486: [180.4, 191.8, 192.4, 182.2, 183.4, 185.8, 193.0, 183.4, 178.0],
             488: [185.8, 178.75, 178.0, 188.2, 195.4, 182.8, 185.8, 179.0, 184.6],
             495: [184.0, 191.8, 186.4, 187.6, 185.8, 183.4, 194.8, 187.0, 179.2],
             1009: [187.0, 176.6, 180.8, 183.0, 187.6, 190.0, 179.6, 180.8, 187.8],
             1015: [181.0, 181.0, 178.0, 169.0, 187.6, 177.4, 179.8, 177.4, 181.6],
             1111: [194.8, 185.8, 184.0, 198.4, 196.0, 195.4, 189.0, 186.4, 200.8],
             1683: [175.0, 175.0, 169.0, 175.0, 174.4, 172.0, 175.0, 175.0, 172.0],
             1760: [182.2, 180.4, 180.4, 181.0, 187.0, 185.8, 179.8, 195.4, 183.4],
             1772: [188.8, 184.0, 182.8, 190.0, 189.4, 193.0, 179.8, 195.4, 186.4],
             1779: [191.8, 185.2, 177.4, 185.8, 189.4, 190.0, 187.0, 195.4, 185.8],
             1921: [192.25, 188.2, 182.2, 190.6, 193.0, 191.8, 183.4, 192.4, 179.8],
             1922: [191.2, 196.6, 185.8, 179.8, 193.0, 191.0, 197.2, 183.4, 181.0],
             2254: [200.2, 183.0, 185.8, 191.8, 200.8, 197.8, 185.8, 191.0, 202.0],
             2255: [185.5, 175.0, 175.0, 173.8, 188.8, 183.4, 177.4, 176.2, 178.0],
             2261: [191.2, 186.25, 179.8, 185.8, 196.6, 192.4, 186.4, 203.2, 196.0],
             2262: [189.25, 192.25, 188.2, 192.4, 192.4, 183.4, 184.0, 194.8, 194.8],
             2265: [195.4, 191.2, 184.0, 204.4, 191.8, 196.0, 191.2, 200.8, 199.0],
             2290: [190.6, 191.2, 181.0, 202.6, 197.2, 196.6, 181.6, 194.2, 188.8],
             2323: [192.0, 188.8, 177.4, 200.8, 193.6, 187.6, 185.8, 193.6, 194.8],
             2335: [193.0, 191.8, 184.6, 184.75, 186.4, 184.0, 190.6, 178.0, 182.2],
             2340: [195.0, 184.6, 182.0, 192.4, 196.6, 193.6, 188.2, 199.6, 184.0],
             2352: [195.4, 178.0, 175.0, 182.8, 199.0, 186.4, 179.8, 183.4, 181.0],
             2367: [186.0, 193.2, 195.6, 184.0, 184.6, 182.8, 196.0, 184.2, 184.0],
             2372: [180.4, 181.0, 186.4, 176.2, 176.2, 173.5, 185.2, 178.0, 175.0],
             2374: [178.0, 192.4, 183.4, 181.0, 185.8, 185.2, 193.0, 179.8, 178.0],
             2530: [195.4, 179.8, 185.8, 208.0, 195.4, 193.6, 183.4, 191.5, 194.2],
             2531: [189.4, 187.0, 184.0, 204.4, 199.6, 187.6, 188.2, 194.2, 196.6],
             2549: [197.2, 194.8, 179.8, 201.4, 190.0, 196.0, 187.0, 192.4, 192.4],
             2576: [200.2, 195.4, 190.0, 205.0, 199.0, 193.6, 198.4, 199.0, 199.6],
             2578: [187.0, 187.6, 184.0, 185.8, 188.2, 190.0, 184.42857142857142, 196.0, 181.6],
             2587: [196.6, 192.4, 192.4, 201.4, 191.8, 195.4, 193.0, 194.2, 196.6],
             2674: [196.6, 192.4, 187.75, 208.0, 189.4, 191.2, 192.4, 199.0, 196.85714285714286],
             2728: [197.8, 191.8, 187.75, 202.6, 195.4, 195.4, 198.0, 201.4, 196.6],
             2857: [189.4, 186.4, 182.2, 179.8, 185.2, 185.8, 190.0, 178.0, 185.8],
             2890: [187.0, 190.0, 186.4, 180.4, 183.4, 185.8, 185.8, 187.6, 184.0],
             2891: [191.2, 191.8, 191.2, 189.4, 192.4, 189.4, 185.8, 188.8, 186.4],
             2979: [191.8, 185.8, 178.0, 193.6, 194.71428571428572, 192.4, 183.4, 191.8, 196.6],
             2987: [192.4, 192.4, 184.0, 204.4, 193.0, 202.0, 195.4, 198.4, 198.4],
             3074: [181.0, 187.0, 187.75, 178.0, 180.4, 181.0, 193.0, 175.0, 179.0],
             3075: [188.8, 179.8, 179.8, 185.8, 199.0, 187.0, 185.8, 187.0, 175.0],
             3080: [197.2, 175.0, 179.8, 188.2, 192.4, 193.0, 181.0, 179.8, 186.0],
             3092: [192.4, 179.8, 177.25, 182.8, 190.0, 182.5, 179.8, 182.2, 179.2],
             3100: [195.4, 191.8, 185.2, 213.2, 193.6, 195.4, 199.0, 196.6, 202.6],
             3130: [193.75, 188.0, 187.0, 190.6, 199.0, 194.2, 196.0, 199.0, 187.75],
             3133: [177.6, 189.6, 189.2, 178.6, 180.6, 180.8, 184.6, 180.6, 177.4],
             3147: [188.2, 192.4, 197.2, 185.8, 200.8, 189.4, 187.6, 184.6, 178.0],
             3150: [185.8, 193.6, 187.0, 186.4, 187.0, 190.0, 191.8, 185.2, 181.0],
             3155: [182.2, 188.2, 181.0, 185.8, 185.8, 183.4, 185.8, 183.4, 179.8],
             3158: [191.8, 195.4, 195.4, 185.8, 193.0, 194.2, 195.25, 184.0, 183.4],
             3169: [181.0, 179.8, 186.4, 172.75, 178.0, 178.6, 191.2, 178.0, 181.0],
             3237: [186.4, 185.8, 179.8, 185.8, 181.6, 185.8, 185.8, 187.0, 179.8],
             3242: [185.8, 193.6, 185.8, 184.0, 185.2, 191.2, 187.0, 182.8, 179.8],
             3250: [186.4, 186.4, 187.0, 187.0, 191.2, 190.0, 186.0, 185.8, 187.0],
             3290: [175.0, 175.0, 175.0, 175.0, 175.75, 175.0, 175.0, 180.4, 179.8],
             3291: [191.8, 197.2, 189.4, 196.0, 190.0, 199.0, 190.6, 204.4, 197.2],
             3307: [194.2, 176.5, 182.2, 185.2, 190.0, 192.4, 189.4, 193.0, 184.75],
             3356: [194.2, 187.6, 179.5, 200.0, 197.2, 192.4, 186.4, 194.2, 197.8],
             3365: [201.4, 187.6, 182.2, 188.8, 195.4, 193.0, 184.6, 191.8, 197.2],
             3396: [177.4, 180.25, 182.0, 179.8, 182.2, 179.2, 182.5, 179.8, 187.0],
             3397: [193.6, 181.0, 184.0, 180.4, 197.2, 196.6, 176.2, 185.8, 185.2],
             3398: [176.8, 177.4, 178.0, 176.4, 179.2, 181.0, 179.2, 178.8, 175.6],
             3499: [184.0, 179.0, 175.0, 181.0, 182.0, 177.0, 189.0, 179.0, 178.0],
             3638: [185.0, 191.8, 191.8, 183.4, 187.0, 192.4, 187.6, 183.4, 183.4],
             3721: [186.4, 185.8, 192.4, 179.8, 185.2, 185.2, 184.0, 185.0, 180.4],
             3974: [187.6, 185.8, 182.2, 185.2, 197.2, 194.8, 180.4, 202.8, 187.6],
             4089: [201.4, 177.4, 178.0, 185.8, 195.4, 192.4, 182.2, 190.42857142857142, 184.0],
             4092: [200.2, 193.6, 188.8, 193.6, 196.6, 200.2, 188.2, 199.125, 187.0],
             4291: [182.8, 185.8, 191.2, 179.0, 181.0, 175.0, 191.2, 175.6, 173.8],
             4305: [173.8, 176.2, 186.4, 179.4, 175.6, 175.25, 184.0, 177.6, 171.6],
             9220: [186.0, 194.0, 181.0, 197.0, 189.0, 186.5, 187.5, 199.0, 186.0]}

PavoDataset = pd.read_csv('datasets/dataset2.csv')
# print(PavoDataset.head(6))
# print(PavoDataset.describe())
location = PavoDataset['location4'][:]
# print(location.head(6))

X = PavoDataset.drop(['location2', 'location1', 'location3', 'location4'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, location, test_size=0.10)

knn = KNeighborsClassifier(n_neighbors=3, metric='minkowski')

knn.fit(X_train, y_train)

open('xyz.txt', 'w')


def predictData():
    values = []
    for key in some_dict:
        asd = some_dict[key]
        va = knn.predict(list([asd]))
        print("2) Using K Neighbors Classifier Prediction is " + str(key) + "     " + str(va))

        # if va == 1:
        #     PavoDataset = pd.read_csv('datasets/1.csv')
        #     location1 = PavoDataset['location1'][:]
        #     X = PavoDataset.drop(['location2', 'location1'], axis=1)
        #     X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
        #     knn1 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
        #     knn1.fit(X_train, y_train)
        #     asd = some_dict[key]
        #     va1 = knn1.predict(list([asd]))
        #     print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va1))
        #     with open("xyz.txt", 'a') as output:
        #         output.write(str(key) + "," + str(va1) + "\n")
        #
        #
        # elif va == 2:
        #     PavoDataset = pd.read_csv('datasets/2.csv')
        #     location1 = PavoDataset['location1'][:]
        #     X = PavoDataset.drop(['location2', 'location1'], axis=1)
        #     X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
        #     knn2 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
        #     knn2.fit(X_train, y_train)
        #     asd = some_dict[key]
        #     va2 = knn2.predict(list([asd]))
        #     print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va2))
        #
        #     with open("xyz.txt", 'a') as output:
        #         output.write(str(key) + "," + str(va2) + "\n")
        # elif va == 3:
        #     PavoDataset = pd.read_csv('datasets/3.csv')
        #     location1 = PavoDataset['location1'][:]
        #     X = PavoDataset.drop(['location2', 'location1'], axis=1)
        #     X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
        #     knn3 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
        #     knn3.fit(X_train, y_train)
        #     asd = some_dict[key]
        #     va3 = knn3.predict(list([asd]))
        #     print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va3))
        #     with open("xyz.txt", 'a') as output:
        #         output.write(str(key) + "," + str(va3) + "\n")
        # else:
        #     PavoDataset = pd.read_csv('datasets/4.csv')
        #     location1 = PavoDataset['location1'][:]
        #     X = PavoDataset.drop(['location2', 'location1'], axis=1)
        #     X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
        #     knn4 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
        #     knn4.fit(X_train, y_train)
        #     asd = some_dict[key]
        #     va4 = knn4.predict(list([asd]))
        #     print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va4))
        #     with open("xyz.txt", 'a') as output:
        #         output.write(str(key) + "," + str(va4) + "\n")


predictData()

time.sleep(5)

import frontend
