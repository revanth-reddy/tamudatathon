# from selenium import webdriver
# url = 'https://devpost.com/hackathons?page=2'
# driver = webdriver.Chrome()
# driver.get(url)

# hacks = driver.find_elements_by_class_name('hackathon-tile')
# # print(hacks)
# for hack in hacks:
#     title = hack.get_attribute('innerHTML')
#     status = hack.find_element_by_class_name('mb-4').text
#     info = hack.find_element_by_class_name('info').text
#     # title=hack.find_element_by_xpath('.//*[@id="results-and-filters"]/div[2]/div[2]/div[1]/a/div[1]/div/h3').text
#     print(status)
#     break
# driver.__exit__()
import dateutil.parser as parser
from datetime import datetime

def clean_date(date):
  if date=='':
    return '',''
  else:
    if '-' not in date:
      try:
        d = parser.parse(date)
        d = datetime.strftime(d, "%m/%d/%Y")
        return d,d
      except:
        return date,date
    elif '-' in date:
      s = date.split()
      if len(s)==5:
        try:
          d1 = s[0]+' '+s[1]+' '+s[4]
          d2 = s[0]+' '+s[3][:-1]+' '+s[4]
          d1 = datetime.strftime(parser.parse(d1), "%m/%d/%Y")
          d2 = datetime.strftime(parser.parse(d2), "%m/%d/%Y")
          return d1,d2
        except:
          return date,date
      elif len(s)==6:
        try:
          d1 = s[0]+' '+s[1]+' '+s[5]
          d2 = s[3]+' '+s[4][:-1]+' '+s[5]
          print(d1,d2)
          d1 = datetime.strftime(parser.parse(d1), "%m/%d/%Y")
          d2 = datetime.strftime(parser.parse(d2), "%m/%d/%Y")
          return d1,d2
        except:
          return date,date
      elif len(s)==7:
        try:
          d1 = s[0]+' '+s[1][:-1]+' '+s[2]
          d2 = s[4]+' '+s[5][:-1]+' '+s[6]
          print(d1,d2)
          d1 = datetime.strftime(parser.parse(d1), "%m/%d/%Y")
          d2 = datetime.strftime(parser.parse(d2), "%m/%d/%Y")
          return d1,d2
        except:
          return date,date
    
    return date,date

# s = 'Aug 31 - Oct 29, 2021'
# s = 'Oct 15 - 31, 2021'
# s = 'Oct 15 2021'
# s = 'Sep 08 - Nov 03, 2021'
s = 'Nov 01, 2021 - Feb 13, 2022'
s = 'Sep 01, 2021 - Sep 27, 2022'
print(clean_date(s))

