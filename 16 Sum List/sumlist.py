import statistics

#numbers
numbers = [27, 865, 482, 977, 525, 318, 678, 134, 651, 262, 352, 277, 9, 986, 27, 18, 805, 356, 715, 881, 851, 196, 171, 850, 336, 61, 90, 292, 860, 754]

#mean median using function
def average(list):
    return sum(list)/len(list)
average = average(numbers)

#mean median using statistics import
mean_numbers = statistics.mean(numbers)
median_numbers = statistics.median(numbers)

#print
print("Mean of numbers via Function: ", average)
print("Mean of numbers via Statistics: ", mean_numbers)
print("Median of numbers via Statistics: ", median_numbers)