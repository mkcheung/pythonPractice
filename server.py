import json
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import seaborn as sns
from urllib.request import urlopen
import matplotlib.dates as mdates
import pandas as pd

# Practice Drills:
    # Given a list of numbers, return a list with each number squared
    # Given a list of numbers, return the even ones in that list
    # Return a dict of numbers with keys of even or odd depending on which qualify for either
    # Return a dict of numbers that are squared if they are above ten. Key should be the original value
    # print all users over 18
    # create a dict in which the users have their ages squared
    # write a list of identifiers of name and age from a dict of userse
    # filter the dict for adults. Anyone over 18 and above
    # flatten the sublist

listOfNums = [3, 9, 12, 15, 7, 4, 18]
users = [
    {"name": "Alice", "age": 32},
    {"name": "Bob", "age": 18},
    {"name": "Carla", "age": 25},
    {"name": "David", "age": 16},
]
matrix = [[1,2,3],[4,5,6],[7,8,9]]


# data frame drills
# filter the frames for rows with temps above 60 degrees
# average temperature per city
# add a new column with the temperatures adjust for farenheit 
# sort the dataframe by humidity in ascending order

# loc
# Get the row for index 3 using loc
# Get the temp for NY on the second NY row
# Get LA rows only (label filtering vs boolean filtering)
# Get LA rows, but only temp + humidity columns
# Select rows by label range

# iloc
# Get the first row
# Get the last 2 rows
# Get the first 3 rows of temp + humidity (positions 1 and 2)
# Get the humidity of the 5th row (index position 4)
# Swap: retrieve the same value using loc instead

# idxmax & idxmin
# Find the index of the hottest temperature
# Using that index, return the full row
# Coldest temperature row
# City with highest humidity
# Entire row with highest humidity

# BOOLEAN INDEXING DRILLS (critical for filtering)
# All temps above 60
# All rows where humidity < 60 and temp > 60
# Combine boolean + loc: Select rows where humidity ≥ 55 AND return only city + date:

# SLICING DRILLS (labels vs positions)
# Label-based slicing with loc (inclusive of stop) something.loc[0:2]
# Position-based slicing with iloc (stop is EXCLUSIVE)
# Select alternating rows

# MULTIINDEX-SPECIFIC EXTENSIONS (when you're ready)
# Set a multiindex
# Retrieve all LA rows
# Retrieve LA on a specific date (label tuple)
# Slice by partial index

# Only LA OR SF rows
df = pd.DataFrame({
    "city": ["LA","NY","SF","LA","NY","SF"],
    "temp": [70, 55, 60, 75, 58, 62],
    "humidity": [30, 65, 55, 35, 70, 58],
    "date": pd.date_range("2021-01-01", periods=6)
})


# Practice Drills:
    # Given a list of numbers, return a list with each number squared
    # Given a list of numbers, return the even ones in that list
    # Return a dict of numbers with keys of even or odd depending on which qualify for either
    # Return a dict of numbers that are squared if they are above ten. Key should be the original value
    # print all users over 18
    # create a dict in which the users have their ages squared
    # write a list of identifiers of name and age from a dict of userse
    # filter the dict for adults. Anyone over 18 and above
    # flatted the sublist
class PythonPracticeDrills:
    def __init__(self):
        self.name = 'Python Practice Details'

    def listToSquares(self, numbers: list[int]):
        return [num * num for num in numbers]

    def listReturnEvensOnly(self, numbers: list[int]):
        return [ num for num in numbers if num % 2 == 0]
    
    def createEvenNumDict(self, numbers: list[int]):
        keys = [ 'even' if num % 2 == 0 else 'odd' for num in numbers]
        return dict(zip(keys, numbers))
    
    def createSquaredDict(self, numbers: list[int]):
        squared = [ num * num if num > 10 else num for num in numbers ]
        keys = [ num for num in numbers if num > 10 ]
        return dict(zip(keys,squared))
    
    def printUsersOver18(self, users: list[dict[str:int]]):
        for user in users:
            if(user['age'] > 18):
                print(f"{user['name']} is {user['age']}\n")
    
    def squaredAges(self, users: list[dict[str:int]]):
        return { user['name']:(user['age']*user['age']) for user in users }
    
    def userAgeIdentifier(self, users: list[dict[str:int]]):
        return  [f"{user['name']} is {user['age']}\n" for user in users ]
    
    def filterForAdults(self, users: list[dict[str:int]]):
        return { user['name']:user['age'] for user in users if user['age'] >= 18 }
    
    def flattenListOfSubLists(self, listOfListOfNums: list[list[int]]):
        return [ num for list in listOfListOfNums for num in list]
    

# class PythonPracticeDrills:
#     def __init__(self):
#         self.name="Python Practice Drills"

#     def listToSquares(self, numbers: list[int]):
#         return [i * i for i in numbers]

#     def listReturnEvensOnly(self, numbers: list[int]):
#         return [ i for i in numbers if i % 2 == 0] 

#     def createEvenNumDict(self, numbers: list[int]):
#         keys = [ "even" if i % 2 == 0 else 'odd' for i in numbers]
#         return dict(zip(numbers, keys))
    
#     def createSquaredDict(self, numbers: list[int]):
#         squared = [ num * num  for num in numbers if (num > 10) ]
#         numsAboveTen = [ num for num in numbers if (num > 10) ]
#         return dict(zip(numsAboveTen, squared))
    
#     def printUsersOver18(self, users: dict[str:int]):
#         return [ user['name'] for user in users if user['age'] >= 18 ]
    
#     def squaredAges(self, users: dict[str:int]):
#         return { user['name']:(user['age'] * user['age']) for user in users}
        
#     def userAgeIdentifier(self, users: dict[str:int]):
#         return [ f"{user['name']} is {user['age']}\n" for user in users]

#     def filterForAdults(self, users: dict[str:int]):
#         return { user['name']:user['age'] for user in users if(user['age'] >= 18)}
    
#     def flattenListOfSubLists(self, listOfListOfNums: list[list[int]]):
#         return [ list for listOfNums in listOfListOfNums for list in listOfNums ]

ppd = PythonPracticeDrills()
listOfSquares = ppd.listToSquares(listOfNums);
listOfEvens = ppd.listReturnEvensOnly(listOfNums)
dictOfNums = ppd.createEvenNumDict(listOfNums)
dictOfSquaredNums = ppd.createSquaredDict(listOfNums)
listOfUsersAge18AndOver = ppd.printUsersOver18(users)
usersAgeSquared = ppd.squaredAges(users)
# print(usersAgeSquared)
userAgeIdentified = ppd.userAgeIdentifier(users)
# print(f"{"".join(userAgeIdentified)}")
adultUsers = ppd.filterForAdults(users)
# print(adultUsers)
flattenedNums = ppd.flattenListOfSubLists(matrix)
print(flattenedNums)
