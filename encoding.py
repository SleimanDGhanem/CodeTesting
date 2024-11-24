from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Generate all sizes (3x3 to 20x20)
sizes = [(i, j) for i in range(3, 21) for j in range(3, 21)]

# Initialize and fit the encoder
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(sizes)

#load the data
data = np.load("dungeon.npy", allow_pickle=True)
data1D = []

for i in range(len(data)):
  data1D.append({'layout': data[i]['layout'].flatten(),'size': data[i]['size']})

data1D = np.array(data1D)

np.save("Dungeon1D.npy", data1D, allow_pickle=True)
