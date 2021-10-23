grocery_list=["banana", "apple", "milk"]
print(grocery_list)
grocery_list.append ("yogurt")
print(grocery_list)
grocery_list[0:2]
len(grocery_list)

counties = []
counties= ["Arapahoe", "Denver", "Jefferson"]
counties_turple = ("Arapahoe", "Denver", "Jefferson")
print(counties_turple)

counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denvor"]=463353
counties_dict["Jefferson"]=432438

voting_data =[]
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denvor", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county": "El Paso", "registered_voters": 461149})
voting_data.pop(0)
voting_data[2] = "Jefferson"
voting_data[3] = "Denvor"

counties = ["Arapahoe", "Denvor", "Jefferson"]
if counties[3] != "Jefferson":
    print(counties[2])

temperture = int(input("What is the tempi outside today?"))
if temperture >80:
    print("Turn on the AC!")
else:
    print("Open the windows!")

score = int(input("What is your test score?"))
if score >=90:
    print("Your grade is an A")
else:
    if score >=80:
        print ("Your grade is a B")
    else:
        if score>=70:
            print ("Your grade is a C")
        else:
            if score>=60:
                print("Your grade is a D")
            else:
                print ("You failed!")

counties = ["Arapahoe", "Denvor", "Jefferson"]
if "Arapahoe" in counties:
    print(True)
else:
    print(False)
if "El Paso" not in counties:
    print(True)
else:
    print(False)

x= 7
y = 8
if x==10 or y ==10:
    print(True)
else:
    print(False)

x = 5
y = 9
if not (x>y):
    print(True)
else:
    print(False)

x = 0
while x<=7:
    print(x)
    x=x+2

for county in counties:
    print(county)

i=0
for i in range(len(counties)):
    print(counties[i])

counties_turple=("Arapahoe", "Denvor", "Jefferson")
for county in counties_turple:
    print(county)

counties_dict={"Arapahoe": 422829, "Denvor": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

counties_dict={"Arapahoe": 422829, "Denvor": 463353, "Jefferson": 432438}
for counties in counties_dict.keys():
    print(counties)
#or
for county in counties_dict:
    print(counties_dict[county])

voting_data=[{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denvor", "registered_voters": 463353},
            {"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(counties_dict)):
    print(counties_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county in range(len(voting_data)):
    print(county)

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for counties_dict in voting_data:
    for key, value in counties_dict.items():
        print(value)

my_votes=int(input("how many votes did you get?"))
total_votes = int(input("What is the total votes?"))
print(f"I received {my_votes/total_votes*100:.2f}% of the total votes.")

counties_dict={"Arapahoe":369237, "Denvor": 413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

counties_dict={"Arapahoe": 422829, "Denvor": 463353, "Jefferson": 432438}
for keys, value in counties_dict.items():
    print(f"{keys} has {value:,} registered voters")

# import datatime class from datetime module
import datetime

# use the now() attribute on datetime class to get present time
now = datetime.datetime.now()

# print result
print("the time right now is "+ now)
