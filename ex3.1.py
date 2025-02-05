import json
import matplotlib.pyplot as plt

with open("internetdata.json") as file:
    data = json.load(file)

belowThresh = []
aboveThresh = []

for country in data:
    incomePerPerson = country.get("incomeperperson")
    internetUseRate = country.get("internetuserate")
     
    if(incomePerPerson is None or internetUseRate is None):
        continue

    if(incomePerPerson >= 10000):
        aboveThresh.append(internetUseRate)
    else:
        belowThresh.append(internetUseRate)

plt.hist(belowThresh, bins=20, color='blue', edgecolor='black')
plt.title('Internet Usage (Income < 10,000)')
plt.xlabel('Internet Usage (%)')
plt.ylabel('Number of Countries')
plt.show()

plt.hist(aboveThresh, bins='auto', color='red', edgecolor='black')
plt.title('Internet Usage (Income >= 10,000)')
plt.xlabel('Internet Usage (%)')
plt.ylabel('Number of Countries')
plt.show()