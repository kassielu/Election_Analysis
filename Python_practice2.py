#3.2.10 - Repetition Statements
x = 0

while x <= 5:
    print(x)
    x = x + 1

#Test
#the following code should print nothing
count = 7

while count < 1:

    print("Hello World")

#Iterate Through Lists and Tuples

#3.2.8 - Decision Statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Iterate Through Lists and Tuples
for county in counties:
    print(county)

#Sample code not using Range()
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
#Sample code using Range()
for num in range(5):
    print(num)

#Using idexing to iterate through a list
for i in range(len(counties)):
    print(counties[i])

#Test
counties_tuple = ("Arapahoe","Denver","Jefferson")
#The following will print all 3 values from the above
for i in range(len(counties_tuple)):
      print(counties_tuple[i])
#Same for the below code
for county in counties_tuple:
      print(county)


#Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Using For Loop to print the Counties
for county in counties_dict:
    print(county)

#Using the Keys() method to print the keys
for county in counties_dict.keys():
    print(county)

#Get the Values of a Dictionary
for voters in counties_dict.values():
    print(voters)

#Get specific value for a key using the dictionary_name[key] format
print(counties_dict["Arapahoe"])

#Get all values for dictionary using dictionary_name[key] format
for county in counties_dict:
    print(counties_dict[county])

#Using the get method() to get the values of a key
for county in counties_dict:
    print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary
#for key, value in dictionary_name.items():
#    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

#3.2.10 Skill Drill - Print each county and registered voter form the counties dictionary
for county, voters in counties_dict.items():
    print(county + " county has ", str(voters) + " registered voters.")

#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Test - Using the Range() to function to iterate over the list of dictionaries and print the counties in voting_data
for i in range(len(voting_data)):

      print(voting_data[i])

#Get the Values from a List of Dictionaries
#Using the nested for loop to retrieve only the values from each dictionary in the list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Test - To retrieve the number of registered voters from each dictionary
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#To print oly the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#3.2.11 - Printing Formats
#Using F-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Using Multi F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

#Skill Drill using F-String
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#Skill Drill using F-String Again
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} County has {county_dict['registered_voters']} registered voters.")