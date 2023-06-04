import random
import math
import numpy as np
import matplotlib.pyplot as plt
steps=10
N =16
def main():
    sumClassical_array=[]
    sumImportance_array=[]
    for _ in range(steps):
        sumClassical =0
        sumImportance = 0
        for _ in range(N):
            r=random.uniform(0,1)
            sumClassical +=math.sin(r*math.pi*0.5) # we scale the random number from [0,1] --> [0, pi/2]
            X_i = math.sqrt(r)*(math.pi*0.5)
            sumImportance+=(math.sin(X_i)/((8*X_i)/(math.pi*math.pi)))
        
        sumClassical_array.append(sumClassical*(math.pi*0.5)/N)
        sumImportance_array.append(sumImportance*(1.0)/N)

    x=np.linspace(1,steps,steps)
    analytic = np.ones(steps)

    plt.ylim(0, 1.3)  

    plt.xlabel("Samples")
    plt.ylabel("Integral value")

    plt.scatter(x, sumClassical_array, color='red', marker='o', label='classical MC')
    plt.plot(x,sumClassical_array,color='red')

    plt.scatter(x, sumImportance_array, color='blue', marker='o',label='Importance Sampling')
    plt.plot(x,sumImportance_array,color='blue')

    plt.plot(x,analytic,color='green', label='analytic value of the integral')
    plt.title('Classical Monte Carlo Integration vs \n Integration using Importance Sampling')
    plt.legend()
    plt.show()

main()