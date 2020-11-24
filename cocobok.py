

def drop_frist_last(grades):
  frist,*middle,last = grades
  return avg(*middle)
    

if __name__ == "__main__":

  data  = (3,5,6,5,54,4,33,9)
  drop_frist_last(data)




