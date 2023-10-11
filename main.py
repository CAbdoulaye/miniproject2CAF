# INF601 - Advanced Programming in Python
# Cheikh Abdoulaye Faye
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

  # occupation name
  nameoOfOccupation = occupationName['Occupation'].iloc[0]

  # age info
  count = describe['Age'].iloc[0]
  ageMean = describe['Age'].iloc[1]
  ageStd = describe['Age'].iloc[2]
  ageMin = describe['Age'].iloc[3]
  ageMax = describe['Age'].iloc[7]

  # sleep duration info
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
  salespersons = data.loc[data['Occupation'] == 'Salesman']
  scientists = data.loc[data['Occupation'] == 'Scientist']
  teachers = data.loc[data['Occupation'] == 'Teacher']

  allOccupations = [
      accountants, doctors, engineers, lawyers, nurses, managers, salespersons,
      scientists, teachers
  ]
  return allOccupations


def sortOccupations(listOfOccupations):
  # sort dataframe to only get occupation, ages, ... ignore everything else I will not use
  for i in range(len(listOfOccupations)):
    listOfOccupations[i] = (listOfOccupations[i])[[
        'Occupation', 'Age', 'Sleep Duration', 'Quality of Sleep',
        'Stress Level'
    ]]
  return listOfOccupations


def getListOfMeans(descriptiveList):
  # return a list with only means
  newList = []
  newDict = {}
  for element in descriptiveList:
    # newDict['ageMean'] = element['ageMean']
    newDict['Occupation'] = element['Occupation']
    newDict['sleepDurationMean'] = element['sleepDurationMean']
    newDict['qualityOfSleepMean'] = element['qualityOfSleepMean']
    newDict['stressLevelMean'] = element['stressLevelMean']
    newList.append(newDict)
  return newList


def makeAllGraphs(descriptions):
  # make individual graphs for each field and one with all together
  makeIndividualGraph(descriptions, 'sleepDurationMean',
                      'Hours of Sleep per Occupation', 'Hours')
  makeIndividualGraph(descriptions, 'qualityOfSleepMean',
                      'Quality of Sleep per Occupation', 'PSQI')
  makeIndividualGraph(descriptions, 'stressLevelMean',
                      'Stress Level per Occupation', 'HRV')
  finalGraph(descriptions)

def makeIndividualGraph(descriptions, name, title, ylabel):
  # Graph each bar individully
  values = []
  keys = []
  for element in descriptions:
    values.append(element[name])
    keys.append(element['Occupation'])
  plt.bar(keys, values)
  addLabels(values)
  plt.ylabel(ylabel)
  plt.xlabel('Occupations')
  plt.title(title)
  # Save graphs to png files
  fileName = "Charts/" + name + ".png"
  plt.savefig(fileName)
  plt.show()


def addLabels(yValues):
  # add y value on each bar
  for i in range(len(yValues)):
    plt.text(i, (yValues[i] + 0.1), yValues[i])


def finalGraph(data):
  # Graph all bars on the same y-x plan
  listOfList = []
  keys = []
  values = []
  x = len(data)
  x = np.arange(x)
  names = ["sleepDurationMean", 'qualityOfSleepMean', 'stressLevelMean']
  attributes = ['hoursofsleep', 'qualityofsleep', 'stresslevel']
  colors = ['b', 'g', 'r']
  for i in range(3):
    for element in data:
      if i == 1:
        keys.append(element['Occupation'])
      values.append(element[names[i]])
    listOfList.append(values)
    plt.bar((x + (0.25 * (i + 1))) * 2,
            listOfList[0],
            color=colors[i],
            width=0.50,
            label=attributes[i])
    plt.xticks((x + 0.5) * 2, keys)
    values.clear()
  plt.legend(loc='upper right', ncols=3)
  plt.ylim(0, 9)
  plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='y', alpha=0.2)
  plt.xlabel('Occupations')
  plt.title('Hours of Sleep vs Quality of Sleep vs Stress Level')
  fileName = "Charts/CombinedGraph.png"
  plt.savefig(fileName)
  plt.show()


try:
  Path("Charts").mkdir()
except:
  pass

# convert cvs file to pd dataframe and stored it to dataframe
dataframe = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv',
                        index_col='Person ID')

# sorted dataframe by occupation
dataframe = dataframe.sort_values(by=['Occupation'])

occupations = getOccupationsList(dataframe)

sortedOccupations = sortOccupations(occupations)

descriptionList = getInfoList(sortedOccupations)

makeAllGraphs(descriptionList)