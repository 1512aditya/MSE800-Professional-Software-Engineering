import numpy as np

def mainFunction():
    Rain = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    #Convert the list to a NumPy array and print it.
    arrayRain = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
    print ('this is array : ',arrayRain)

    # Print the total rainfall for the week.
    total = np.sum(Rain)
    print (f'this is sum : {total:.2f}')

    #Print the average rainfall for the week.
    avg_rain = np.mean(Rain)
    print (f'this is avg rain : {avg_rain:.2f}')

    #Count how many days had no rain (0 mm).
    count = 0.0
    for rain in Rain:
        if rain == 0.0:
            count += 1

    print ('no rain days are : ',count)

    #Print the days (by index) where the rainfall was more than 5 mm.
    HighRainDays = np.where(arrayRain > 5)[0]
    print ('this are the high rain days: ', HighRainDays)

    # Calculate the 75th percentile of the rainfall data and identify values above it.
    Per75 = np.percentile(arrayRain, 75)
    print('75th percentile of rainfall:', Per75)

    # Values above the 75th percentile
    above_75Per = arrayRain[arrayRain > Per75]
    print('Rainfall values above 75th percentile:', above_75Per)

if __name__ == '__main__':
    mainFunction()