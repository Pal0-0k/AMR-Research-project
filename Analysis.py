import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Palak\Downloads\responses.csv.csv")
x = df["Have you ever heard of antibiotics before?"]
counts = x.value_counts()
plt.title("Awareness About Antibiotics and Viral Infections")
plt.xlabel("People Aware of antibiotics")

plt.ylabel("Number of people")
counts_index = counts.index
counts_values = counts.values
plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
plt.savefig("viral_awareness.png")
plt.show()
