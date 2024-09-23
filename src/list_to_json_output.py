# list_to_json_output.py

import json
import inspect

RED = '\033[1;31m'
GREEN = '\033[1;32m'
NC = '\033[0m'

# ETL job - converting data from simple list to json export file
# convert a 2d list of data into json object and output to file

# 1. take schema and input list and convert to dictionary
# 2. convert dictionary to json object
# 3. output json object to file with given filename
# 4. report success back to user

schema = ["name", "age", "location", "degree"]
input_list= [
  ["james", 52, "liverpool"],
  ["mary", 27, "st. helens"],
  ["bob", 23, "runcorn"],
  ["sarah", None, "warrington", "BA 2:1 Art"],
]

def array_to_dictionary(list, schema):
  dict_list = []
  for rec in list:
    rec_dict = {}
    for i in range(len(rec)):
        rec_dict[schema[i]] = rec[i]
    dict_list.append(rec_dict)  
  
  return dict_list

def output_to_file(filename: str, data: json):
  try:
    status = True
    file = open(filename, "w")
    file.write(data)
  
  except Exception as e:
    print(f"Error: {e} occured in {inspect.stack()[0][3]}")
    status = False
  
  finally:
    if file and not file.closed:
      file.close()
    return status
    
def main(input_list, schema, filename):
  dict = array_to_dictionary(input_list, schema)
  json_object = json.dumps(dict, indent=2)
  file_written = output_to_file(filename, json_object)
  
  if file_written:
    print(f"{GREEN}File: {filename} was written successfully{NC}")
  else:
    print(f"{RED}File: {filename} was Not written successfully{NC}")

main(input_list, schema, "students.json")