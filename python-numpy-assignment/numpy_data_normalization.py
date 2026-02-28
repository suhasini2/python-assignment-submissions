import numpy as np

arr=np.array([10,20,30,40])

meandata=np.mean(arr)
stddata=np.std(arr)

normalized = (arr - meandata) / stddata

reshaped=np.reshape(normalized,[2,2])

print(f"Original data: {arr}")
print(f"Mean: {meandata}")
print(f"Standard Deviation: {stddata}")
print(f"Normalized data: {normalized}")
print(f"Reshaped data shape: {reshaped.shape}")