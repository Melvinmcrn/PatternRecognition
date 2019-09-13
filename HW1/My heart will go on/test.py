import pandas as pd
import numpy as np

# def T7T8():
    # print(train)

    # print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(train["Age"].mode()[0])
    # train["Age"] = train["Age"].fillna(train["Age"].mode()[0])
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(train["Age"].mode()[0])
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    # train.loc[train["Embarked"] == "S", "Embarked"] = 0
    # train.loc[train["Embarked"] == "C", "Embarked"] = 1
    # train.loc[train["Embarked"] == "Q", "Embarked"] = 2
    # print(train["Embarked"].mode())
    # train["Embarked"] = train["Embarked"].fillna(train["Embarked"].mode()[0])
    # print(train["Embarked"].mode())
    # print("************************************************")

    # train.loc[train["Sex"] == "male", "Sex"] = 0
    # train.loc[train["Sex"] == "female", "Sex"] = 1
    # print(train["Sex"].mode())
    # train["Sex"] = train["Sex"].fillna(train["Sex"].mode()[0])
    # print(train["Sex"].mode())
    # print("************************************************")

    # print(train)

def h(x,a):
    c = -1 * np.dot(a.T, x)
    return 

def T9():

    train.loc[train["Embarked"] == "S", "Embarked"] = 0
    train.loc[train["Embarked"] == "C", "Embarked"] = 1
    train.loc[train["Embarked"] == "Q", "Embarked"] = 2

    train.loc[train["Sex"] == "male", "Sex"] = 0
    train.loc[train["Sex"] == "female", "Sex"] = 1

    train["Pclass"] = train["Pclass"].fillna(train["Pclass"].median())
    train["Sex"] = train["Sex"].fillna(train["Sex"].median())
    train["Age"] = train["Age"].fillna(train["Age"].median())
    train["Embarked"] = train["Embarked"].fillna(train["Embarked"].median())

    data = np.array(train[["Pclass","Sex","Age","Embarked"]].values)
    print(data)

    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    data = np.array(train[["Pclass","Sex","Age","Embarked"]].values, dtype = float)
    print(data[:,0])


train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url) #training set

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
#test = pd.read_csv(test_url) #test set
#print(train)
print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
T9()
#print(test)