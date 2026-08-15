# program to find maximum and minimum in list !
# without using max() and min() function
numbers =[ 10 , 25 ,5 ,12, 44]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers :
    if num > maximum:
        maximum = num
    if num < minimum :
        minimum = num

print("Maximum:",maximum)
print("Minimum:",minimum)    