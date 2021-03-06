# Jeff Austin
# 7/16/2019
# Portland State University
# CS350
# Daniel LeBlanche
# HW3
# Insertion sort code in pyhton 3

import sys
import random
import time

# insertion sorting algorithm
# taken from D. LeBlanche's slides: http://web.cecs.pdx.edu/~dleblanc/cs350/sorting.pdf
# also an inspiration of: https://github.com/aligoren/pyalgo/blob/master/insertionSort.py
# credit to that github user (LICENSE at the bottom of this file)
def insertion_sort(A):
  for j in range(1, len(A)):
    key = A[j]
    i = j
    while i > 0 and A[i - 1] > key:
      A[i] = A[i - 1]
      i = i - 1
    A[i] = key
  return A

# generate list
def gen_list(size):
  random.seed()
#  n = random.randint(0, size)
  liss = []

  i = 0
  while i < size:
      liss.append(random.randint(0, 100))  # fill the list with values from zero to 100
      i = i + 1
  return liss

def main():
  if len(sys.argv) < 1:
    print("Error. Not enough arguments")
    return
  size = int(sys.argv[1])
  ticks1 = time.time()
  list = gen_list(size)
  ticks2 = time.time()

# formatting idea came from: https://stackoverflow.com/questions/8595973/truncate-to-three-decimals-in-python
  print("Total time to generate list in seconds: " + str('%.3f'%(ticks2 - ticks1)) + '.')

  ticks1 = time.time()
  sorted = insertion_sort(list)
  ticks2 = time.time()

  print("Total insertion sort time taken in seconds: " + str('%.3f'%(ticks2 - ticks1)) + '.')
#  print("Sorted: ")
#  print(sorted)
  return

if __name__ == '__main__':
  main()


'''
The MIT License (MIT)

Copyright (c) 2015 Ali GOREN

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
