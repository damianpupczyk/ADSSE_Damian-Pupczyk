import matplotlib.pyplot as plt
import numpy as np

n = np.array([10, 100, 1000, 10000, 100000])
dac = np.array([0, 0, 0.03127, 0.29533, 3.92185])
kadane = np.array([0, 0, 0, 0.01567, 0.19952])

dacmemory = np.array([39494, 39711, 41074, 41885, 42206])
kadanememory = np.array([35318, 35319, 36672, 36673, 36674])


plot1=plt.figure(1)
plt.plot(dac, n, label="Divide-and-Conquer", linestyle='-', marker='o', color='b')
plt.plot(kadane, n, label="Kadane", linestyle='-', marker='o', color='g')
plt.xlabel("Time (s)")
plt.ylabel("Array size (n)")
plt.legend()
plt.show()

plot2=plt.figure(2)
plt.plot(dacmemory, n, label="Divide-and-Conquer", linestyle='-', marker='o', color='b')
plt.plot(kadanememory, n, label="Kadane", linestyle='-', marker='o', color='g')
plt.xlabel("Memory (b)")
plt.ylabel("Array size (n)")
plt.legend()
plt.show()
