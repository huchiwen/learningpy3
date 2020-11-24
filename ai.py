#!/usr/bin/env python3
"""
author: huchiwen
language :python3

"""

def main():
    A = [1,2,3]
    B = [1,89,3]
    res =0

    result  = (len(A) == len(B)) 
    if result:
      for i in range(0,len(A)):
          res+=A[i]*B[i]
      print(res)
    else:
      print("list not equal")

if __name__ == "__main__":
    main()
