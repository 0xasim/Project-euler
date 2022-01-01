from utils import timeMe

'''
Takes 90s very bad time complexity probably due to dvsble list
Replace it with a separate function ismultiple for better
'''

def smallest_multiple(lim):
  n = 1
  while True:
    dvsble = []
    for en in range(1, lim+1):
      dvsble.append(n%en == 0)
      if n%en!=0: break
    if all(dvsble): return n
    n += 1

if __name__ == "__main__":
  print(timeMe(smallest_multiple, 20))
