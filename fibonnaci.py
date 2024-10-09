#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def fib_limit(limit):
    fiblist = [0,1]
    while fiblist[-1] + fiblist[-2] <= limit:
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("output_file", type=str, help = 'output_file_fibonacci')
	parser.add_argument("limit", type = float,help = 'upper_limit')
	
	args = parser.parse_args()
	fib = fib_limit(args.limit)
    
	try:
		with open(args.output_file, 'w') as file:
			for i in fib:
				file.write(f"{i}\n")
	except IOError:
		print("wrong!")

