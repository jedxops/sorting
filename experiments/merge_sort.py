# Jeff Austin
# 7/16/2019
# Portland State University
# CS350
# Daniel LeBlanche
# HW3
# Merge sort code in pyhton 3

import sys
import random
import time
import math

# merge sort algorithm
# taken from D. LeBlanche's slides: http://web.cecs.pdx.edu/~dleblanc/cs350/sorting.pdf
def merge_sort(A):
  if len(A) == 0:
      return []
  if len(A) == 1:
    return A
  mid = math.floor(len(A) // 2)
  B = []
  C = []
  #for i in range(mid - 1):  #these were making my code run infinitely.
    #B.append(A[i])          #slice operators saved the day!
  B = merge_sort(A[:mid])
  #for i in range(mid, len(A) - 1):
  #  C.append(A[i])
  C = merge_sort(A[mid:])
  return merge_lists(B, C)

# merge two lists
# taken from D. LeBlanche's slides: http://web.cecs.pdx.edu/~dleblanc/cs350/sorting.pdf
def merge_lists(B, C):
  i = 0
  j = 0
  A = []
  while i < len(B) and j < len(C):
    if B[i] <= C[j]:
      A.append(B[i])
      i = i + 1
    else:
      A.append(C[j])
      j = j + 1
  if i == len(B):
    Z = []
    for i in range(j, len(C)):
      Z.append(C[i])
    A = A + Z
  else:
    Z = []
    for k in range(i, len(B)):
      Z.append(B[k])
    A = A + Z
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
  list = merge_sort(list)
  ticks2 = time.time()

  print("Total merge sort time taken in seconds: " + str('%.3f'%(ticks2 - ticks1)) + '.')
  #print("sorted")
  #print(list)
  return

if __name__ == '__main__':
  main()
