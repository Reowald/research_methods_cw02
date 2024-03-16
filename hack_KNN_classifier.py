import os
import gzip
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Function to extract label from filename
def extract_label(filename):
    return filename.split('_')[0]

# Function to extract file size
def get_file_size(filepath):
    return os.path.getsize(filepath)

data_dir = r'C:\Users\ryand\Code\Data\Dataset News Articles\News Articles\compressed'

# List to store file sizes and corresponding labels
file_sizes = []
labels = []

# Iterate through files
for filename in os.listdir(data_dir):
    if filename.endswith('.gz'):
        label = extract_label(filename)
        filepath = os.path.join(data_dir, filename)
        # Open compressed file and get size
        with gzip.open(filepath, 'rb') as f:
            file_size = get_file_size(filepath)
            file_sizes.append(file_size)
            labels.append(label)

# Convert lists to numpy arrays
file_sizes = np.array(file_sizes).reshape(-1, 1)
labels = np.array(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(file_sizes, labels, test_size=0.25, random_state=42)

# Initialize and train KNN classifier
k = 3  # Number of neighbors
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train, y_train)

# Visualize the test data labels and linearized label data
plt.figure(figsize=(10, 6))

# Plot test data labels
plt.scatter(X_test, y_test, color='red', label='Test Data Labels', alpha=0.5)

# Plot linearized label data
unique_labels = np.unique(labels)
for i, label in enumerate(unique_labels):
    x = np.mean(X_train[y_train == label])
    plt.plot(x, label, 'X', markersize=10, label=f'Linearized Label: {label}')

plt.title('Visualization of Test Data Labels and Linearized Label Data')
plt.xlabel('File Size')
plt.ylabel('Label')
plt.legend()
plt.grid(True)
plt.show()


# Predict labels for test data
y_pred = knn_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Calculate nearest distances
distances, indices = knn_classifier.kneighbors(X_test)
print("Nearest distances:")
print(distances)

# Select a subset of test data points for visualization
num_samples = 1
selected_indices = np.random.choice(len(X_test), num_samples, replace=False)

# Get nearest neighbors and distances for the selected test data points
selected_distances = distances[selected_indices]
selected_indices_neighbors = indices[selected_indices]

# Plot nearest neighbors for each selected test data point
plt.figure(figsize=(12, 8))

for i, idx in enumerate(selected_indices):
    plt.subplot(num_samples, 1, i+1)
    plt.scatter(X_train, y_train, color='blue', label='Training Data')
    plt.scatter(X_test[idx], y_test[idx], color='red', label='Test Data', marker='x')
    plt.scatter(X_train[selected_indices_neighbors[i]], y_train[selected_indices_neighbors[i]], c='green', label='Nearest Neighbors', marker='o')
    plt.title(f"Nearest Neighbors for Test Data Point {idx}")
    plt.xlabel('File Size')
    plt.ylabel('Label')
    plt.legend()
    plt.grid(True)
    
    # Display distances to nearest neighbors
    for j, neighbor_idx in enumerate(selected_indices_neighbors[i]):
        plt.text(X_train[neighbor_idx], y_train[neighbor_idx], f"{selected_distances[i][j]:.2f}", fontsize=8, ha='right', va='bottom')

plt.tight_layout()
plt.show()

plt.show()

