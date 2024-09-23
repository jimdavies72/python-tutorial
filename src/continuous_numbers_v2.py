# continuous_numbers_v2.py

import inspect

# from a list of numbers, how many numbers are needed to create a continues
# sequence of numbers?

# -- input --
input_list = [6, 3, 9, "a", 14, None, 4, 6, 9, 10, 11]
# input_list = [] # expected fail
# input_list = "hello" # expected fail
# input_list = [1, 2] # expected 0


# 0. Check input_list contains at least 2 values: if len(input_list) >= 2:
# 1. Clear the list of junk data. 
# 2. Remove duplicates
# 3. Identify highest and lowest numbers in list : get highest - lowest.
#    Expected output: [3, 4, 6, 9, 10, 11, 14]
# 4. Get subset of list values: set(range(min - max)) - set(output from above)
#    Expected output: [5, 7, 8, 12, 13]
# 5. Count number of values - len(list)
#    Expected output: 5

def remove_notints_from_list(list) -> list:
  for item in list:
    if type(item) != int:
      list.remove(item)
  
  return list

def remove_duplicates(dupe_list) -> list: 
  return(list(dict.fromkeys(dupe_list)))

def missing_list(list) -> list:
  return sorted(set(range(list[0], list[-1])) - set(list))
  
def main(input_list):
  try:
    # test input is valid
    if type(input_list) is list and len(input_list) >= 2:
      int_list = remove_notints_from_list(input_list)
      clean_list = remove_duplicates(int_list)
      clean_list.sort()
      missing_elements = missing_list(clean_list)
      
      print(f"Missing list elements are: {missing_elements}")
      print(f"Numbers needed to produce continuous list: {len(missing_elements)}")
      
    else:
      raise Exception("Invalid input list provided")
    
  except Exception as e:
    print(f"Exception: {e}, occured in function: {inspect.stack()[0][3]}")
    

main(input_list)