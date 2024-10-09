#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!
import argparse
from fibonnaci import fib_limit

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def maxprimefib(limit):
    prime_fib = []
    fib = fib_limit(limit)
    for i in fib:
          if check_prime(i):
              prime_fib.append(i)
    return (max(prime_fib))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("limit", type = float,help = 'upper_limit')
	args = parser.parse_args()
	max_prime_fib = maxprimefib(args.limit)
	print(f'The largest prime Fibonacci number is:{max_prime_fib}')

    



