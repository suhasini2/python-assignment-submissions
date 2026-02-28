import numpy as np

np.random.seed(2)
arr=np.random.randint(0,10,[100,3])
featuremean=np.mean(arr, axis=0)
featurestd=np.std(arr, axis=0)
normalized = (arr - featuremean) / featurestd
split_idx=int(len(arr)*0.8)
training_set=arr[:split_idx]
test_set=arr[split_idx:]
training_set[1][2]=24


print(f"Original data shape: {arr.shape}")
print(f"Mean shape: {featuremean.shape}")
print(f"Training data shape: {training_set.shape}")
print(f"Test data shape: {test_set.shape}")
print(f"Note: Modifying the slice affected the original array")
