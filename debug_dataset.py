
import pickle

with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
labels = data_dict['labels']

print(f"Number of samples: {len(data)}")
print(f"Number of labels: {len(labels)}")

unique_labels = sorted(list(set(labels)))
print(f"Unique labels: {unique_labels}")

for label in unique_labels:
    count = labels.count(label)
    print(f"Number of samples for label {label}: {count}")
