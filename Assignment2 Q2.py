"""
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
for i in range(1, 51, 1):
  #  print(i*((i+1)/2))
 Total = sum(i for i in range(1, 51, 1))
print(f"The sum of numbers from 1 to 50 is {Total}")



