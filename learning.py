import numpy as np
import requests

def lagouSpider():

  page = 1
  lang_name = 'python'

  url = "http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
  data = {'first': 'true', 'pn': page, 'kd': lang_name}
  json = requests.post(url, data).json()
  
  print(json)



if __name__ == "__main__":

  lagouSpider()

