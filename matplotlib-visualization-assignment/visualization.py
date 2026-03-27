import numpy as np
import matplotlib.pyplot as plt

epochs=np.arange(0,11)
stl=np.random.normal(loc=0, scale=1, size=len(epochs))
models=['ModelA','ModelB','ModelC']
accuracy=[0.85,0.90,0.88]

plt.figure(1)
plt.plot(stl,epochs,marker='*', linestyle='--')
plt.xlabel("Synthetic Training Loss")
plt.ylabel("Loss")
plt.title("Loss vs Epchs")
plt.grid(True)

plt.figure(2)
plt.scatter(epochs,stl, marker='o')
plt.xlabel("epochs")
plt.ylabel("Synthetic Training Loss")
plt.title("Loss vs Epchs")
plt.grid(True)


plt.figure(3)
plt.bar(models,accuracy)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Models vs Accuracy")


plt.show()
