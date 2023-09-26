from matplotlib import pyplot as plt
import numpy as np

#Uniform distribution of X amount of random numbers
def getUniformDist(x):
    #This determines the "randomness"
    np.random.seed(7)
    r = np.random.uniform(low=0, high=1,size=x)
    
    #Mean of the random numbers
    print('Mean ')
    print(np.mean(r))

    #Standard deviation of random numbers (how far apart each value is)
    print('Standard Deviation ')
    print(np.std(r))

    #Variation of random numbers (Sd = root(variance)) Total of differences in the set??
    print('Variance ')
    print(np.var(r))

    #Each bin represents how often that value was called in the uniform distribution
    plt.hist(r, bins=30)
    plt.title('Uniform Distribution of ' + str(x))
    plt.xlabel('Random Number Value')
    plt.ylabel('Quantity in Distribution')
    plt.axvline(np.mean(r), color='red', linestyle='dashed',linewidth=1)
    plt.text(np.mean(r), .5, format(np.mean(r), '.4f'))

    plt.show()


#Exponential distribution of X amount of random numbers
def getExpDest(x):
    np.random.seed(7)
    expo = np.random.exponential(scale=7,size=x)

   
    #Mean of the random numbers
    print('Mean ')
    print(np.mean(expo))

    #Standard deviation of random numbers (how far apart each value is)
    print('Standard Deviation ')
    print(np.std(expo))

    #Variation of random numbers (Sd = root(variance)) Total of differences in the set??
    print('Variance ')
    print(np.var(expo))

    #Each bin represents how often that value was called in the uniform distribution
    plt.hist(expo, bins=30)
    plt.title('Exponential Distribution of ' + str(x))
    plt.xlabel('Random Number Value')
    plt.ylabel('Quantity in Distribution')
    plt.axvline(np.mean(expo), color='red', linestyle='dashed',linewidth=1)
    plt.text(np.mean(expo), .5, format(np.mean(expo), '.4f'))


    plt.show()


#Poisson distribution of X amount of random numbers
def getPoisDist(x):
    np.random.seed(7)

    poisson = np.random.poisson(lam=7, size=x)
   
    #Mean of the random numbers
    print('Mean ')
    print(np.mean(poisson))

    #Standard deviation of random numbers (how far apart each value is)
    print('Standard Deviation')
    print(np.std(poisson))

    #Variation of random numbers (Sd = root(variance)) Total of differences in the set??
    print('Variance ')
    print(np.var(poisson))

    #Each bin represents how often that value was called in the uniform distribution
    plt.hist(poisson, bins=30)
    plt.title('Poisson Distribution of ' + str(x))
    plt.xlabel('Random Number Value')
    plt.ylabel('Quantity in Distribution')
    plt.axvline(np.mean(poisson), color='red', linestyle='dashed',linewidth=1)
    plt.text(np.mean(poisson), .5, format(np.mean(poisson), '.4f'))
    plt.show()


#Get the distribution type from parameters and call sample size
def getDistribution(type, sample):
    if(type == 'Uniform'):
        getUniformDist(sample)
    elif(type == 'Expo'):
        getExpDest(sample)
    elif(type == 'Poisson'):
        getPoisDist(sample)
    else:
        print("Distribution Not available. Try another one")
    


#Constantly request input for distributions
while(True):
    type = input("\n Distribution Type (Uniform, Expo, Poisson) :").strip()
    sample = int(input("Sample Size : "))

    if((sample >= 1) and (sample <= 100000)):
        getDistribution(type, sample)

    else:
        print("Sample Size Invalid")