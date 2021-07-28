def average(lyst):
    """Returns the average of the number in lyst."""
    theSum = 0
    for number in lyst:
        theSum += number
        return theSum / len(lyst)
