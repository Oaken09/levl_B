import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("list.xlsx")
X = df["X"]
Y = df["Y"]
Z = df["Z"]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=X, cmap='coolwarm')

plt.show()