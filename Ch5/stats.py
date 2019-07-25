"""
Program: stats.py
Author: Kirill Redin
Description:
    This program counts median, mode and average
    of a set of a numbers.
"""

def main():
    numbers_str = str(input("Enter numbers separated by commas: "))
    numbers_str = numbers_str.split(',')
    numbers = []
    for number_str in numbers_str:
        numbers.append(int(number_str))
    print('Median is: ', median(numbers))
    print('Mode is: ', mode(numbers))
    print('Average is: ', mean(numbers))

def median(numbers):
    numbers.sort()
    medium = len(numbers) // 2
    if medium == 0:
        return (numbers[medium] + numbers[medium-1]) / 2
    else:
        return numbers[medium]

def mode(numbers):
    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    mode = []
    maximum = max(frequency_dict.values())
    for (number,  frequency) in frequency_dict.items():
        if frequency == maximum:
            mode.append(number)
    return mode

def mean(numbers):
    return sum(numbers) / len(numbers)

if '__name__' == '__main__':
    main()
    
