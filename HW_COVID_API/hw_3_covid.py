import json
from operator import indexOf
from statistics import mean
import requests


url1 = "https://covid-api.mmediagroup.fr/v1/history?country=Finland&status=confirmed"
url2 = "https://covid-api.mmediagroup.fr/v1/history?country=US&status=confirmed"
url3 = "https://covid-api.mmediagroup.fr/v1/history?country=Russia&status=confirmed"

print("Covid confirmed cases statistics")
print("----------------------------------------------------")

def complete_Homework(url):

  req = requests.get(url)

  dct1 = json.loads(req.text)

  confirmed = []
  dates = []
  new_cases = []
  month_year = []
  month_distinct = []
  using_dictionary = {}
  json_dictionary = {}

  output = "Country name: " + str(dct1["All"]["country"]) + '\n'
  json_dictionary['Country Name'] = dct1["All"]["country"]

# take JSON and make it a list of dates, cases, and new_cases

  for date in dct1["All"]["dates"].keys():
    dates.append(date)

  for cases in dct1["All"]["dates"].values():
    confirmed.append(cases)

  for i in range(len(confirmed) - 1):
    new_cases.append((confirmed[i] - confirmed[i + 1]))

  # print("Average number of new daily confirmed cases for the entire dataset:", "%.2f" %mean(new_cases))
  output += "Average number of new daily confirmed cases for the entire dataset: " +  str("%.2f" %mean(new_cases)) + '\n'
  json_dictionary["Average number of new daily confirmed cases for the entire dataset:"] = "%.2f" %mean(new_cases)
  # find date with the highest new number of cases

  for i in range(len(dates) - 1):
    if new_cases[i] == max(new_cases):
      # print("Date with the highest new number of confirmed cases is:", dates[i])
      output += "Date with the highest new number of confirmed cases is: " + str(dates[i]) + '\n'
      json_dictionary["Date with the highest new number of confirmed cases is:"] = dates[i]
  # most recent date with no new confirmed cases

  for i in range(len(dates) - 1):
    if new_cases[i] == 0:
      # print("Most recent date with no new confirmed cases:", dates[i])
      output += "Most recent date with no new confirmed cases: "+ str(dates[i]) + '\n'
      json_dictionary["Most recent date with no new confirmed cases:"] = dates[i]
      break

  # get JUST the month and the year from dates and put it into month_year
  for i in range(0, len(dates)):
    month_year.append(dates[i][:7])
    
  # put all distinct month_years, along with their new cases value in a dictionary

  for i in range(0, len(new_cases)):
    if month_year[i] in month_distinct:
      using_dictionary[month_year[i]] += new_cases[i]
    else:
      using_dictionary[month_year[i]] = new_cases[i]

  # take it back out of the dictionary to do more calculations on it
  # seperate month_year and and new_cases from the dictionary
  # im not sure why i put it into a dictionary in the first place

  list456 = []
  list_of_months = []

  for value in using_dictionary.values():
    list456.append(value)
  for key in using_dictionary.keys():
    list_of_months.append(key)

  max_month_index = indexOf(list456, max(list456))
  # print("Month with the highest number of new cases is", list_of_months[max_month_index])
  output += "Month with the highest number of new cases is: "+ str(list_of_months[max_month_index]) + '\n'
  json_dictionary["Month with the highest number of new cases is:"] = list_of_months[max_month_index]
  min_month_index = indexOf(list456, min(list456))
  # print("Month with the lowest number of new cases is", list_of_months[min_month_index])
  output += "Month with the lowest number of new cases is: "+ str(list_of_months[min_month_index]) + '\n'
  json_dictionary['Month with the lowest number of new cases is:'] = list_of_months[min_month_index]
  
  print(output)
  return json_dictionary


json.dump(complete_Homework(url1), open("Finland.json", "w"))
json.dump(complete_Homework(url2), open("US.json", "w"))
json.dump(complete_Homework(url3), open("Russia.json", "w"))



# notes for this assignment

# in one for loop, get total cases
  # all, dates print(d1["all"][])
# in one for loop, get new cases
# in one loop, get a list for your dates

# for date in dict1["all"]["dates"]
  #.items will give you a key value pair
  # print(dict1)['all']['dates'][date]