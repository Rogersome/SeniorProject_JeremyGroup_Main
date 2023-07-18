import numpy as np
import pandas as pd
import networkx as nx
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow_addons.layers.graph import GraphConvolution


# Create a list of file names
filenames = ["TripA01.csv", "TripA02.csv", "TripA03.csv", "TripA04.csv", "TripA05.csv", "TripA06.csv", "TripA07.csv",
             "TripA08.csv", "TripA09.csv", "TripA10.csv", "TripA11.csv", "TripA12.csv", "TripA13.csv", "TripA14.csv",
             "TripA15.csv", "TripA16.csv", "TripA17.csv", "TripA18.csv", "TripA19.csv", "TripA20.csv", "TripA21.csv",
             "TripA22.csv", "TripA23.csv", "TripA24.csv", "TripA25.csv", "TripA26.csv", "TripA27.csv", "TripA28.csv",
             "TripA29.csv", "TripA30.csv", "TripA31.csv", "TripA32.csv"]

# Load the data from the files
data = []
for filename in filenames:
    df = pd.read_csv(filename, encoding="ANSI")
    data.append(df)

# Concatenate the DataFrames together
data = pd.concat(data)

# Preprocess the data
data = data.dropna()
data = StandardScaler().fit_transform(data)

# Create a graph object
graph = nx.Graph()
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i, 0] == data[j, 0]:
            graph.add_edge(i, j)

# Train a GNN model on the graph
model = Sequential()
model.add(GraphConvolution(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(data, data[:, -1], epochs=100)

# Evaluate the model on a held-out dataset
X_train, X_test, y_train, y_test = train_test_split(data, data[:, -1], test_size=0.2)
model.evaluate(X_test, y_test)

# Predict the battery health of the EV
predictions = model.predict(data)

# for i in range (33): print("\"TripA", i, ".csv\"", sep="", end=", ")