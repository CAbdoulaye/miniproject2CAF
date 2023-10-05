#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#       Think of some question you would like to solve such as:
#       "How many homes in the US have access to 100Mbps Internet or more?"
#       "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#       Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

# INF601 - Advanced Programming in Python
# Cheikh Abdoulaye Faye
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def getInfoList(occupationsList):
    # return list of all occupation dataframe descriptions
    allOccupationsInfo = []
    for element in occupationsList:
        occupationInfo = getInfo(element)
        allOccupationsInfo.append(occupationInfo)

    return allOccupationsInfo

def getInfo(occupationName):
    # return dictionary of occupation dataframe description
    describe = occupationName.describe()
    describe = describe.round(2)

    #occupation name
    nameoOfOccupation = occupationName['Occupation'].iloc[0]

    # age info
    count = describe['Age'].iloc[0]
    ageMean = describe['Age'].iloc[1]
    ageStd = describe['Age'].iloc[2]
    ageMin = describe['Age'].iloc[3]
    ageMax = describe['Age'].iloc[7]
    # Sleep duration info
    sleepDurationMean = describe['Sleep Duration'].iloc[1]
    sleepDurationStd = describe['Sleep Duration'].iloc[2]
    sleepDurationMin = describe['Sleep Duration'].iloc[3]
    sleepDurationMax = describe['Sleep Duration'].iloc[7]
    # Quality of Sleep info
    qualityOfSleepMean = describe['Quality of Sleep'].iloc[1]
    qualityOfSleepStd = describe['Quality of Sleep'].iloc[2]
    qualityOfSleepMin = describe['Quality of Sleep'].iloc[3]
    qualityOfSleepMax = describe['Quality of Sleep'].iloc[7]
    # Stress Level info
    stressLevelMean = describe['Stress Level'].iloc[1]
    stressLevelStd = describe['Stress Level'].iloc[2]
    stressLevelMin = describe['Stress Level'].iloc[3]
    stressLevelMax = describe['Stress Level'].iloc[7]

    infoDictionary = {}
    infoDictionary['Occupation'] = nameoOfOccupation

    infoDictionary['count'] = count
    infoDictionary['ageMean'] = ageMean
    infoDictionary['ageStd'] = ageStd
    infoDictionary['ageMin'] = ageMin
    infoDictionary['ageMax'] = ageMax

    infoDictionary['sleepDurationMean'] = sleepDurationMean
    infoDictionary['sleepDurationStd'] = sleepDurationStd
    infoDictionary['sleepDurationMin'] = sleepDurationMin
    infoDictionary['sleepDurationMax'] = sleepDurationMax

    infoDictionary['qualityOfSleepMean'] = qualityOfSleepMean
    infoDictionary['qualityOfSleepStd'] = qualityOfSleepStd
    infoDictionary['qualityOfSleepMin'] = qualityOfSleepMin
    infoDictionary['qualityOfSleepMax'] = qualityOfSleepMax

    infoDictionary['stressLevelMean'] = stressLevelMean
    infoDictionary['stressLevelStd'] = stressLevelStd
    infoDictionary['stressLevelMin'] = stressLevelMin
    infoDictionary['stressLevelMax'] = stressLevelMax

    return infoDictionary

def getOccupationsList(data):
    # return a list with each occupation as a dataframe
    accountants = data.loc[data['Occupation'] == 'Accountant']
    doctors = data.loc[data['Occupation'] == 'Doctor']
    engineers = data.loc[data['Occupation'] == 'Engineer']
    lawyers = data.loc[data['Occupation'] == 'Lawyer']
    nurses = data.loc[data['Occupation'] == 'Nurse']
    managers = data.loc[data['Occupation'] == 'Manager']
    salesRepresentatives = data.loc[data['Occupation'] == 'Sales Representative']
    salespersons = data.loc[data['Occupation'] == 'Salesperson']
    scientists = data.loc[data['Occupation'] == 'Scientist']
    softwareEngineers = data.loc[data['Occupation'] == 'Software Engineer']
    teachers = data.loc[data['Occupation'] == 'Teacher']

    allOccupations = [accountants, doctors, engineers, lawyers, nurses, managers, salesRepresentatives, salespersons,
                   scientists, softwareEngineers, teachers]
    return allOccupations

def sortOccupations(listOfOccupations):
    # sort dataframe to only get occupation, ages, ... ignore everything else I will not use
    for i in range(len(listOfOccupations)):
        listOfOccupations[i] = (listOfOccupations[i])[['Occupation', 'Age', 'Sleep Duration', 'Quality of Sleep', 'Stress Level']]
    return listOfOccupations

def makeGraphs(descriptions):
    meansList = getListOfMeans(descriptions)
    keys = list(meansList[0].keys())
    values = list(meansList[0].values())
    length = len(meansList[0])
    print('keys = ')
    print(keys)
    plt.bar(range(length), values, tick_label=keys)
    # Save graphs to png files
    fileName = "Charts/ch.png"
    plt.savefig(fileName)
    plt.show()

def makeOtherGraph(descriptions):
    values = []
    keys = []
    for element in descriptions:
        values.append(element['sleepDurationMean'])
        keys.append(element['Occupation'])
    length = len(descriptions)
    plt.bar(range(length), values, tick_label=keys)
    # Save graphs to png files
    fileName = "Charts/ch2.png"
    plt.savefig(fileName)
    plt.show()

def getListOfMeans(descriptiveList):
    newList = []
    newDict = {}
    for element in descriptiveList:
        #newDict['ageMean'] = element['ageMean']
        newDict['Occupation'] = element['Occupation']
        newDict['sleepDurationMean'] = element['sleepDurationMean']
        newDict['qualityOfSleepMean'] = element['qualityOfSleepMean']
        newDict['stressLevelMean'] = element['stressLevelMean']
        newList.append(newDict)
    return newList

def changeOccupationsNames(data):

    print(data.at[4, 'Occupation'])
    print(data.at[5, 'Occupation'])

    data.at[4, 'Occupation'] = 'Salesman'
    data.at[5, 'Occupation'] = 'Salesman'

    print(data.at[4, 'Occupation'])
    print(data.at[5, 'Occupation'])

try:
    Path("Charts").mkdir()
except:
    pass

# convert cvs file to pd dataframe and stored it to dataframe
dataframe = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv',  index_col='Person ID')

#changeOccupationsNames(dataframe)

# sorted dataframe by occupation
dataframe = dataframe.sort_values(by=['Occupation'])

occupations = getOccupationsList(dataframe)

sortedOccupations = sortOccupations(occupations)

descriptionList = getInfoList(sortedOccupations)

# makeGraphs(descriptionList)
makeOtherGraph(descriptionList)