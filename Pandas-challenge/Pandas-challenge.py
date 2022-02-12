#!/usr/bin/env python
# coding: utf-8

# In[1]:


# libraries
import pandas as pd
import numpy as np

# file to Load 
file_to_load = "Desktop/Pandas-challenge/purchase_data.csv"

# purchasing File and store in Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:
#total players


total_players=len(purchase_data["SN"].unique())
all_players = pd.DataFrame({"Total Players":[total_players]})
all_players



# In[3]:


# calculations to obtain number of unique items and average price
numberUniqueItems = purchase_data['Item ID'].nunique()
avgPrice = purchase_data['Price'].mean()
numberPurchases = purchase_data['Purchase ID'].count()
totalRevenue = purchase_data['Price'].sum()

# summary data frame for the results
summary_df = pd.DataFrame({
    "Number of Unique Items": [numberUniqueItems],
    "Average Price": [avgPrice],
    "Number of Purchases": [numberPurchases],
    "Total Revenue": [totalRevenue]
})

# data as a cleaner formatting
summary_df["Average Price"] = summary_df["Average Price"].map("${:,.2f}".format)
summary_df["Total Revenue"] = summary_df["Total Revenue"].map("${:,.2f}".format)

# summary data frame
summary_df[["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]]


# In[4]:


# calculations for number of count & percentage
grouped_gender_df = purchase_data.groupby(["Gender"])

genderCount = grouped_gender_df["SN"].nunique()
genderPercentage = genderCount / total_players * 100

# summary data frame for the results
gender_demo_df = pd.DataFrame({"Total Count": genderCount,
                                    "Percentage of Players": genderPercentage})

# data as a cleaner formatting
gender_demo_df["Percentage of Players"] = gender_demo_df["Percentage of Players"].map("{:.2f}%".format)

# summary of the data frame
gender_demo_df[["Total Count", "Percentage of Players"]].sort_values(["Total Count"], ascending= False)


# In[5]:


# group to split by gender
gender = purchase_data.groupby("Gender")

#purchase count, average purchase price, total purchase value and average purchase per person
purchase_count = gender["Purchase ID"].count()
av_pp = gender["Price"].mean()
tot_val = gender["Price"].sum()
avg_ppp = tot_val / genderCount

#all values in data frame & format
purch_analysis = pd.DataFrame({"Purchase Count":purchase_count, "Average Purchase Price":av_pp, "Total Purchase Value":tot_val, "Avg Total Purchase per Person":avg_ppp})
purch_analysis.style.format({"Average Purchase Price":"${:.2f}", "Total Purchase Value":"${:,.2f}", "Avg Total Purchase per Person":"${:,.2f}"})



# In[6]:


# ages
bins = [0, 9, 14, 19, 24, 29, 34, 39, 150]
age_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# existing players using the age bins
purchase_data["Age Labels"] = pd.cut(purchase_data["Age"], bins, labels=age_labels)
grouped_age_df = purchase_data.groupby(["Age Labels"])

# numbers and percentages by age group
ageCount = grouped_age_df["SN"].nunique()
agePercentage = ageCount / total_players * 100

# summary data frame for the results
age_demo_df = pd.DataFrame({"Total Count": ageCount,
                            "Percentage of Players": agePercentage})

# percentage column to two decimal points
age_demo_df["Percentage of Players"] = age_demo_df["Percentage of Players"].map("{:.2f}%".format)

# age demographics table
age_demo_df[["Total Count", "Percentage of Players"]]


# In[7]:


# purchase count, average purchase price, total purchase price, average purchase total purchase per person in the table 
purchaseCount = grouped_age_df["Purchase ID"].count()
averagePurchasePrice = grouped_age_df["Price"].mean()
totalPurchasePrice = grouped_age_df["Price"].sum()
averageTotalPurchasePerPerson = totalPurchasePrice / ageCount

# data frame for the results
age_purchase_df = pd.DataFrame({"Purchase Count": purchaseCount,
                                "Average Purchase Price": averagePurchasePrice,
                                "Total Purchase Value": totalPurchasePrice,
                                "Avg Total Purchase per Person": averageTotalPurchasePerPerson})

# cleaner format of data 
age_purchase_df["Average Purchase Price"] = age_purchase_df["Average Purchase Price"].map("${:,.2f}".format)
age_purchase_df["Total Purchase Value"] = age_purchase_df["Total Purchase Value"].map("${:,.2f}".format)
age_purchase_df["Avg Total Purchase per Person"] = age_purchase_df["Avg Total Purchase per Person"].map("${:,.2f}".format)

# data frame
age_purchase_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Total Purchase per Person"]]


# In[8]:


# calculations on the table 
grouped_spenders_df = purchase_data.groupby(["SN"])

purchaseCount = grouped_spenders_df["Purchase ID"].count()
averagePurchasePrice = grouped_spenders_df["Price"].mean()
totalPurchaseValue = grouped_spenders_df["Price"].sum()

# data frame for the results
spenders_df = pd.DataFrame({"Purchase Count": purchaseCount,
                            "Average Purchase Price": averagePurchasePrice,
                            "Total Purchase Value": totalPurchaseValue})

# total purchase value column in descending order
spenders_df = spenders_df.sort_values(["Total Purchase Value"], ascending=False)

# cleaner format of data 
spenders_df["Average Purchase Price"] = spenders_df["Average Purchase Price"].map("${:,.2f}".format)
spenders_df["Total Purchase Value"] = spenders_df["Total Purchase Value"].map("${:,.2f}".format)

# summary of the data frame
spenders_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]].head()


# In[9]:


# item ID, item Name, and item Price in columns
items_df = purchase_data[["Item ID", "Item Name", "Price"]]

# group by item ID and item Name
grouped_items_df = items_df.groupby(["Item ID", "Item Name"])
# calculations for purchase count, item price, and total purchase value
purchaseCount = grouped_items_df["Item ID"].count()
itemPrice = grouped_items_df["Price"].mean()
totalPurchaseValue = grouped_items_df["Price"].sum()

# data frame for the results
items_df = pd.DataFrame({"Purchase Count": purchaseCount,
                         "Item Price": itemPrice,
                         "Total Purchase Value": totalPurchaseValue})

# purchase count column in descending order
items_df = items_df.sort_values(["Purchase Count"], ascending=False)

# cleaner format of the data
items_df["Item Price"] = items_df["Item Price"].map("${:,.2f}".format)
items_df["Total Purchase Value"] = items_df["Total Purchase Value"].map("${:,.2f}".format)

# summary data frame
items_df[["Purchase Count", "Item Price", "Total Purchase Value"]].head()


# In[10]:


# converting the Total Purchase Value column to floats
items_df["Total Purchase Value"] = items_df["Total Purchase Value"].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

# Table in descending order
items_df = items_df.sort_values(["Total Purchase Value"], ascending=False)

# cleaner formatt of the data
items_df["Total Purchase Value"] = items_df["Total Purchase Value"].map("${:,.2f}".format)

# data frame
items_df[["Purchase Count", "Item Price", "Total Purchase Value"]].head()













