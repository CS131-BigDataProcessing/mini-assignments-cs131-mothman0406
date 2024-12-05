# stats_function.py
import statistics

def calculate_mean(ages):
    """Calculates the mean of the ages."""
    return sum(ages) / len(ages)

def calculate_median(ages):
    """Calculates the median of the ages."""
    return statistics.median(ages)

