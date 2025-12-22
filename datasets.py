import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("movies.csv")

print("Here is what the dataset looks like:")
print(df.head())
print("\n")

df["title_length"] = df["title"].str.len()
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")

df_clean = df.dropna(subset=["title_length", "popularity"])


# Plot 1: Heated Scatter Plot

plt.figure()
scatter = plt.scatter(
    df_clean["title_length"],
    df_clean["popularity"],
    c=df_clean["popularity"],
    cmap="hot"
)

plt.xlabel("Title Length (number of characters)")
plt.ylabel("Popularity")
plt.title("Movie Title Length vs Popularity (Heat Scatter)")
plt.colorbar(scatter, label="Popularity")
plt.savefig("title_length_vs_popularity")
plt.show()


# Plot 2: Popularity vs Release Year Bar graph 

df_clean["release_date"] = pd.to_datetime(df_clean["release_date"], errors="coerce")
df_clean = df_clean.dropna(subset=["release_date", "popularity"])

df_clean["release_year"] = df_clean["release_date"].dt.year

pop_by_year = df_clean.groupby("release_year")["popularity"].mean()

plt.figure(figsize=(16, 6))
plt.bar(pop_by_year.index, pop_by_year.values, color='skyblue')
plt.xlabel("Release Year")
plt.ylabel("Average Popularity")
plt.title("Average Movie Popularity by Release Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("popularity_vs_release_year.png")
plt.show()

