#Fatima shrateh- Jihan Alshafie- Hedaya Mustafa
# Automatic tweet spam detection Project
#-----------------------LIBRARIES----------------------------
import os
import tkinter
import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
import sklearn.neural_network
import matplotlib.pyplot as plt
import sklearn.model_selection
import re
import sys
from nltk.stem.porter import PorterStemmer
import numpy as geek
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot

###############################################################
from sklearn.tree import export_graphviz
import graphviz
from IPython.display import Image
import pydotplus
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from six import StringIO
from IPython.display import Image
import pydotplus

##################################################################
# Welcome window interface
welcome = Tk()
# login window settings
welcome.geometry('390x430')
welcome.title(' AI_2022 ')
welcome.resizable(0, 0)

#---------------------READ FILE--------------------------
twitterData = pd.read_csv('train.csv')
print(twitterData.isnull().sum())                   # find the null cells in all columns
#---------------------------------------CLEAN DATA------------------------------------
# Function to clean Tweet coulmn by removing punctuation , stop words , etc. ...
def clean_data(Tweet):

    tweetlower = Tweet.lower() # Convert to lower case
    #this method from library re to remove the URLs from the column tweet
    CleanData = re.sub(r'((www\.[\S]+)|(https?:\/\/\S+))', '',tweetlower)
    #here we removed the punctuation from tweets
    withoutpunctuation = [char for char in CleanData if char not in string.punctuation]
    withoutpunctuation = ''.join(withoutpunctuation) #replace the punctuation with space

    replace2dots = re.sub(r'\.{2,}','', withoutpunctuation)#Replace 2+ dots with space
    without_quotetion = replace2dots.strip(' "\'')# Strip space, " and ' from tweet

    # Convert more than 2 letter repetitions to 2 letter
    # Happpppy --> Happy
    withoutrepetitions = re.sub(r'(.)\1+', r'\1\1', without_quotetion)

    # Replace multiple spaces with a single space
    multiple_spaces = re.sub(r'\s+', ' ', withoutrepetitions)
    #remove stopwords from tweets
    without_stop_words = [word for word in multiple_spaces.split() if word.lower() not in stopwords.words('english')]

    return without_stop_words
#------------------------------------------------------------------------------------------
print(twitterData['Tweet'].head().apply(clean_data))
#convert each tweet to tokens and count them and represent these tokens as vectors
tweet_token = CountVectorizer(analyzer=clean_data).fit_transform(twitterData['Tweet'])
print(tweet_token)
print("============================")
twitterData['actions'] = twitterData.actions.fillna(twitterData.actions.mean())
print(twitterData['actions'])
twitterData['followers'] = twitterData.followers.fillna(twitterData.followers.mean())
#-----------------------------------------------------------------------------------
#Drop the coulmns that we don't need
features = twitterData.drop(columns = ['Id','following', 'is_retweet', 'location','Type'])
#we give 20% for testing, 80% for training
x_train, x_test, y_train, y_test = train_test_split(features,twitterData['Type'], test_size=0.20, random_state=0)

#------------------------------------------------------------------------------------------
#function for the interface of naive bayes to let user choose train data or test data
def test_train_naiveBayes():
    tt1 = Tk()
    # login window settings
    tt1.geometry('200x130')
    tt1.title(' Naive Bayes ')
    tt1.resizable(0, 0)
    gradientttt(tt1)

    test1 = Button(tt1, width=20, height=2, text="Train", bg="#E87C43", fg="white", command=naiveBayes_Train)
    test1.pack()
    test1.place(x=20, y=15)

    test2 = Button(tt1, width=20, height=2, text="Test",bg = "#E87C43",fg = "white", command=naiveBayes_Test)
    test2.pack()
    test2.place(x=20, y=70)

