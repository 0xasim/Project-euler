import functools
from utils import *

def oneSeq(n):
  def collatzSeq(n):
    nonlocal count
    count += 1
    if n != 1: return collatzSeq(n/2) if n%2==0 else collatzSeq(3*n+1)
    else: return count
  count = 0
  return collatzSeq(n)

largest = 0
largest_number = 0
for i in range(1, 10**6):
  terms = oneSeq(i)
  if terms > largest: 
    largest = terms
    largest_number = i

print(largest_number)
