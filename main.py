
#This project include KNN as a learning methoden , trying ANN  is not useful because dataset is not a enough large for learning
#however fluctation is still biggest problem against to learning
#but when we consider the data after fluctuation,



import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from clients import client1, client2, client3, client4, client5, client6 ,client7, client8


import clientController
import time

global a_dict
a_dict = {}


def print_hi(name):
    i = 0
    for i in range(5):
        print(f'Hi, {name}')

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #clients running same time
    clientController.method_1()

    #waiting to done clients process
    time.sleep(127)

    #after client process,we have 8 dic. so searching the common key in per dictionary
    #and create new dict. with this common key's values
    for key in client1.keyMapDict:
        if key in client2.keyMapDict and key in client3.keyMapDict and key in client4.keyMapDict and key in client5.keyMapDict \
                 and key in client6.keyMapDict and key in client7.keyMapDict and key in client8.keyMapDict:
            a_dict[key] = [client1.keyMapDict[key], client2.keyMapDict[key], client3.keyMapDict[key],
                           client4.keyMapDict[key], client5.keyMapDict[key],client6.keyMapDict[key],
                           client7.keyMapDict[key], client8.keyMapDict[key]]
    print("\033[1;34;40m Bright Blue \n")
    print(a_dict)

    #KNN algorithm is running on datasets

    PavoDataset = pd.read_csv('datasets/dataset1.csv')
    # print(PavoDataset.head(6))
    # print(PavoDataset.describe())
    location = PavoDataset['location2'][:]
    # print(location.head(6))

    X = PavoDataset.drop(['location2', 'location1','location3'], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, location, test_size=0.10)

    knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski')

    knn.fit(X_train, y_train)

    #for the frontend progress,we have to clean xyz.txt
    open('xyz.txt', 'w')

    #with the mapping methoden,prediction operation is going from big to small

    def predictData():
        values = []
        for key in a_dict:

            asd = a_dict[key]
            va = knn.predict(list([asd]))
            print("2) Using K Neighbors Classifier Prediction is " + str(key) + str(va))

            if va == 1:
                PavoDataset = pd.read_csv('datasets/1.csv')
                location1 = PavoDataset['location1'][:]
                X = PavoDataset.drop(['location2', 'location1'], axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
                knn1 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
                knn1.fit(X_train, y_train)
                asd = a_dict[key]
                va1 = knn1.predict(list([asd]))
                print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va1))
                with open("xyz.txt", 'a') as output:
                    output.write(str(key) + "," + str(va1) + "\n")


            elif va == 2:
                PavoDataset = pd.read_csv('datasets/2.csv')
                location1 = PavoDataset['location1'][:]
                X = PavoDataset.drop(['location2', 'location1'], axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
                knn2 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
                knn2.fit(X_train, y_train)
                asd = a_dict[key]
                va2 = knn2.predict(list([asd]))
                print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va2))

                with open("xyz.txt", 'a') as output:
                    output.write(str(key) + "," + str(va2) + "\n")
            elif va == 3:
                PavoDataset = pd.read_csv('datasets/3.csv')
                location1 = PavoDataset['location1'][:]
                X = PavoDataset.drop(['location2', 'location1'], axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
                knn3 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
                knn3.fit(X_train, y_train)
                asd = a_dict[key]
                va3 = knn3.predict(list([asd]))
                print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va3))
                with open("xyz.txt", 'a') as output:
                    output.write(str(key) + "," + str(va3) + "\n")
            else:
                PavoDataset = pd.read_csv('datasets/4.csv')
                location1 = PavoDataset['location1'][:]
                X = PavoDataset.drop(['location2', 'location1'], axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, location1, test_size=0.10)
                knn4 = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
                knn4.fit(X_train, y_train)
                asd = a_dict[key]
                va4 = knn4.predict(list([asd]))
                print("1) Using K Neighbors Classifier Prediction is " + str(key) + str(va4))
                with open("xyz.txt", 'a') as output:
                    output.write(str(key) + "," + str(va4) + "\n")


    predictData()
    time.sleep(5)
    import frontend

    flag=False

    while True:
        if flag==True:
            break

    print("#############################################################################")
