import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.data import Data
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import add_self_loops, degree
import pandas as pd

# Step 1: Load the data from multiple files
file_paths = ["TripA01.csv", "TripA02.csv", "TripA03.csv", "TripA04.csv", "TripA05.csv", "TripA06.csv", "TripA07.csv",
              "TripA08.csv", "TripA09.csv", "TripA10.csv", "TripA11.csv", "TripA12.csv", "TripA13.csv", "TripA14.csv",
              "TripA15.csv", "TripA16.csv", "TripA17.csv", "TripA18.csv", "TripA19.csv", "TripA20.csv", "TripA21.csv",
              "TripA22.csv", "TripA23.csv", "TripA24.csv", "TripA25.csv", "TripA26.csv", "TripA27.csv", "TripA28.csv",
              "TripA29.csv", "TripA30.csv", "TripA31.csv", "TripA32.csv"]

# Load and merge the data from multiple files
data_frames = []
for file_path in file_paths:
    data_frame = pd.read_csv(file_path, encoding="ANSI")  # Adjust if using a different file format
    data_frames.append(data_frame)

# Merge the data frames into a single data frame
merged_data = pd.concat(data_frames)

# Step 2: Preprocess the merged data
# Perform preprocessing steps on the merged data
# ...

# Step 3: Prepare the data for GNN training
# Create lists to store node features and edge indices
node_features = []
edge_index = []

# Iterate over the merged data and populate the node features and edge indices lists
for i in range(len(merged_data)):
    node_features.append([merged_data.loc[i, 'Battery Temperature [°C]'],
                          # merged_data.loc[i, 'Battery Temperature (End)'],
                          merged_data.loc[i, 'SoC [%]'],
                          # merged_data.loc[i, 'Battery State of Charge (End)'],
                          merged_data.loc[i, 'Ambient Temperature [°C]']])
    edge_index.append([i, i + 1])  # Assuming data is sorted in temporal order

# Convert the lists to torch tensors
node_features = torch.tensor(node_features, dtype=torch.float)
edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()


# Step 4: Define the GNN model
class GNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GNN, self).__init__()
        self.conv1 = MessagePassing(nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.ReLU()))
        self.conv2 = MessagePassing(nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.ReLU()))
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = self.conv2(x, edge_index)
        x = self.fc(x)
        return x


# Step 5: Prepare the data for GNN training
data = Data(x=node_features, edge_index=edge_index)

# Step 6: Create an instance of the GNN model and define the loss function and optimizer
input_dim = node_features.size(1)
hidden_dim = 64
output_dim = 1

model = GNN(input_dim, hidden_dim, output_dim)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Extract the target values from the merged_data DataFrame
target = torch.tensor(merged_data['Battery Health'].values, dtype=torch.float)


# Step 7: Train the GNN model
num_epochs = 100

for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(data.x, data.edge_index)
    loss = criterion(outputs, target)  # Assuming you have the target values for battery health
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))

# Step 8: Evaluate the GNN model
# After training, you can use the trained model to make predictions on new data
with torch.no_grad():
    predicted_health = model(data.x, data.edge_index)
