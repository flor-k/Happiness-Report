#!/usr/bin/env python
# coding: utf-8

# In[199]:


import pandas as pd
import matplotlib.pyplot as plt

# Import data
h_2015 = pd.read_csv("2015.csv")
h_2016 = pd.read_csv("2016.csv")
h_2017 = pd.read_csv("2017.csv")
h_2018 = pd.read_csv("2018.csv")
h_2019 = pd.read_csv("2019.csv")

h_2015["Year"] = "2015"
h_2016["Year"] = "2016"
h_2017["Year"] = "2017"
h_2018["Year"] = "2018"
h_2019["Year"] = "2019"

h_2015 = h_2015.drop(columns=['Standard Error', 'Dystopia Residual', 'Region', "Happiness Rank" ])

h_2015.rename(columns={"Country": "Country Region"},inplace=True)

h_2016 = h_2016.drop(columns=['Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual', "Happiness Rank", "Region"])

h_2016.rename(columns={"Country": "Country Region"},inplace=True)

h_2017 = h_2017.drop(columns=['Whisker.high', 'Whisker.low', 'Dystopia.Residual', "Happiness.Rank"])

h_2017.rename(columns={"Happiness.Score": "Happiness Score", "Country": "Country Region", "Economy..GDP.per.Capita.": "Economy (GDP per Capita)", "Health..Life.Expectancy.": "Health (Life Expectancy)", "Trust..Government.Corruption.": "Trust (Government Corruption)"},inplace=True)

h_2018.rename(columns={"Score": "Happiness Score", "Country or region": "Country Region", "GDP per capita": "Economy (GDP per Capita)", "Healthy life expectancy": "Health (Life Expectancy)", "Perceptions of corruption": "Trust (Government Corruption)",
                      "Social support":"Family", "Freedom to make life choices":"Freedom"},inplace=True)


h_2018 = h_2018.drop(["Overall rank"], axis=1)

h_2019 = h_2019.drop(["Overall rank"], axis=1)

h_2019.rename(columns={"Score": "Happiness Score", "Country or region": "Country Region", "GDP per capita": "Economy (GDP per Capita)", "Healthy life expectancy": "Health (Life Expectancy)", "Perceptions of corruption": "Trust (Government Corruption)",
                      "Social support":"Family", "Freedom to make life choices":"Freedom"},inplace=True)


frames = [h_2015, h_2016, h_2017, h_2018, h_2019]

df = pd.concat(frames)


df2 = df.loc[(df['Country Region']=='Canada'), :]
df3 = df.loc[(df['Country Region']=='Iceland'), :]
df4 = df.loc[(df['Country Region']=='Switzerland'), :]
df5 = df.loc[(df['Country Region']=='Denmark'), :]
df6 = df.loc[(df['Country Region']=='Norway'), :]

plt.figure(figsize=(25,6))
plt.plot(df2["Year"],df2["Happiness Score"])
plt.plot(df3["Year"],df3["Happiness Score"])
plt.plot(df4["Year"],df4["Happiness Score"])
plt.plot(df5["Year"],df5["Happiness Score"])
plt.plot(df6["Year"],df6["Happiness Score"])
plt.grid()
plt.title('Happiness Score for Top 5 Countries')
plt.ylabel('Happiness')
plt.xlabel('Years')

plt.show()

