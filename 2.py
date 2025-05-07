import pandas as pd
import matplotlib.pyplot as plt


file_path = 'list.xlsx'
df = pd.read_excel(file_path)

plt.figure(figsize=(8, 6))
plt.plot(df['X'], df['Y'], marker='o', label='Зависимость y от x')

plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)

plt.show()