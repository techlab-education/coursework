# import packages:
import pickle
import numpy as np
import scipy.stats as scs


# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name, 'rb'), encoding='bytes')


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    pass


def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    pass


def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    pass


def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    
    hint: definition (we didn't go over this in Week 2 Lecture):
    http://onlinestatbook.com/glossary/sem.html
    """
    pass


def get_confidence_interval(sample, confidence=.95):
    """INPUT:
    - sample(NUMPY ARRAY)
    - confidence(FLOAT) [The confidence of the ci from 0 to 1, usually .95]

    OUTPUT:
    - (tuple) [mean, mean - half_rng, mean + half_rng]
    """
    pass


def get_interquartile_range(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - iqr(FLOAT) [Interquartile range]
    """
    pass


def get_outlier(population):
    """INPUT:
    - population(NUMPY ARRAY)

    OUTPUT:
    - outliers(NUMPY ARRAY) [List of outliers]
    """
    pass


if __name__ == '__main__':
    population = load_pickle('population.pkl')
    print('First 10 element of the population: ', population[:5])
