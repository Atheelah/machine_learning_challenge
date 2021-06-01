# CHALLENGE ONE

# IMPORTING NUMPY
import numpy as np

# CREATING AN ARRAY OF NUMBERS
number = np.arange(1, 21)

# TO GET THE MEAN
mean = np.mean(number)

# TO GET THE STANDARD DEVIATION
StandDev = np.std(number)

# TO GET THE VARIANCE
variance = np.var(number)

# HOW I WANT IT TO BE DISPLAYED
print("numbers :" + str(number) + "\n" +
      "Mean :" + str(mean) + "\n" +
      "Standard Deviation :" + str(StandDev) + "\n" +
      "Variance :" + str(variance))


# CHALLENGE TWO

# IMPORTING MATPLOTLIB.PYPLOT
import matplotlib.pyplot as plt

# CREATING AN ARRAY OF NUMBERS
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

# STATING WHERE AND WHAT THE LABELS SHOULD BE
plt.xlabel("NUMS")
plt.ylabel("BINS")
plt.title("Histogram of nums against bins")

# SETTING THE COLOR, AND WHAT MUST BE DISPLAYED
plt.hist(nums, bins, color="pink")

# ALLOWING THE HISTOGRAM TO BE DISPLAYED
plt.show()


