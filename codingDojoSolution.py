#Helper functions for tasks######################

#returns all subsets of an array of numbers
def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]
 

#returns the digital root of a given number
def digitalRoot(number):
    while(len(str(number)) > 1):
        currentSum = 0
        for digit in str(number):
            currentSum += int(digit)
        number = currentSum
    return number

#################################################

def part1(numbers, value):
    mySubsets = subsets(numbers)
    answerList=[]
    for x in mySubsets:
        if sum(x) == value:
            answerList.append(x)
    return(answerList)


def part3(numbers, value):
    mySubsets = subsets(numbers)
    answerList=[]
    for x in mySubsets:
        if digitalRoot(sum(x)) == value:
            answerList.append(x)
    return(answerList)



print(part1([1,2,3,4,5], 7))
print(part1([], 5))
print(part1([1,2,3,4,5,10], 10))

print(digitalRoot(345))
print(digitalRoot(7))
print(digitalRoot(6589))

print(part3([1,2,5,8], 7))
print(part3([1], 5))
print(part3([100,3,5,7,8], 2))

