import numpy as np
import pandas as pd

def getData():
    data = pd.read_excel('./Module6_Data.xlsx')
    return data

def maxWaterConsumption(data):
    return data["NYC Consumption(Million gallons per day)"].max()

def calendarYear(data):
    return np.shape(data['Year'])

def meanAndSTD(data):
    mean = np.mean(data['Per Capita(Gallons per person per day)'])
    std = np.std(data['Per Capita(Gallons per person per day)'])

    print(mean, " | ", std)

    return mean, std

def changeInPopulation(data):
    pop_diff = np.diff(data['New York City Population'])
    print(pop_diff)

def main():
   data = getData()
   print(maxWaterConsumption(data))

   print(calendarYear(data))

   print(meanAndSTD(data))

   changeInPopulation(data)

if __name__ == '__main__':
    main()