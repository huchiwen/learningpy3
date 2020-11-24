#!/usr/bin/env python3
def check_list_equals(list1,list2):

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
            else:
                return False
def main():

    A = [1,2,3]
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
