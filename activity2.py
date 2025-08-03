import numpy as np

def mainFunction():
    
    temp = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    # this is avg    
    avg_temp = np.mean(temp)
    print(f"Average Temperature (C): {avg_temp:.3f}")

    # this for min and max temp
    max_temp = np.max(temp)
    min_temp = np.min(temp)
    print(f"Highest Temperature (C): {max_temp}")
    print(f"Lowest Temperature (C): {min_temp}")
    # convert to Fahrenheit
    temp_f = temp * 9/5 + 32
    print("Temperatures in Fahrenheit:", temp_f)
    # calculate the hot days
    hot_days = np.where(temp > 20)
    print("temperature when > 20C:", hot_days)


if __name__ == "__main__":
    mainFunction()
