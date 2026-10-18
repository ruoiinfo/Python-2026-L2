import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu tu file CSV
df = pd.read_csv("scores.csv")

# In du lieu de kiem tra
print(df.head())

# 1. Scatter plot
df[["math", "python", "db"]].plot(
    kind="scatter",
    x="math",
    y="python"
)

plt.title("Student Scores")
plt.savefig("scattered.png")
plt.show()

# 2. Histogram cua 3 mon hoc
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

df["math"].plot(kind="hist", ax=axes[0], title="Math")
df["python"].plot(kind="hist", ax=axes[1], title="Python")
df["db"].plot(kind="hist", ax=axes[2], title="DB")

plt.tight_layout()
plt.savefig("histo.png")
plt.show()

# 3. Box plot cua 3 mon hoc
df[["math", "python", "db"]].plot(kind="box")

plt.title("Score Comparison")
plt.savefig("box.png")
plt.show()