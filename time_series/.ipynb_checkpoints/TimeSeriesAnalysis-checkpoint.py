# imports
import numpy as np


# evaluation
def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100



# prediction "models"
def moving_average(series, n):
    """
        Calculate average of last n observations
        Can predict 1 future value
    """
    return np.average(series[-n:])



def weighted_average(series, weights):
    """
        Calculate weighter average on series
    """
    result = 0.0
    weights.reverse()
    for n in range(len(weights)):
        result += series.iloc[-n-1] * weights[n]
    return float(result)