#function to train the datat using naive bayes classifier and show it in an interface as an accuracy and report
def naiveBayes_Train():
    nb = Tk()
    # login window settings
    nb.geometry('500x550')
    nb.title(' Naive Bayes Train')
    nb.resizable(0, 0)
    gradientttt(nb)

    # use ready clasifier from naive bayes
    naive_bayes = MultinomialNB().fit(x_train, y_train)
    #print(naive_bayes.predict_proba(x_test[:5]))


    predicted_values1 = naive_bayes.predict(x_train)  # predicted value (x)
    print(predicted_values1)
    #print the accuracy of Train data
    accuracyy = Label(nb, text=f'classifier Accuracy {accuracy_score(y_train,predicted_values1)}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)
    #print performance report of train data
    report = Label(nb, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(nb, text=f"{classification_report(y_train, predicted_values1)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)
    # print the confusion matrix
    confmat = Label(nb, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(nb, text=f"{confusion_matrix(y_train,predicted_values1)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)

# Function to test the datat using naive bayes classifier
def naiveBayes_Test():
    nb1 = Tk()
    # login window settings
    nb1.geometry('500x550')
    nb1.title(' Naive Bayes Test ')
    nb1.resizable(0, 0)
    gradientttt(nb1)

    # use ready clasifier from naive bayes
    naive_bayes = MultinomialNB().fit(x_train, y_train)
    predicted_values1 = naive_bayes.predict(x_test)  # predicted value (x)
    print(f"predict values{predicted_values1}")
    # print accuracy for test data
    accuracyy = Label(nb1, text=f'classifier Accuracy {accuracy_score(y_test, predicted_values1)}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)
    # print report for test data
    report = Label(nb1, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(nb1, text=f"{classification_report(y_test, predicted_values1)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)
    # print confusion matrix for test data
    confmat = Label(nb1, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(nb1, text=f"{confusion_matrix(y_test,predicted_values1)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
# --------------------------------------------------------------------------------------------------------------------
# function to let the user choose from an interface tran data or test data of Decision tree
def test_train_DecisionTree():
    tt2 = Tk()
    # login window settings
    tt2.geometry('200x130')
    tt2.title(' Decision Tree ')
    tt2.resizable(0, 0)
    gradienttt(tt2)

    test1 = Button(tt2, width=20, height=2, text="Train", bg="#E87C43", fg="white", command=DecisionTree_Train)
    test1.pack()
    test1.place(x=20, y=15)

    test2 = Button(tt2, width=20, height=2, text="Test",bg = "#E87C43",fg = "white", command=DecisionTree_Test)
    test2.pack()
    test2.place(x=20, y=70)
# evaluate decision tree performance on train and test sets with different tree depths
# function to test the data using decision tree and plot the tree graph
def DecisionTree_Test():
    dt = Tk()
    # login window settings
    dt.geometry('500x550')
    dt.title(' Decision Tree Test')
    dt.resizable(0, 0)
    gradienttt(dt)    #color the background of the interface

    # define lists to collect scores to find the fittness of the classifier
    train_scores, test_scores = list(), list()
    # define the tree depths to evaluate
    values = [i for i in range(1, 30)]
    # evaluate a decision tree for each depth
    for i in values:

        # use Decision Tree Classifier
        decision_tree = DecisionTreeClassifier(max_depth=i)
        decision_tree.fit(x_train, y_train)
        predicted_values2 = decision_tree.predict(x_test)
        test_acc = accuracy_score(y_test, predicted_values2)
        test_scores.append(test_acc)

        predicted_values22 = decision_tree.predict(x_train)
        train_acc = accuracy_score(y_train, predicted_values22)
        train_scores.append(train_acc)

        print('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))
    # plot train and test scores vs tree depth
    pyplot.plot(values, train_scores, '-o',color="blue", label='Train')
    pyplot.plot(values, test_scores, '-o',color="black", label='Test')
    pyplot.legend()
    pyplot.show()
    #  the following features will be used in the decision tree
    feature_col = ["followers", "actions", "Tweet"]
    dot_data = StringIO()
    # plot the tree based on the class name (spam or quality)
    export_graphviz(decision_tree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_col, class_names=['Spam', 'Quality'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    # make the tree as an image in png
    graph.write_png('decision_tree_Test.png')
    Image(graph.create_png())
    # print the accuracy of the test data
    accuracyy = Label(dt, text=f'classifier Accuracy {str(metrics.accuracy_score(y_test, predicted_values2))}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)

    # print the report of the test data
    report = Label(dt, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(dt, text=f"{metrics.classification_report(y_test, predicted_values2)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)

    # print the confusion matrix of the test data
    confmat = Label(dt, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(dt, text=f"{metrics.confusion_matrix(y_test, predicted_values2)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
    # -------------------------------------------------------------------
 # function to train the data using decision tree
def DecisionTree_Train():
    dtt = Tk()
    # login window settings
    dtt.geometry('500x550')
    dtt.title(' Decision Tree Train')
    dtt.resizable(0, 0)
    gradienttt(dtt)

    # use Decision Tree Classifier
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(x_train, y_train)
    predicted_values2 = decision_tree.predict(x_train)

    #print the accuracy
    accuracyy = Label(dtt, text=f'classifier Accuracy {str(metrics.accuracy_score(y_train, predicted_values2))}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)
    #print the report
    report = Label(dtt, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(dtt, text=f"{metrics.classification_report(y_train, predicted_values2)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)
    #print the confusion matrix
    confmat = Label(dtt, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(dtt, text=f"{metrics.confusion_matrix(y_train, predicted_values2)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
    # -------------------------------------------------------------------
# show the interface of the random forest
def test_train_RandomForest():
    tt3 = Tk()
    # login window settings
    tt3.geometry('200x130')
    tt3.title(' Random Forest ')
    tt3.resizable(0, 0)
    gradient(tt3)

    test1 = Button(tt3, width=20, height=2, text="Train", bg="#E87C43", fg="white", command=RandomForest_Train)
    test1.pack()
    test1.place(x=20, y=15)

    test2 = Button(tt3, width=20, height=2, text="Test",bg = "#E87C43",fg = "white", command=RandomForest_Test)
    test2.pack()
    test2.place(x=20, y=70)
 # function to test the data using Random forest
def RandomForest_Test():
    rf = Tk()
    # login window settings
    rf.geometry('500x550')
    rf.title(' Random Forest Test ')
    rf.resizable(0, 0)
    gradient(rf)    # color the background of the random forest interface

    # define lists to collect scores
    train_scores, test_scores = list(), list()
    # define the tree depths to evaluate
    values = [i for i in range(1, 30)]
    # evaluate a decision tree for each depth
    for i in values:
        # use Random Forest Classifier
        random_forest = RandomForestClassifier(max_depth=i)
        random_forest.fit(x_train, y_train)
        predicted_values3 = random_forest.predict(x_test)
        test_acc = accuracy_score(y_test, predicted_values3)
        test_scores.append(test_acc)

        predicted_values33 = random_forest.predict(x_train)
        train_acc = accuracy_score(y_train, predicted_values33)
        train_scores.append(train_acc)

        print('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))
        # plot of train and test scores vs tree depth
    pyplot.plot(values, train_scores, '-o', color="orange", label='Train')
    pyplot.plot(values, test_scores, '-o', color="green", label='Test')
    pyplot.legend()
    pyplot.show()
    #print the accuarcy
    accuracyy = Label(rf, bg="#7185A3",text=f'classifier Accuracy {str(metrics.accuracy_score(y_test, predicted_values3))}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)
    #print the report
    report = Label(rf, bg="#7185A3",text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(rf, bg="#7185A3", text=f"{metrics.classification_report(y_test, predicted_values3)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)
    #print the confusion matrix
    confmat = Label(rf, bg="#7185A3", text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(rf, bg="#7185A3", text=f"{metrics.confusion_matrix(y_test, predicted_values3)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
    # ----------------------------------------------------------------
 # function to train  the data using Random forest
def RandomForest_Train():
    rft = Tk()
    # login window settings
    rft.geometry('500x550')
    rft.title(' Random Forest Train ')
    rft.resizable(0, 0)
    gradient(rft)

    # use Random Forest Classifier
    random_forest = RandomForestClassifier()
    random_forest.fit(x_train, y_train)
    predicted_values3 = random_forest.predict(x_train)
    #print the accuarcy
    accuracyy = Label(rft, bg="#7185A3",text=f'classifier Accuracy {str(metrics.accuracy_score(y_train, predicted_values3))}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)
    #print the report
    report = Label(rft, bg="#7185A3", text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(rft, bg="#7185A3", text=f"{metrics.classification_report(y_train, predicted_values3)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)
    #print the confusion matrix
    confmat = Label(rft, bg="#7185A3", text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(rft, bg="#7185A3", text=f"{metrics.confusion_matrix(y_train, predicted_values3)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
    # ----------------------------------------------------------------
# show the interface of Nueral network
def test_train_NeuralNetwork():
    tt4 = Tk()
    # login window settings
    tt4.geometry('200x130')
    tt4.title(' Neural Network ')
    tt4.resizable(0, 0)
    gradientt(tt4)


    test1 = Button(tt4, width=20, height=2, text="Train", bg="#E87C43", fg="white", command=NeuralNetwork_Train)
    test1.pack()
    test1.place(x=20, y=15)

    test2 = Button(tt4, width=20, height=2, text="Test",bg = "#E87C43",fg = "white", command=NeuralNetwork_Test)
    test2.pack()
    test2.place(x=20, y=70)

 # function to train  the data using Nueral network
def NeuralNetwork_Train():
    nn = Tk()
    # login window settings
    nn.geometry('500x550')
    nn.title(' Neural Network Train ')
    nn.resizable(0, 0)
    gradientt(nn)

    # use nural network classifier
    nural_network = sklearn.neural_network.MLPClassifier()
    # Train the model on the whole data set
    nural_network.fit(x_train, y_train)
    # Evaluate on training data
    predicted_values4 = nural_network.predict(x_train)

    accuracyy = Label(nn,text=f'classifier Accuracy {sklearn.metrics.accuracy_score(y_train, predicted_values4)}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)

    report = Label(nn, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    metricss = Label(nn, text=f"{sklearn.metrics.classification_report(y_train, predicted_values4)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)

    confmat = Label(nn, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(nn, text=f"{sklearn.metrics.confusion_matrix(y_train, predicted_values4)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)

 # function to test  the data using nueral network
def NeuralNetwork_Test():
    nn = Tk()
    # login window settings
    nn.geometry('500x550')
    nn.title(' Neural Network Test ')
    nn.resizable(0, 0)
    gradientt(nn)

    # use nural network classifier
    nural_network = sklearn.neural_network.MLPClassifier()
    # Train the model on the whole data set
    nural_network.fit(x_train, y_train)
    # Evaluate on training data
    predicted_values4 = nural_network.predict(x_test)
# print the accuarcy
    accuracyy = Label(nn,text=f'classifier Accuracy {sklearn.metrics.accuracy_score(y_test, predicted_values4)}')
    o = ('Andalus', 16)
    accuracyy.config(font=o)
    accuracyy.place(x=40, y=5)

    report = Label(nn, text='classifier performance Report: ')
    o = ('Andalus', 16)
    report.config(font=o)
    report.place(x=40, y=60)

    # print the report
    metricss = Label(nn, text=f"{sklearn.metrics.classification_report(y_test, predicted_values4)}")
    o = ('Andalus', 16)
    metricss.config(font=o)
    metricss.place(x=40, y=95)

    # print the confusion matrix
    confmat = Label(nn, text="confusion matrix: ")
    o = ('Andalus', 16)
    confmat.config(font=o)
    confmat.place(x=40, y=405)

    conf = Label(nn, text=f"{sklearn.metrics.confusion_matrix(y_test, predicted_values4)}")
    o = ('Andalus', 16)
    conf.config(font=o)
    conf.place(x=40, y=440)
# function to color the background
def gradient(x):
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(333333 + r)
        Frame(x, width=15, height=550, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

gradient(welcome)  # set the gradient color for the login window

# function to color the background in another colors
def gradientt(t):
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(423512 + r)
        Frame(t, width=15, height=550, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1
# function to color the background in another colors
def gradienttt(t):
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(223522 + r)
        Frame(t, width=15, height=550, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

# function to color the background in another colors
def gradientttt(t):
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(753522 + r)
        Frame(t, width=15, height=550, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1


note = Label(welcome,text='                        Fatima  Jihan  Hedaya                        ')
o = ('French Script MT', 14)
note.config(font=o)
note.place(x=2, y=400)

note1 = Label(welcome,bg="#7185A3",text='Tweet Spam Detection')
o = ('Andalus', 16)
note1.config(font=o)
note1.place(x=90, y=1)

Frame(welcome, width=250,bg = "#7185A3",height=320).place(x=70, y=60)  # set a white background abov the grdient one

button1 = Button(welcome, width=20, height=2, text="Naive Bayes",bg = "#E87C43",fg = "white", command=test_train_naiveBayes)
button1.pack()
button1.place(x=120, y=80)

button2 = Button(welcome, width=20, height=2, text="Decision Tree",bg = "#E87C43",fg = "white", command=test_train_DecisionTree)
button2.pack()
button2.place(x=120, y=150)

button3 = Button(welcome, width=20, height=2, text="Random Forest",bg = "#E87C43",fg = "white", command=test_train_RandomForest)
button3.pack()
button3.place(x=120, y=230)

button4 = Button(welcome, width=20, height=2, text="Neural Network",bg = "#E87C43",fg = "white", command=test_train_NeuralNetwork)
button4.pack()
button4.place(x=120, y=310)

welcome.mainloop()
