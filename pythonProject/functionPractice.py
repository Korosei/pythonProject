from math import sqrt, floor, pi
from datetime import datetime
import re

def max_of_two (num1, num2):
    return num1 if num1>num2 else num2


def fizz_bizz(num):
    div_by_3 = True if num%3 == 0 else False
    div_by_5 = True if num%5 == 0 else False

    if div_by_3 and div_by_5:
        return "FizzBuzz"
    elif div_by_3:
        return "Fizz"
    elif div_by_5:
        return "Buzz"
    else:
        return num


def speed_check(speed):
    demerit_count = 0
    if speed < 70:
        print("Ok")
    elif speed > 70:
        speed_diff = speed - 70
        demerit_count = speed_diff//5
        print(f"Points: {demerit_count}.", end=" ")
        if demerit_count > 12:
            print("License suspended.")


def show_numbers(limit):
    print ("1. 0 EVEN")
    for i in range(1, limit+1):
        is_odd = True if i % 2 != 0 else False
        if is_odd:
            print(f"{i+1}. {i} ODD")
        else:
            print(f"{i+1}. {i} EVEN")


def multiples(limit):
    three_sum = 0
    five_sum = 0
    for mul3 in range(0, limit+1, 3):
        three_sum += mul3
    for mul5 in range(0, limit+1, 5):
        five_sum += mul5

    print(three_sum)
    return three_sum+five_sum

def show_stars(rows):
    for row in range(1, rows+1):
        for star in range(row):
            print("*", end="")
        print()

def primeNumbers(limit):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime in primeList:
        if prime < limit:
            print(prime, end = " ")
        else:
            break

def primeCheck(number):
    isPrime = True
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    square = floor(sqrt(number))
    for prime in primeList:
        if square % prime == 0 and square > prime:
            isPrime = False
    return isPrime


def currentTime():
    current = datetime.now()
    print(current.strftime("%Y-%m-%d %H:%M:%S"))

def circleRadius(radius):
    return pi * radius**2

def reverseName(first, last):
    name = first + " " + last
    return name[::-1]

def listCreate(userInput):
    return list(userInput), tuple(userInput)

def extensionOut(filename):
    fileList = filename.split('.')
    return fileList[1]

def examinationDate(exam_st_date):
    month, day, year = exam_st_date
    print(f"The examination will start from: {month} / {day} / {year}")

#n+nn+nnn
def nAddition (number, limit):
    total = 0
    for mult in range(1, limit+1):
        tempTotal = 0
        multiplier = 1
        for i in range(1, mult+1):
            tempTotal += (number * multiplier)
            multiplier *= 10
        total += tempTotal

    return total

def nAddition(number):
    n1 = int("%s" % number)
    n2 = int("%s%s" %(number, number))
    n3 = int("%s%s%s" %(number, number, number))

    print(n1 + n2 + n3)

# print(max(4, 5))
# print(fizz_bizz(15))
# speed_check(300)
# showNumbers(3)
# print(multiples(20))
# show_stars(10)
# primeNumbers(10)
# print(primeCheck(1013))
# currentTime()
# print(circleRadius(1.1))
# print(reverseName("Kareem", "Khan"))
"""
userInput = "3, 5, 7, 23".replace(" ", "")
userList, userTuple = listCreate(userInput.split(","))
print(f"List: {userList}\nTuple: {userTuple}")
"""
# print(extensionOut("abc.java"))
"""
exam_st_date = (11, 12, 2014)
examinationDate(exam_st_date)
"""

#print(nAddition(5, 4))
nAddition(5)