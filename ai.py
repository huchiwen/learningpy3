#!/usr/bin/env python3

def check_list_equals(list1,list2):
    num1 = len(list1)
    num2 = len(list2)

    if num1 == num2:
        return True
    return False

def main():

    A = [1,2,3,3]
    B = [1,2,3]
    res =0
    result = check_list_equals(A,B) 
    if result:
      for i in range(0,len(A)):
          res+=A[i]*B[i]
      print(res)
    else:
      print("list not equal")


if __name__ == "__main__":
    main()
