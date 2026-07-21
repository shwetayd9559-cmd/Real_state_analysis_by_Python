import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('gurgaon_real_state_dataset.csv')
print(df.head(10))
df.info()
# data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
# numerical column cleaning

df['price'] = df['price'].astype(str).str.replace(',', '', regex=False).astype(float)
print(df['price'])
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(float)
print(df['rate_per_sqft'])

# categorical column cleaning

df['rera_approval'] = df['rera_approval'].astype(bool)
print(df['rera_approval'])
# drop duplicate values from dataset
df=df.drop_duplicates()
df=df.dropna()


# Questions for data analysis:
# 1. which is the costlier apartment in gurgaon datset?
costliest_flat=df[df['price'] == df['price'].max()]
print(f"Costliest Apartment in Gurgaon Dataset: {costliest_flat}")

#2. which locality has the highest average price?
locality_avg_price = df.groupby('locality')['price'].mean().sort_values(ascending=False)
print(f"Locality with Highest Average Price: {locality_avg_price}")

#3. which locality  has the highest rate per sqft?
locality_avg_rate = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False)
print(f"Locality with Highest Average Rate per Sqft: {locality_avg_rate}")

#4. do ready to move properties cost more than under construction properties?
ready_to_move_avg_price = df[df['status'] == 'Ready to Move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'Under Construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print(f"Ready to Move properties cost more than Under Construction properties. ")
else:
    print(f"Under Construction properties cost more than Ready to Move properties.")

#5. do rera_approval property command A price premium ?
rera_approval_avg_price = df[df['rera_approval'] == True]['price'].mean()
non_rera_approval_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approval_avg_price > non_rera_approval_avg_price:
    print(f"RERA approved properties command a price premium.")
else:
    print(f"Non-RERA approved properties command a price premium.")

# 6. How does area impact price?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='area', y='price')
plt.title('Impact of Area on Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()


# 7. which BHK CONFIGURATION IS MOST EXPENSIVE?
bhk_expensive = df.groupby('bhk_count')['rate_per_sqft'].mean().sort_values(ascending=False).idxmax()
print(f"BHK Configuration with Highest Average Rate per Sqft: {bhk_expensive}")


# 8. which property type is costlier ?
property_type_costliest = df.groupby('property_type')['price'].mean().sort_values(ascending=False).idxmax()
print(f"Property Type with Highest Average Price: {property_type_costliest}")

# 9. Do certain builder price higher?
print("Top 5 Builders with Highest Average Price:")
top_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
print(top_builders)

# 10. Are larger homes more expensive per sqft?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.title('Impact of Area on Rate per Sqft')
plt.xlabel('Area')
plt.ylabel('Rate per Sqft')
plt.show()














