# Sums and Digital Roots



### Task 1 - Sums of Combinations
Given an array of **distinct** integers and a target integer, return a list of all the **unique** combinations of integers where the sum of the integers equals the target integer. You may return the combinations in any order.

e.g.
> - integers = [1,2,3,4,5], target = 7 ---> returns [[2,5], [3,4], [1,2,4]]
> - integers = [], target = 5 ---> returns []
> - integers = [1,2,3,4,5,10], target = 10 ---> returns [[10], [2, 3, 5], [1, 4, 5], [1, 2, 3, 4]]


### Task 2 - Digital Roots
The digital root of a number is found by iteratively adding up it's digits until a single digit value is found.

e.g.
> - 345 
>   - 3 + 4 + 5 = 12 
>   - 1 + 2 = *3*

> - 7 = *7*

> - 6589 
>   - 6 + 5 + 8 + 9 = 28 
>   - 2 + 8 = 10
>   - 1 + 0 = 1
  
Given an integer, return its digital root.


### Task 3 - Bringing it Together
Given an array of **distinct** integers and a target integer, return a list of all the **unique** combinations of integers where the digital root of the sum of the integers equals the target integer. You may return the combinations in any order.

e.g.
> - integers = [1,2,5,8], target = 7 ---> returns [[2, 5], [1, 2, 5, 8]]
> - integers = [1], target = 5 ---> returns []
> - integers = [100,3,5,7,8], target = 2 ---> returns [[5, 7, 8], [3, 8], [100, 3, 7]]


### Bonus tasks (yay!)
1. There is a set of numbers that exists, where if just one of them is added to a given input list in Task 3, the number of possible combinations that give the correct digital root doubles. What is the set of numbers?

2. Repeat task 1, but this time allow for numbers to be reused an unlimited number of times.
  > - integers = [2,3,6,7], target = 7 ---> returns [[2,2,3], [7]]
  > - integers = [2,3,5], target = 8 ---> returns [[2,2,2,2],[2,3,3],[3,5]]
  > - integers = [2], target = 1 ---> returns []
