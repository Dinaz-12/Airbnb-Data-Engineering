import pandas as pd

df = pd.read_csv("data/processed/featured_listings.csv")

print("Dataset Loaded")
print(df.shape)

print(df.columns.tolist())


from scipy.stats import ttest_ind

print("\n" + "="*60)
print("H1: Entire Home vs Private Room Price Comparison")
print("="*60)

# Extract prices
entire_home = df[df["room_type"] == "Entire home/apt"]["price"]

private_room = df[df["room_type"] == "Private room"]["price"]

# Run T-Test
t_stat, p_value = ttest_ind(
    entire_home,
    private_room,
    equal_var=False,
    nan_policy="omit"
)

print(f"Entire Home Mean Price : {entire_home.mean():.2f}")
print(f"Private Room Mean Price: {private_room.mean():.2f}")

print(f"T Statistic : {t_stat:.4f}")
print(f"P Value     : {p_value:.6f}")

if p_value < 0.05:
    print("✅ Result: Reject H0")
    print("There is a statistically significant difference in price.")
else:
    print("❌ Result: Fail to Reject H0")
    print("No statistically significant difference found.")


print("\nUnique values in host_is_superhost:")
print(df["host_is_superhost"].value_counts(dropna=False))


from scipy.stats import ttest_ind

print("\n" + "="*60)
print("H2: Superhost vs Non-Superhost Review Rating")
print("="*60)

# Extract review ratings
superhost = df[df["host_is_superhost"] == "t"]["review_scores_rating"].dropna()

normal_host = df[df["host_is_superhost"] == "f"]["review_scores_rating"].dropna()

# print sample size
print(f"Superhost Sample Size   : {len(superhost)}")
print(f"Normal Host Sample Size : {len(normal_host)}")

# T-Test
t_stat, p_value = ttest_ind(
    superhost,
    normal_host,
    equal_var=False,
    nan_policy="omit"
)

print(f"Superhost Mean Rating    : {superhost.mean():.2f}")
print(f"Normal Host Mean Rating  : {normal_host.mean():.2f}")

print(f"T Statistic : {t_stat:.4f}")
print(f"P Value     : {p_value:.6f}")

if p_value < 0.05:
    print("✅ Result: Reject H0")
    print("Superhosts have significantly different review ratings.")
else:
    print("❌ Result: Fail to Reject H0")
    print("No statistically significant difference in review ratings.")



print("\n" + "="*60)
print("H3: Price Difference by Review Count")
print("="*60)

# Create two groups
more_reviews = df[df["number_of_reviews"] > 10]["price"].dropna()
few_reviews = df[df["number_of_reviews"] <= 10]["price"].dropna()

print(f"Sample Size (>10 Reviews)  : {len(more_reviews)}")
print(f"Sample Size (<=10 Reviews) : {len(few_reviews)}")

# Independent T-Test
t_stat, p_value = ttest_ind(
    more_reviews,
    few_reviews,
    equal_var=False,
    nan_policy="omit"
)

print(f"Average Price (>10 Reviews)  : {more_reviews.mean():.2f}")
print(f"Average Price (<=10 Reviews) : {few_reviews.mean():.2f}")

print(f"T Statistic : {t_stat:.4f}")
print(f"P Value     : {p_value:.6f}")

if p_value < 0.05:
    print("✅ Result: Reject H0")
    print("There is a statistically significant price difference.")
else:
    print("❌ Result: Fail to Reject H0")
    print("No statistically significant price difference.")



from scipy.stats import f_oneway

print("\n" + "="*60)
print("H4: Price Differences Across Neighbourhoods")
print("="*60)

# Select top 5 neighbourhoods by listing count
top5 = (
    df["neighbourhood_cleansed"]
    .value_counts()
    .head(5)
    .index
)

groups = []

for area in top5:
    prices = df[df["neighbourhood_cleansed"] == area]["price"].dropna()
    groups.append(prices)

f_stat, p_value = f_oneway(*groups)

print("Neighbourhoods Tested:")
for area in top5:
    print(f"- {area}")

print(f"\nF Statistic : {f_stat:.4f}")
print(f"P Value     : {p_value:.6f}")

if p_value < 0.05:
    print("✅ Result: Reject H0")
    print("Average prices differ significantly across neighbourhoods.")
else:
    print("❌ Result: Fail to Reject H0")
    print("No statistically significant difference found.")