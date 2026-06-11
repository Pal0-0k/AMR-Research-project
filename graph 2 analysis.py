import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Palak\Downloads\responses.csv.csv")
print(list(df.columns))
question = df.columns[2]
x = df[question]
counts = x.value_counts()
plt.title("People Aware of antibiotic use for bacterial infection")
plt.xlabel("Antibiotics are used to treat")
plt.ylabel("Responses")
counts_index = counts.index
counts_values = counts.values
plt.bar(counts_index, counts_values, color=["g", "r", "b", "y"])
plt.savefig("What do antibiotics work against.png")
plt.show()
