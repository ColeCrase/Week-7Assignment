"""
File: Project1
Author: Cole Crase
This program is to create a set of functions
that compute the median, mode, and mean of a set of numbers.
"""

def median(median):
    """Returns the median of a number set"""
    if len(median) == 0:
        return '0'
    midpoint = len(median) // 2
    print("The median is", end=" ")
    if len(median) % 2 == 1:
        print(median[midpoint])
    else:
        print((median[midpoint] + median[midpoint - 1]) / 2)

def mode(mode):
    """Returns the mode of a number set"""
    if len(mode) == 0:
        return '0'
    number = []
    numberz = {}
    for thenumber in mode:
        num = numberz.get(thenumber, None)
        if num == None:
            numberz[thenumber] = 1
        else:
            numberz[thenumber] = num + 1
            
    theMaximum = max(numberz.values())
    for key in numberz:
        if numberz[key] == theMaximum:
            print("The mode is", key)

def mean(mean):
    """Returns the mean of a number set"""
    number = []
    theSum = sum(number)
    x = len(number)
    if x == 0:
        return "0"
    avg = (theSum / x)
    print("The mean is", avg)

def main():
   """The main funcion of this script"""
   numbers = input("Enter a set of numbers: ").split(",")
   operation = input("Do you want it compute to median, mode, or mean?: ")
   operators = ['median', 'mode', 'mean']
   theoperator = operators.index(operation)

   if theoperator == 0:
       return median(numbers)
   elif theoperator == 1:
       return mode(numbers)
   elif theoperator == 2:
       return mean(numbers)
if __name__ == "__main__":
       main()
