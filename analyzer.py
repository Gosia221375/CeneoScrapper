import os
import pandas as pd
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("Please enter the product id: ")

opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["score"].mean().round(2)

stars_recommendation = pd.crosstab(opinions["score"], opinions["rcmd"], dropna=False)

if not os.path.exists("plots"):
    os.makedirs("plots")

recommendations = opinions["rcmd"].value_counts(dropna=False).sort_index().reindex([False, True, None])

recommendations.plot.pie(
    label = "",
    title = "Recommendations: "+product_id,
    labels = ["Not recommend", "Recommend", "No opinion"],
    colors = ["crimson", "forestgreen", "grey"],
    autopct = lambda p: f"{p:.1f}%" if p>0 else ""
)
plt.savefig(f"plots/{product_id}_rcmd.png")
plt.close()

stars = opinions["score"].value_counts(dropna=False).sort_index().reindex([5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5])

stars.plot.bar(
    opinions["score"],
    color = "fuchsia",
    width = 0.4
)

plt.show()